from ut.utils import label1
from crewz.grew1.src.grew1.main import grew1_run

from rich.traceback import install

install(show_locals=True)

# --- Main Function that calls run function from each crew ---


def main():
    g1run()


# --- Functions that call the crews in above main function ---


def g1run():
    """Grew1 Run - This is your experiment"""
    label1("Running grew1 Crew")
    grew1_run()


if __name__ == "__main__":
    main()
