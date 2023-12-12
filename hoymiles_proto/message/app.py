from . import ReqMessage, ResMessage, proto

class App:

  class DevData:
    Dtu = proto.AppDevData_pb2.Dtu
    Feature = proto.AppDevData_pb2.Feature
    FeatureKey = proto.AppDevData_pb2.FeatureKey
    Inverter = proto.AppDevData_pb2.Inverter
    Meter = proto.AppDevData_pb2.Meter
    Repeater = proto.AppDevData_pb2.Repeater
    class Req(ReqMessage):
      msg_type = 0xA301
      _dto_class = proto.AppDevData_pb2.DevDataToDtu
    class Res(ResMessage):
      msg_type = 0xA201
      _dto_class = proto.AppDevData_pb2.DevDataFromDtu

  class Heartbeat:
    class Req(ReqMessage):
      msg_type = 0xA302
      _dto_class = proto.Heartbeat_pb2.HeartbeatToDtu
    class Res(ResMessage):
      msg_type = 0xA202
      _dto_class = proto.Heartbeat_pb2.HeartbeatFromDtu

  class RealtimeData:
    Meter = proto.RealtimeData_pb2.Meter
    Panel = proto.RealtimeData_pb2.Panel
    Repeater = proto.RealtimeData_pb2.Repeater
    class Req(ReqMessage):
      msg_type = 0xA303
      _dto_class = proto.RealtimeData_pb2.RealtimeDataToDtu
    class Res(ResMessage):
      msg_type = 0xA203
      _dto_class = proto.RealtimeData_pb2.RealtimeDataFromDtu

  class Alarms:
    Alarm = proto.Alarms_pb2.Alarm
    class Req(ReqMessage):
      msg_type = 0xA304
      _dto_class = proto.Alarms_pb2.AlarmsToDtu
    class Res(ResMessage):
      msg_type = 0xA204
      _dto_class = proto.Alarms_pb2.AlarmsFromDtu

  class Command:
    CommandAction = proto.Command_pb2.CommandAction
    DeviceKind = proto.Command_pb2.DeviceKind
    ESErrorStatus = proto.Command_pb2.ESErrorStatus
    ESOperatingStatus = proto.Command_pb2.ESOperatingStatus
    ESSuccessStatus = proto.Command_pb2.ESSuccessStatus
    MIErrorStatus = proto.Command_pb2.MIErrorStatus
    MIOperatingStatus = proto.Command_pb2.MIOperatingStatus
    class Req(ReqMessage):
      msg_type = 0xA305
      _dto_class = proto.Command_pb2.CommandToDtu
    class Res(ResMessage):
      msg_type = 0xA205
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
      msg_type = 0xA306
      _dto_class = proto.Command_pb2.CommandStatusToDtu
    class Res(ResMessage):
      msg_type = 0xA206
      _dto_class = proto.Command_pb2.CommandStatusFromDtu

  class DevConfigFetch:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(ReqMessage):
      msg_type = 0xA307
      _dto_class = proto.DevConfig_pb2.DevConfigFetchToDtu
    class Res(ResMessage):
      msg_type = 0xA207
      _dto_class = proto.DevConfig_pb2.DevConfigFetchFromDtu

  class DevConfigPut:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(ReqMessage):
      msg_type = 0xA308
      _dto_class = proto.DevConfig_pb2.DevConfigPutToDtu
    class Res(ResMessage):
      msg_type = 0xA208
      _dto_class = proto.DevConfig_pb2.DevConfigPutFromDtu

  class GetConfig:
    class Req(ReqMessage):
      msg_type = 0xA309
      _dto_class = proto.Config_pb2.GetConfigToDtu
    class Res(ResMessage):
      msg_type = 0xA209
      _dto_class = proto.Config_pb2.GetConfigFromDtu

  class SetConfig:
    class Req(ReqMessage):
      msg_type = 0xA310
      _dto_class = proto.Config_pb2.SetConfigToDtu
    class Res(ResMessage):
      msg_type = 0xA210
      _dto_class = proto.Config_pb2.SetConfigFromDtu

  class RealtimeDataNew:
    Grid = proto.RealtimeDataNew_pb2.Grid
    Meter = proto.RealtimeDataNew_pb2.Meter
    Panel = proto.RealtimeDataNew_pb2.Panel
    Repeater = proto.RealtimeDataNew_pb2.Repeater
    Rsd = proto.RealtimeDataNew_pb2.Rsd
    ThreePhaseGrid = proto.RealtimeDataNew_pb2.ThreePhaseGrid
    class Req(ReqMessage):
      msg_type = 0xA311
      _dto_class = proto.RealtimeDataNew_pb2.RealtimeDataNewToDtu
    class Res(ResMessage):
      msg_type = 0xA211
      _dto_class = proto.RealtimeDataNew_pb2.RealtimeDataNewFromDtu

  class AutoSearch:
    class Req(ReqMessage):
      msg_type = 0xA213
      _dto_class = proto.AutoSearch_pb2.AutoSearchFromDtu
    class Res(ResMessage):
      msg_type = 0xA313
      _dto_class = proto.AutoSearch_pb2.AutoSearchToDtu

  class NetworkInfo:
    class Req(ReqMessage):
      msg_type = 0xA214
      _dto_class = proto.NetworkInfo_pb2.NetworkInfoFromDtu
    class Res(ResMessage):
      msg_type = 0xA314
      _dto_class = proto.NetworkInfo_pb2.NetworkInfoToDtu
