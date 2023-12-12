import asyncio
import random

from .message import ReqMessage, ResMessage, msg_from_packet
from .message.cloud import Cloud

class Connection(asyncio.Protocol):
  def __init__(self):
    self._disconnected_future = asyncio.Future()
    self._disconnected_future.set_result(True)
    self._next_seq = random.randrange(0x10000)
    self._timeout = 10.0
    self._reset_state()

  def _reset_state(self):
    self.transport = None
    self._incoming = bytearray()
    self._msg_futures = {}

  @property
  def connected(self):
    try:
      return not self.transport.is_closing()
    except AttributeError:
      return False

  @property
  def peername(self):
    return self.transport.get_extra_info('peername')

  def _write(self, x: bytes):
    try:
      self.transport.write(x)
    except AttributeError:
      raise Exception('disconnected')

  def send_request(self, msg: ReqMessage):
    if not isinstance(msg, ReqMessage):
      raise Exception(f'Tried to send {type(msg).__qualname__} as request')

    if msg.seq is None:
      msg.seq = self._next_seq
      self._next_seq = (self._next_seq + 1) & 0xFFFF

    # Workaround for a bug in Hoymiles' cloud due to which the response will be sent with different sequence number.
    if isinstance(msg, Cloud.DevConfigReport.Req):
      self._last_dev_config_report_seq = msg.seq

    fut = asyncio.Future()
    self._msg_futures[msg.seq] = fut
    print(f'Sending request {type(msg).__qualname__} seq {msg.seq}')
    self._write(msg.ToPacket())
    return asyncio.ensure_future(asyncio.wait_for(fut, self._timeout))

  def send_response(self, orig_msg: ReqMessage, msg: ResMessage):
    if not isinstance(msg, ResMessage):
      raise Exception(f'Tried to send {type(msg).__qualname__} as response')
    msg.seq = orig_msg.seq
    print(f'Sending response {type(msg).__qualname__} seq {msg.seq}')
    self._write(msg.ToPacket())

  def disconnect(self):
    try:
      self.transport.close()
    except AttributeError:
      pass
    return self._disconnected_future

  def connection_made(self, transport):
    self._disconnected_future = asyncio.Future()
    self.transport = transport
    print('Connected')
    asyncio.create_task(self.on_connected())

  async def on_connected(self):
    pass

  def connection_lost(self, exc):
    print('Disconnected')
    for fut in self._msg_futures.values():
      fut.set_exception(Exception('disconnected'))
    asyncio.create_task(self.on_disconnected(exc))
    self._reset_state()
    self._disconnected_future.set_result(True)

  async def on_disconnected(self, exc: Exception):
    pass

  def data_received(self, data):
    self._incoming.extend(data)
    while self._incoming:
      try:
        if self._incoming[:2] != b'HM':
          print(self._incoming)
          raise Exception("Packet does not start with HM")
      except IndexError:
        break

      buffer_len = len(self._incoming)
      if len(self._incoming) < 10:
        break

      packet_len = int.from_bytes(self._incoming[8:10], byteorder='big')
      if buffer_len < packet_len:
        break

      packet = self._incoming[:packet_len]
      del self._incoming[:packet_len]
      msg = msg_from_packet(packet)

      if isinstance(msg, ResMessage):
        print(f'Received response {type(msg).__qualname__} seq {msg.seq}')
        seq = msg.seq
        if isinstance(msg, Cloud.DevConfigReport.Res) and msg.seq not in self._msg_futures:
          seq = self._last_dev_config_report_seq
        fut = self._msg_futures.pop(seq)
        fut.set_result(msg)
      else:
        print(f'Received request {type(msg).__qualname__} seq {msg.seq}')
        asyncio.create_task(self.on_message(msg))

  async def on_message(self, msg: ReqMessage):
    return False
