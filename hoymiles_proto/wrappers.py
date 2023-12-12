from datetime import datetime

from .message.proto.Alarms_pb2 import Alarm as _AlarmData
from .sn import SN

class Alarm:
  def __init__(self, data: _AlarmData) -> None:
    self.sn = SN(data.sn)
    # Bits (from right):
    # 15/14 = ???
    # 13 = start on afternoon
    # 12 = start on afternoon
    self.code = data.code
    self.num = data.num
    self.start_time = datetime.fromtimestamp(data.start_time) if data.start_time else None
    self.end_time = datetime.fromtimestamp(data.end_time) if data.end_time else None
    self.data1 = data.data1
    self.data2 = data.data2

  def __repr__(self) -> str:
    return str(self.__dict__)
    # return str(self._data)

class GridProfile:
  def __init__(self, raw: bytes) -> None:
    self.raw = raw
