from ut.utils import label1
from crewz.grew1.src.grew1.main import grew1_run
from crewz.grew2.src.grew2.main import grew2_run

from rich.traceback import install

install(show_locals=True)

# --- Main Function that calls run function from each crew ---


def main():
    g2run()


# --- Functions that call the crews in above main function ---


def g1run():
    """Grew1 Run - This is your experiment"""
    label1("Running grew1 Crew")
    grew1_run()


def g2run():
    """Grew1 Run - This is your experiment"""
    label1("Running grew2 Crew")
    grew2_run()


if __name__ == "__main__":
    main()
