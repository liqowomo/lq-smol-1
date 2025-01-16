# Main Entry Point here
from ut.utils import label1
from src.s1 import main
from rich.traceback import install

install(show_locals=True)


def main():
    label1("Panty.py")


if __name__ == "__main__":
    main()
