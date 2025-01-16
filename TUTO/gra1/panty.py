# Gra Main funcs here
from src.g1 import App1
from ut.utils import label1

from rich.traceback import install

install(show_locals=True)


def main():
    label1("App1")
    App1()


if __name__ == "__main__":
    main()
