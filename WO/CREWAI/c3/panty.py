from ut.utils import label1
from grew1.src.grew1.main import grew1_run

from rich.traceback import install

install(show_locals=True)


def main():
    label1("Running grew1 Crew")
    grew1_run()


if __name__ == "__main__":
    main()
