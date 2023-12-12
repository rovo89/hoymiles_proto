from . import ReqMessage, ResMessage, proto

class Cloud:

  class DevData:
    Dtu = proto.CloudDevData_pb2.Dtu
    Feature = proto.CloudDevData_pb2.Feature
    FeatureKey = proto.CloudDevData_pb2.FeatureKey
    Inverter = proto.CloudDevData_pb2.Inverter
    Meter = proto.CloudDevData_pb2.Meter
    Repeater = proto.CloudDevData_pb2.Repeater
    class Req(ReqMessage):
      msg_type = 0x2201
      _dto_class = proto.CloudDevData_pb2.DevDataFromDtu
    class Res(ResMessage):
      msg_type = 0x2301
      _dto_class = proto.CloudDevData_pb2.DevDataToDtu

  class Heartbeat:
    class Req(ReqMessage):
      msg_type = 0x2202
      _dto_class = proto.Heartbeat_pb2.HeartbeatFromDtu
    class Res(ResMessage):
      msg_type = 0x2302
      _dto_class = proto.Heartbeat_pb2.HeartbeatToDtu

  class RealtimeData:
    Meter = proto.RealtimeData_pb2.Meter
    Panel = proto.RealtimeData_pb2.Panel
    Repeater = proto.RealtimeData_pb2.Repeater
    class Req(ReqMessage):
      msg_type = 0x2203
      _dto_class = proto.RealtimeData_pb2.RealtimeDataFromDtu
    class Res(ResMessage):
      msg_type = 0x2303
      _dto_class = proto.RealtimeData_pb2.RealtimeDataToDtu

  class HistoryData:
    Meter = proto.RealtimeData_pb2.Meter
    Panel = proto.RealtimeData_pb2.Panel
    Repeater = proto.RealtimeData_pb2.Repeater
    class Req(ReqMessage):
      msg_type = 0x2204
      _dto_class = proto.RealtimeData_pb2.RealtimeDataFromDtu
    class Res(ResMessage):
      msg_type = 0x2304
      _dto_class = proto.RealtimeData_pb2.RealtimeDataToDtu

  class Command:
    CommandAction = proto.Command_pb2.CommandAction
    DeviceKind = proto.Command_pb2.DeviceKind
    ESErrorStatus = proto.Command_pb2.ESErrorStatus
    ESOperatingStatus = proto.Command_pb2.ESOperatingStatus
    ESSuccessStatus = proto.Command_pb2.ESSuccessStatus
    MIErrorStatus = proto.Command_pb2.MIErrorStatus
    MIOperatingStatus = proto.Command_pb2.MIOperatingStatus
    class Req(ReqMessage):
      msg_type = 0x2305
      _dto_class = proto.Command_pb2.CommandToDtu
    class Res(ResMessage):
      msg_type = 0x2205
      _dto_class = proto.Command_pb2.CommandFromDtu

  class CommandStatus:
    CommandAction = proto.Command_pb2.CommandAction
    DeviceKind = proto.Command_pb2.DeviceKind
    ESErrorStatus = proto.Command_pb2.ESErrorStatus
    ESOperatingStatus = proto.Command_pb2.ESOperatingStatus
    ESSuccessStatus = proto.Command_pb2.ESSuccessStatus
    MIErrorStatus = proto.Command_pb2.MIErrorStatus
    MIOperatingStatus = proto.Command_pb2.MIOperatingStatus
    class Req(ReqMessage):
      msg_type = 0x2206
      _dto_class = proto.Command_pb2.CommandStatusFromDtu
    class Res(ResMessage):
      msg_type = 0x2306
      _dto_class = proto.Command_pb2.CommandStatusToDtu

  class DevConfigFetch:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(ReqMessage):
      msg_type = 0x2207
      _dto_class = proto.DevConfig_pb2.DevConfigFetchFromDtu
    class Res(ResMessage):
      msg_type = 0x2307
      _dto_class = proto.DevConfig_pb2.DevConfigFetchToDtu

  class DevConfigPut:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(ReqMessage):
      msg_type = 0x2308
      _dto_class = proto.DevConfig_pb2.DevConfigPutToDtu
    class Res(ResMessage):
      msg_type = 0x2208
      _dto_class = proto.DevConfig_pb2.DevConfigPutFromDtu

  class Wave:
    Alarm = proto.Alarms_pb2.Alarm
    class Req(ReqMessage):
      msg_type = 0x220A
      _dto_class = proto.Alarms_pb2.WaveFromDtu
    class Res(ResMessage):
      msg_type = 0x230A
      _dto_class = proto.Alarms_pb2.WaveToDtu

  class Alarms:
    Alarm = proto.Alarms_pb2.Alarm
    class Req(ReqMessage):
      msg_type = 0x220B
      _dto_class = proto.Alarms_pb2.AlarmsFromDtu
    class Res(ResMessage):
      msg_type = 0x230B
      _dto_class = proto.Alarms_pb2.AlarmsToDtu

  class RealtimeDataNew:
    Grid = proto.RealtimeDataNew_pb2.Grid
    Meter = proto.RealtimeDataNew_pb2.Meter
    Panel = proto.RealtimeDataNew_pb2.Panel
    Repeater = proto.RealtimeDataNew_pb2.Repeater
    Rsd = proto.RealtimeDataNew_pb2.Rsd
    ThreePhaseGrid = proto.RealtimeDataNew_pb2.ThreePhaseGrid
    class Req(ReqMessage):
      msg_type = 0x220C
      _dto_class = proto.RealtimeDataNew_pb2.RealtimeDataNewFromDtu
    class Res(ResMessage):
      msg_type = 0x230C
      _dto_class = proto.RealtimeDataNew_pb2.RealtimeDataNewToDtu

  class HistoryDataNew:
    Grid = proto.RealtimeDataNew_pb2.Grid
    Meter = proto.RealtimeDataNew_pb2.Meter
    Panel = proto.RealtimeDataNew_pb2.Panel
    Repeater = proto.RealtimeDataNew_pb2.Repeater
    Rsd = proto.RealtimeDataNew_pb2.Rsd
    ThreePhaseGrid = proto.RealtimeDataNew_pb2.ThreePhaseGrid
    class Req(ReqMessage):
      msg_type = 0x220D
      _dto_class = proto.RealtimeDataNew_pb2.RealtimeDataNewFromDtu
    class Res(ResMessage):
      msg_type = 0x230D
      _dto_class = proto.RealtimeDataNew_pb2.RealtimeDataNewToDtu

  class DevConfigReport:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(ReqMessage):
      msg_type = 0x220E
      _dto_class = proto.DevConfig_pb2.DevConfigReportFromDtu
    class Res(ResMessage):
      msg_type = 0x230E
      _dto_class = proto.DevConfig_pb2.DevConfigReportToDtu
