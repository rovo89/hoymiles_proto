import asyncio

from .connection import Connection
from .message import ReqMessage, int_time, ymd_hms
from .message.cloud import Cloud

class ServerConnection(Connection):
  def __init__(self, server: 'Server'):
    super().__init__()
    self.server = server
    self.sn = None

  async def on_connected(self):
    await super().on_connected()
    # TODO: Add idle timeout.
    await self.server.on_connected(self)

  async def on_disconnected(self, exc: Exception):
    await super().on_disconnected(exc)
    await self.server.on_disconnected(self, exc)

  async def on_message(self, msg: ReqMessage):
    if await super().on_message(msg): return True
    return await self.server.on_message(self, msg)


class Server:
  def __init__(self, loop: asyncio.AbstractEventLoop, port=10081) -> None:
    self.loop = loop
    self.port = port
    self.connections_by_sn = {}

  async def listen(self):
    server = await self.loop.create_server(lambda: ServerConnection(self), port=self.port)
    # FIXME
    async with server:
      await server.serve_forever()

  async def on_connected(self, connection: ServerConnection):
    pass

  async def on_disconnected(self, connection: ServerConnection, exc: Exception):
    if connection.sn is not None:
      del self.connections_by_sn[connection.sn]

  async def on_message(self, connection: ServerConnection, msg: ReqMessage):
    if isinstance(msg, Cloud.Heartbeat.Req):
      print('heartbeat from ' + str(connection.peername))
      # TODO: Use something more appropriate than print() and include SN.
      if connection.sn is None:
        if msg.dtu_sn in self.connections_by_sn:
          print('SN is already used by another connection!')
          connection.disconnect()
          return True
        connection.sn = msg.dtu_sn
        self.connections_by_sn[msg.dtu_sn] = connection
      elif msg.dtu_sn != connection.sn:
        print('SN of the connection has changed!')
        connection.disconnect()
        return True
      connection.send_response(msg, Cloud.Heartbeat.Res(offset=3600, time=int_time(), ymd_hms=ymd_hms()))
      return True
