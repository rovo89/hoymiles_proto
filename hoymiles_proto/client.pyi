import asyncio

from . import Connection, SN

class Client(Connection):
  def __init__(self, host: str, port: int = 10081, loop: asyncio.AbstractEventLoop = None) -> None: ...
  async def connect(self) -> None: ...
