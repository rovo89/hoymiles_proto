from . import ReqMessage, ResMessage, proto

class Cloud:

  class DevData:
    Dtu = proto.CloudDevData_pb2.Dtu
    Feature = proto.CloudDevData_pb2.Feature
    FeatureKey = proto.CloudDevData_pb2.FeatureKey
    Inverter = proto.CloudDevData_pb2.Inverter
    Meter = proto.CloudDevData_pb2.Meter
    Repeater = proto.CloudDevData_pb2.Repeater
    class Req(proto.CloudDevData_pb2.DevDataFromDtu, ReqMessage): ...
    class Res(proto.CloudDevData_pb2.DevDataToDtu, ResMessage): ...

  class Heartbeat:
    class Req(proto.Heartbeat_pb2.HeartbeatFromDtu, ReqMessage): ...
    class Res(proto.Heartbeat_pb2.HeartbeatToDtu, ResMessage): ...

  class RealtimeData:
    Meter = proto.RealtimeData_pb2.Meter
    Panel = proto.RealtimeData_pb2.Panel
    Repeater = proto.RealtimeData_pb2.Repeater
    class Req(proto.RealtimeData_pb2.RealtimeDataFromDtu, ReqMessage): ...
    class Res(proto.RealtimeData_pb2.RealtimeDataToDtu, ResMessage): ...

  class HistoryData:
    Meter = proto.RealtimeData_pb2.Meter
    Panel = proto.RealtimeData_pb2.Panel
    Repeater = proto.RealtimeData_pb2.Repeater
    class Req(proto.RealtimeData_pb2.RealtimeDataFromDtu, ReqMessage): ...
    class Res(proto.RealtimeData_pb2.RealtimeDataToDtu, ResMessage): ...

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
    class Req(proto.Command_pb2.CommandStatusFromDtu, ReqMessage): ...
    class Res(proto.Command_pb2.CommandStatusToDtu, ResMessage): ...

  class DevConfigFetch:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(proto.DevConfig_pb2.DevConfigFetchFromDtu, ReqMessage): ...
    class Res(proto.DevConfig_pb2.DevConfigFetchToDtu, ResMessage): ...

  class DevConfigPut:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(proto.DevConfig_pb2.DevConfigPutToDtu, ReqMessage): ...
    class Res(proto.DevConfig_pb2.DevConfigPutFromDtu, ResMessage): ...

  class Wave:
    Alarm = proto.Alarms_pb2.Alarm
    class Req(proto.Alarms_pb2.WaveFromDtu, ReqMessage): ...
    class Res(proto.Alarms_pb2.WaveToDtu, ResMessage): ...

  class Alarms:
    Alarm = proto.Alarms_pb2.Alarm
    class Req(proto.Alarms_pb2.AlarmsFromDtu, ReqMessage): ...
    class Res(proto.Alarms_pb2.AlarmsToDtu, ResMessage): ...

  class RealtimeDataNew:
    Grid = proto.RealtimeDataNew_pb2.Grid
    Meter = proto.RealtimeDataNew_pb2.Meter
    Panel = proto.RealtimeDataNew_pb2.Panel
    Repeater = proto.RealtimeDataNew_pb2.Repeater
    Rsd = proto.RealtimeDataNew_pb2.Rsd
    ThreePhaseGrid = proto.RealtimeDataNew_pb2.ThreePhaseGrid
    class Req(proto.RealtimeDataNew_pb2.RealtimeDataNewFromDtu, ReqMessage): ...
    class Res(proto.RealtimeDataNew_pb2.RealtimeDataNewToDtu, ResMessage): ...

  class HistoryDataNew:
    Grid = proto.RealtimeDataNew_pb2.Grid
    Meter = proto.RealtimeDataNew_pb2.Meter
    Panel = proto.RealtimeDataNew_pb2.Panel
    Repeater = proto.RealtimeDataNew_pb2.Repeater
    Rsd = proto.RealtimeDataNew_pb2.Rsd
    ThreePhaseGrid = proto.RealtimeDataNew_pb2.ThreePhaseGrid
    class Req(proto.RealtimeDataNew_pb2.RealtimeDataNewFromDtu, ReqMessage): ...
    class Res(proto.RealtimeDataNew_pb2.RealtimeDataNewToDtu, ResMessage): ...

  class DevConfigReport:
    RuleType = proto.DevConfig_pb2.RuleType
    class Req(proto.DevConfig_pb2.DevConfigReportFromDtu, ReqMessage): ...
    class Res(proto.DevConfig_pb2.DevConfigReportToDtu, ResMessage): ...
