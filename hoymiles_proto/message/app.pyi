from . import ReqMessage, ResMessage, proto

class App:

  class DevData:
    Dtu = proto.AppDevData_pb2.Dtu
    Feature = proto.AppDevData_pb2.Feature
    FeatureKey = proto.AppDevData_pb2.FeatureKey
    Inverter = proto.AppDevData_pb2.Inverter
    Meter = proto.AppDevData_pb2.Meter
    Repeater = proto.AppDevData_pb2.Repeater
    class Req(proto.AppDevData_pb2.DevDataToDtu, ReqMessage): ...
    class Res(proto.AppDevData_pb2.DevDataFromDtu, ResMessage): ...

  class Heartbeat:
    class Req(proto.Heartbeat_pb2.HeartbeatToDtu, ReqMessage): ...
    class Res(proto.Heartbeat_pb2.HeartbeatFromDtu, ResMessage): ...

  class RealtimeData:
    Meter = proto.RealtimeData_pb2.Meter
    Panel = proto.RealtimeData_pb2.Panel
    Repeater = proto.RealtimeData_pb2.Repeater
    class Req(proto.RealtimeData_pb2.RealtimeDataToDtu, ReqMessage): ...
    class Res(proto.RealtimeData_pb2.RealtimeDataFromDtu, ResMessage): ...

  class Alarms:
    Alarm = proto.Alarms_pb2.Alarm
    class Req(proto.Alarms_pb2.AlarmsToDtu, ReqMessage): ...
    class Res(proto.Alarms_pb2.AlarmsFromDtu, ResMessage): ...

  class Command:
    CommandAction = proto.Command_pb2.CommandAction
    DeviceKind = proto.Command_pb2.DeviceKind
    ESErrorStatus = proto.Command_pb2.ESErrorStatus
    ESOperatingStatus = proto.Command_pb2.ESOperatingStatus
    ESSuccessStatus = proto.Command_pb2.ESSuccessStatus
    MIErrorStatus = proto.Command_pb2.MIErrorStatus
    MIOperatingStatus = proto.Command_pb2.MIOperatingStatus
    class Req(proto.Command_pb2.CommandToDtu, ReqMessage): ...
    class Res(proto.Command_pb2.CommandFromDtu, ResMessage): ...

  class CommandStatus:
    CommandAction = proto.Command_pb2.CommandAction
    DeviceKind = proto.Command_pb2.DeviceKind
    ESErrorStatus = proto.Command_pb2.ESErrorStatus
    ESOperatingStatus = proto.Command_pb2.ESOperatingStatus
    ESSuccessStatus = proto.Command_pb2.ESSuccessStatus
    MIErrorStatus = proto.Command_pb2.MIErrorStatus
    MIOperatingStatus = proto.Command_pb2.MIOperatingStatus
    class Req(proto.Command_pb2.CommandStatusToDtu, ReqMessage): ...
    class Res(proto.Command_pb2.CommandStatusFromDtu, ResMessage): ...

  class DevConfigFetch:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(proto.DevConfig_pb2.DevConfigFetchToDtu, ReqMessage): ...
    class Res(proto.DevConfig_pb2.DevConfigFetchFromDtu, ResMessage): ...

  class DevConfigPut:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(proto.DevConfig_pb2.DevConfigPutToDtu, ReqMessage): ...
    class Res(proto.DevConfig_pb2.DevConfigPutFromDtu, ResMessage): ...

  class GetConfig:
    class Req(proto.Config_pb2.GetConfigToDtu, ReqMessage): ...
    class Res(proto.Config_pb2.GetConfigFromDtu, ResMessage): ...

  class SetConfig:
    class Req(proto.Config_pb2.SetConfigToDtu, ReqMessage): ...
    class Res(proto.Config_pb2.SetConfigFromDtu, ResMessage): ...

  class RealtimeDataNew:
    Grid = proto.RealtimeDataNew_pb2.Grid
    Meter = proto.RealtimeDataNew_pb2.Meter
    Panel = proto.RealtimeDataNew_pb2.Panel
    Repeater = proto.RealtimeDataNew_pb2.Repeater
    Rsd = proto.RealtimeDataNew_pb2.Rsd
    ThreePhaseGrid = proto.RealtimeDataNew_pb2.ThreePhaseGrid
    class Req(proto.RealtimeDataNew_pb2.RealtimeDataNewToDtu, ReqMessage): ...
    class Res(proto.RealtimeDataNew_pb2.RealtimeDataNewFromDtu, ResMessage): ...

  class AutoSearch:
    class Req(proto.AutoSearch_pb2.AutoSearchFromDtu, ReqMessage): ...
    class Res(proto.AutoSearch_pb2.AutoSearchToDtu, ResMessage): ...

  class NetworkInfo:
    class Req(proto.NetworkInfo_pb2.NetworkInfoFromDtu, ReqMessage): ...
    class Res(proto.NetworkInfo_pb2.NetworkInfoToDtu, ResMessage): ...
