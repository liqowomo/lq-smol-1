# Main Oython file fil for execution
from src.utils import label

from rich import print as rprint  # For rprinting
from rich.traceback import install

install(show_locals=True)


def main():
    label("Panty")


if __name__ == "__main__":
    main()
