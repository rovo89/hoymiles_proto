import asyncio

from .connection import Connection

class Client(Connection):
  def __init__(self, host: str, port: int = 10081, loop: asyncio.AbstractEventLoop = None) -> None:
    super().__init__()
    self.host = host
    self.port = port
    self.loop = loop if loop is not None else asyncio.get_running_loop()

  async def connect(self):
    await self.disconnect()
    await self.loop.create_connection(lambda: self, self.host, self.port)
