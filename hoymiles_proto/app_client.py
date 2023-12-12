import asyncio
from typing import Iterable
from .client import Client
from .message import int_time, ymd_hms
from .message.app import App
from .wrappers import Alarm, GridProfile
from .sn import SN

CmdAction = App.Command.CommandAction
DevKind = App.Command.DeviceKind

class CommandError(Exception):
  pass

class AppClient(Client):
  def __init__(self, host: str, port: int = 10081, loop: asyncio.AbstractEventLoop = None) -> None:
    super().__init__(host, port, loop)
    self._last_command_action = None
    self._last_command_sns = []

  async def execute_command(self, action: int, data: str = None, dev_kind: int = 0, mi_sns: Iterable[SN] = []) -> None:
    tid = int_time()
    cmd_res: App.Command.Res = await self.send_request(App.Command.Req(
      time=tid,
      tid=tid,
      package_count=1,
      action=action,
      data=data,
      dev_kind=dev_kind,
      mi_to_sn=map(lambda sn: sn.int, mi_sns)
    ))
    if cmd_res.err_code:
      raise CommandError('Unknown command action ' + str(action))
    await asyncio.sleep(0.2)
    while True:
      status_res: App.CommandStatus.Res = await self.send_request(App.CommandStatus.Req(time=int_time(), tid=tid, package_idx=1, action=action))
      if status_res.mi_operating_status:
        await asyncio.sleep(1)
      elif status_res.mi_sns_failed:
        raise CommandError('Command failed')
      else:
        # FIXME: Remember other command details.
        self._last_command_action = action
        return

  async def _ensure_command(self, action: int, mi_sns: Iterable[SN] = []):
    # FIXME: Check other command details.
    if self._last_command_action != action:
      return await self.execute_command(action=action, mi_sns=mi_sns)

  async def grid_profile_fetch(self, mi_sn: SN) -> GridProfile:
    await self.execute_command(action=CmdAction.ACTION_GRID_FILE_READ, dev_kind=DevKind.DEV_DTU, mi_sns=[mi_sn])
    res: App.DevConfigFetch.Res = await self.send_request(App.DevConfigFetch.Req(time=int_time(), tid=int_time(), dev_sn=mi_sn.str, rule_type=1))
    # TODO: Check CRC?
    return GridProfile(res.data)

  async def mi_restart(self, mi_sn: SN):
    await self.execute_command(action=CmdAction.ACTION_MI_REBOOT, mi_sns=[mi_sn])

  async def mi_shutdown(self, mi_sn: SN):
    await self.execute_command(action=CmdAction.ACTION_MI_SHUTDOWN, mi_sns=[mi_sn])

  async def mi_start(self, mi_sn: SN):
    await self.execute_command(action=CmdAction.ACTION_MI_START, mi_sns=[mi_sn])

  async def poll_all_mi(self):
    await self.execute_command(action=CmdAction.ACTION_POLL_ALL)

  async def device_data(self) -> App.DevData.Res:
    return await self.send_request(App.DevData.Req(offset=3600, time=int_time(), ymd_hms=ymd_hms()))

  async def realtime_data(self) -> App.RealtimeDataNew.Res:
    await self._ensure_command(action=CmdAction.ACTION_POLL_ALL)
    return await self.send_request(App.RealtimeDataNew.Req(offset=3600, time=int_time(), ymd_hms=ymd_hms()))

  async def network_info(self) -> App.NetworkInfo.Res:
    return await self.send_request(App.RealtimeDataNew.Req(offset=3600, time=int_time(), ymd_hms=ymd_hms()))

  async def alarms(self, mi_sn: SN):
    # await self._ensure_command(action=CmdAction.ACTION_ALARM_ALL)
    await self._ensure_command(action=CmdAction.ACTION_ALARM_SINGLE, mi_sns=[mi_sn])
    res: App.Alarms.Res = await self.send_request(App.Alarms.Req(offset=3600, time=int_time(), ymd_hms=ymd_hms(), package_idx=0))
    # res.alarms.append(App.Alarms.Alarm(sn=22069993801606, code=8409, num=46, start_time=1700145543, data1=683, data2=600))
    # res.alarms.append(App.Alarms.Alarm(sn=22069993801606, code=8316, num=51, start_time=1700148478))
    # res.alarms.append(App.Alarms.Alarm(sn=22069993801606, code=28796, num=52, start_time=1700148478, end_time=1700148850))
    return list(map(lambda data: Alarm(data), res.alarms))
