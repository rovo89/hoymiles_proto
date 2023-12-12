#!/usr/bin/env python3
import asyncio
from hoymiles_proto import ReqMessage, Server, ServerConnection

class MyServer(Server):
  async def on_connected(self, connection: ServerConnection) -> None:
    await super().on_connected(connection)
    print("Connect from: " + str(connection.peername))

  async def on_disconnected(self, connection: ServerConnection, exc: Exception) -> None:
    await super().on_disconnected(connection, exc)
    print("Disconnect from: " + str(connection.peername))

  async def on_message(self, connection: ServerConnection, msg: ReqMessage) -> bool:
    if await super().on_message(connection, msg): return True
    print("Message from: " + str(connection.peername))

async def main():
  loop = asyncio.get_running_loop()
  server = MyServer(loop=loop)
  await server.listen()

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
