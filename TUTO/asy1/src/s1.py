# Work 1 Here
from rich import print as rprint
import asyncio


async def s1_fn():
    rprint("Hello")
    await asyncio.sleep(1)
    rprint("World")
    await asyncio.sleep(1)
    rprint("!")


async def s1_fn2():
    rprint("Hello World")
