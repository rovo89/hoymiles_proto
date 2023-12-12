import crcmod
from struct import pack, unpack
from time import time as _time
from datetime import datetime

hmcrc = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)

def build_packet_raw(msg_type, seq, encoded_dto):
  return b'HM' + pack('>HHHH', msg_type, seq, hmcrc(encoded_dto), len(encoded_dto) + 10) + encoded_dto

def parse_packet_raw(packet):
  if packet[:2] != b'HM':
    raise Exception('Packet does not start with "HM"')
  if len(packet) < 10:
    raise Exception('Packet is too short')
  (msg_type, seq, crc, length) = unpack('>HHHH', packet[2:10])
  if len(packet) != length:
    raise Exception('Packet length does not match embedded length field')
  encoded_dto = packet[10:]
  if crc != hmcrc(encoded_dto):
    raise Exception('Packet checksum is wrong')
  return (msg_type, seq, encoded_dto)

def msg_from_packet(packet):
  (msg_type, seq, dto_str) = parse_packet_raw(packet)
  msg = msg_type_to_cls[msg_type](seq=seq)
  msg.ParseFromString(dto_str)
  return msg

####################################################################################################

def int_time():
  return int(_time())

def ymd_hms():
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

####################################################################################################

class BaseMessage:
  __slots__ = ("seq", "dto")

  def __init__(self, seq=None, *args, **kwargs):
    self.seq = seq
    self.dto = self._dto_class(*args, **kwargs)

  def __repr__(self):
    return type(self).__qualname__ + ' (seq ' + str(self.seq) + '):\n' + str(self.dto)

  def __getattr__(self, name):
    return getattr(self.dto, name)

  def __setattr__(self, name, value):
    if name in self.__slots__:
      super().__setattr__(name, value)
    else:
      return setattr(self.dto, name, value)

  def ToPacket(self):
    return build_packet_raw(self.msg_type, self.seq, self.SerializeToString())

class ReqMessage(BaseMessage):
  pass

class ResMessage(BaseMessage):
  pass

####################################################################################################

from .cloud import Cloud
from .app import App
from .map import msg_type_to_cls
