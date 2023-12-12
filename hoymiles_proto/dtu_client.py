import asyncio

from .sn import SN
from .client import Client
from .message import ReqMessage, int_time
from .message.cloud import Cloud
from .message.app import App

class DtuClient(Client):
  def __init__(self, sn: SN, **kwargs) -> None:
    super().__init__(**kwargs)
    self.sn = sn

  async def on_connected(self) -> None:
    await super().on_connected()
    await self.send_cloud_heartbeat()
    self._heartbeat_task = self.loop.create_task(self.cloud_heartbeat_task())

  async def on_disconnected(self, exc: Exception) -> None:
    await super().on_disconnected(exc)
    self._heartbeat_task.cancel()

  async def on_message(self, msg: ReqMessage):
    if await super().on_message(msg): return True
    if isinstance(msg, App.Heartbeat.Req):
      self.send_response(msg, App.Heartbeat.Res(offset=3600, time=int_time(), csq=-60, dtu_sn=self.sn.str))
      return True

  async def send_cloud_heartbeat(self):
    res: Cloud.Heartbeat.Res = await self.send_request(Cloud.Heartbeat.Req(offset=3600, time=int_time(), csq=-60, dtu_sn=self.sn.str))
    await self.on_cloud_heartbeat_res(res)

  async def on_cloud_heartbeat_res(self, msg: Cloud.Heartbeat.Res):
    pass

  async def cloud_heartbeat_task(self):
    while True:
      await asyncio.sleep(60)
      await self.send_cloud_heartbeat()
