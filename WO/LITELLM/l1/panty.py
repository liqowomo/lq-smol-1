from src.utils import label1
from src.work import or_run1

from rich.traceback import install

install(show_locals=False)


def main():
    label1("Testing OpenRouter here")
    or_run1()


if __name__ == "__main__":
    main()
