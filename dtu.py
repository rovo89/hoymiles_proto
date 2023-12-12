#!/usr/bin/env python3
import asyncio
import time
from hoymiles_proto import SN, DtuClient, ReqMessage, Cloud, int_time, hmcrc

DTU_SN = SN('4143xxxxxxxx')
MI_SN  = SN('1412xxxxxxxx')
raise Exception('Please adjust the serial numbers and then remove this line!')

class MyDtu(DtuClient):
  async def on_connected(self) -> None:
    await super().on_connected()
    await self.send_startup()

  async def send_startup(self):
    await self.send_request(Cloud.DevData.Req(dtu_sn=DTU_SN.str, time=int_time(), inverter_count=1, panel_count=2, package_count=1,
      dtu=Cloud.DevData.Dtu(sw_version=0x108, hw_version=0x100, step_time=15, access_model=1, wifi_version='2.1.21_hm'),
      inverters=[Cloud.DevData.Inverter(sn=MI_SN.int, sw_version=10008, hw_part_num=0x10214201, hw_version=0x100, grid_profile_version=0x300, grid_profile_code=0x2001)],
      features=[Cloud.DevData.Feature(key=Cloud.DevData.FeatureKey.POWER_LIMIT, value='1,A:1000,B:0,C:0\r')]
    ))

    await self.send_request(Cloud.RealtimeDataNew.Req(sn=DTU_SN.str, time=int_time(), ap=1, ver=1,
      grids=[Cloud.RealtimeDataNew.Grid(sn=MI_SN.int, ver=1, v=2300, freq=5000, p=2800, q=1, i=100, pf=999, temp=189, wnum=11, crc=28864, link=1, mi_signal=0x9D001F)],
      panels=[
        Cloud.RealtimeDataNew.Panel(sn=MI_SN.int, pi=1, v=370, i=30, p=150, et=2949, ed=83, code=0x3090000),
        Cloud.RealtimeDataNew.Panel(sn=MI_SN.int, pi=2, v=370, i=30, p=150, et=2949, ed=82, code=0x3000000),
      ]
    ))

  async def on_message(self, msg: ReqMessage):
    if await super().on_message(msg): return True
    print('incoming: ' + str(msg))

    if isinstance(msg, Cloud.Command.Req):
      self.send_response(msg, Cloud.Command.Res(dtu_sn=self.sn.str, time=int_time(), action=msg.action, tid=msg.tid))
      await self.send_request(Cloud.CommandStatus.Req(dtu_sn=self.sn.str, time=int_time(), action=msg.action, package_count=1, tid=msg.tid, mi_sns_success=[MI_SN.int]))
      if msg.action == Cloud.CommandStatus.CommandAction.ACTION_GRID_FILE_READ:
        with open('grid_profile.bin', 'rb') as f:
          data = f.read()
        self.send_request(Cloud.DevConfigReport.Req(time=int_time(), tid=msg.tid, data=data, crc=hmcrc(data), dtu_sn=self.sn.str, dev_sn=MI_SN.str, package_count=1, rule_type=Cloud.DevConfigFetch.RuleType.GRID_PROFILE))

    elif isinstance(msg, Cloud.DevConfigPut.Req):
      if msg.rule_type == Cloud.DevConfigPut.RuleType.GRID_PROFILE:
        with open('grid_profile.bin', 'wb') as f:
          f.write(msg.data)
      self.send_response(msg, Cloud.DevConfigPut.Res(time=int_time(), tid=msg.tid, dtu_sn=msg.dtu_sn, dev_sn=msg.dev_sn))
      await self.send_request(Cloud.CommandStatus.Req(dtu_sn=msg.dtu_sn, time=int_time(), action=Cloud.CommandStatus.CommandAction.ACTION_SET_GRID_FILE, tid=msg.tid, package_count=1, mi_sns_success=[SN(msg.dev_sn).int]))

  async def on_disconnected(self, exc: Exception):
    await super().on_disconnected(exc)
    print('disconnected')
    loop.stop()

  async def on_cloud_heartbeat_res(self, msg: Cloud.Heartbeat.Res):
    print(msg)

async def main():
  # dtu = MyDtu(loop=loop, host='127.0.0.1', sn=DTU_SN)
  dtu = MyDtu(host='dataeu.hoymiles.com', sn=DTU_SN)
  await dtu.connect()

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
