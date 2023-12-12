#!/usr/bin/env python3
from enum import Enum, auto
import importlib
import re
import sys

base_path = './hoymiles_proto/message/'
sys.path.insert(0, base_path + 'proto')

####################################################################################################

class Direction(Enum):
  FROM_DTU = auto()
  TO_DTU = auto()

sub_msg_pattern = re.compile('^[A-Za-z]+$')
sub_msg_excl_pattern = re.compile('^DESCRIPTOR$|.*FromDtu$|.*ToDtu$|_pb2$|^[A-Z_]+$')

def header():
  global py, pyi, scope
  for file in (py, pyi):
    print('from . import ReqMessage, ResMessage, proto', file=file)
    print(file=file)
    print(f'class {scope}:', file=file)

def msg(base_id, name, pb_mod, direction: Direction, base_msg=None):
  global py, pyi, scope, map

  if base_msg is None:
    base_msg = name
  if direction == Direction.FROM_DTU:
    request_name = base_msg + 'FromDtu'
    reply_name = base_msg + 'ToDtu'
    request_id = base_id
    reply_id = base_id | 0x0100
  else:
    request_name = base_msg + 'ToDtu'
    reply_name = base_msg + 'FromDtu'
    request_id = base_id | 0x0100
    reply_id = base_id

  pb_mod_obj = importlib.import_module(pb_mod)
  sub_msgs = list(filter(lambda x: sub_msg_pattern.match(x) and not sub_msg_excl_pattern.match(x), dir(pb_mod_obj)))

  # Write to .py.
  print('', file=py)
  print(f'  class {name}:', file=py)
  for msg in sub_msgs:
    print(f'    {msg} = proto.{pb_mod}.{msg}', file=py)
  print(f'    class Req(ReqMessage):', file=py)
  print(f'      msg_type = 0x{request_id:X}', file=py)
  print(f'      _dto_class = proto.{pb_mod}.{request_name}', file=py)
  print(f'    class Res(ResMessage):', file=py)
  print(f'      msg_type = 0x{reply_id:X}', file=py)
  print(f'      _dto_class = proto.{pb_mod}.{reply_name}', file=py)

  # Write to .pyi.
  print('', file=pyi)
  print(f'  class {name}:', file=pyi)
  for msg in sub_msgs:
    print(f'    {msg} = proto.{pb_mod}.{msg}', file=pyi)
  print(f'    class Req(proto.{pb_mod}.{request_name}, ReqMessage): ...', file=pyi)
  print(f'    class Res(proto.{pb_mod}.{reply_name}, ResMessage): ...', file=pyi)

  # Write to map.py.
  print(f'  0x{request_id:X}: {scope}.{name}.Req, 0x{reply_id:X}: {scope}.{name}.Res,', file=map)

####################################################################################################

pb_mods = set()
with open(base_path + 'map.py', 'w') as map:
  print('from .cloud import Cloud', file=map)
  print('from .app import App', file=map)
  print('', file=map)
  print('msg_type_to_cls = {', file=map)

  scope = 'Cloud'
  with open(base_path + scope.lower() + '.py', 'w') as py, open(base_path + scope.lower() + '.pyi', 'w') as pyi:
    header()
    msg(0x2201, 'DevData', 'CloudDevData_pb2', Direction.FROM_DTU)
    msg(0x2202, 'Heartbeat', 'Heartbeat_pb2', Direction.FROM_DTU)
    msg(0x2203, 'RealtimeData', 'RealtimeData_pb2', Direction.FROM_DTU)
    msg(0x2204, 'HistoryData', 'RealtimeData_pb2', Direction.FROM_DTU, 'RealtimeData')
    msg(0x2205, 'Command', 'Command_pb2', Direction.TO_DTU)
    msg(0x2206, 'CommandStatus', 'Command_pb2', Direction.FROM_DTU)
    msg(0x2207, 'DevConfigFetch', 'DevConfig_pb2', Direction.TO_DTU)
    msg(0x2208, 'DevConfigPut', 'DevConfig_pb2', Direction.TO_DTU)
    msg(0x220A, 'Wave', 'Alarms_pb2', Direction.FROM_DTU)
    msg(0x220B, 'Alarms', 'Alarms_pb2', Direction.FROM_DTU)
    msg(0x220C, 'RealtimeDataNew', 'RealtimeDataNew_pb2', Direction.FROM_DTU)
    msg(0x220D, 'HistoryDataNew', 'RealtimeDataNew_pb2', Direction.FROM_DTU, 'RealtimeDataNew')
    msg(0x220E, 'DevConfigReport', 'DevConfig_pb2', Direction.FROM_DTU)

  scope = 'App'
  with open(base_path + scope.lower() + '.py', 'w') as py, open(base_path + scope.lower() + '.pyi', 'w') as pyi:
    header()
    msg(0xA201, 'DevData', 'AppDevData_pb2', Direction.TO_DTU)
    msg(0xA202, 'Heartbeat', 'Heartbeat_pb2', Direction.TO_DTU)
    msg(0xA203, 'RealtimeData', 'RealtimeData_pb2', Direction.TO_DTU)
    msg(0xA204, 'Alarms', 'Alarms_pb2', Direction.TO_DTU)
    msg(0xA205, 'Command', 'Command_pb2', Direction.TO_DTU)
    msg(0xA206, 'CommandStatus', 'Command_pb2', Direction.TO_DTU)
    msg(0xA207, 'DevConfigFetch', 'DevConfig_pb2', Direction.TO_DTU)
    msg(0xA208, 'DevConfigPut', 'DevConfig_pb2', Direction.TO_DTU)
    msg(0xA209, 'GetConfig', 'Config_pb2', Direction.TO_DTU)
    msg(0xA210, 'SetConfig', 'Config_pb2', Direction.TO_DTU)
    msg(0xA211, 'RealtimeDataNew', 'RealtimeDataNew_pb2', Direction.TO_DTU)
    # msg(0xA212, 'GPST', 'GPST_pb2', Direction.FROM_DTU)
    msg(0xA213, 'AutoSearch', 'AutoSearch_pb2', Direction.FROM_DTU)
    msg(0xA214, 'NetworkInfo', 'NetworkInfo_pb2', Direction.FROM_DTU)
    # msg(0xA215, 'HistPower', 'HistPower_pb2', Direction.FROM_DTU)
    # msg(0xA215, 'HistED', 'HistED_pb2', Direction.FROM_DTU)
    # FIXME

  print('}', file=map)
