#!/usr/bin/env python3
import asyncio
from hoymiles_proto import SN, AppClient, Cloud, App, ReqMessage, int_time, ymd_hms

async def main():
  app = AppClient('192.168.4.200')
  await app.connect()
  while True:
    print(await app.realtime_data())
    await asyncio.sleep(5)

asyncio.run(main())
