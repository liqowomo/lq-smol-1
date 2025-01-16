from ut.utils import label1

from rich import print as rprint
from rich.traceback import install

install(show_locals=True)


def main():
    label1("Hello from pro1!")


if __name__ == "__main__":
    main()
