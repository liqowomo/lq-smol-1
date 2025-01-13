from src.utils import label1
from pus1.src.pus1.main import run

from rich.traceback import install
from rich import print as rprint

install(show_locals=True)


def main():
    label1("Running pus1 Crew")
    run()


if __name__ == "__main__":
    main()
