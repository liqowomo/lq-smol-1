# Main Entry Point here
from ut.utils import label1
from src.s1 import *
import asyncio
from rich.traceback import install

install(show_locals=True)


def main():
    fn_s2()


def fn_s1():
    label1("Executing s1_fn")
    asyncio.run(s1_fn())


def fn_s2():
    label1("Executing s1_fn2")
    asyncio.run(s1_fn2())


if __name__ == "__main__":
    main()
