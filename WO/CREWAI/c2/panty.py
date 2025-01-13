from utils.utils import label1
from pu1.src.pu1.main import pu1run
from pu2.src.pu2.main import pu2run

from rich.traceback import install
from rich import print as rprint


def main():
    pu2runz()


def pu1runz():
    label1("""
Running pus1 Crew - from pu1.src.pu1.main import run
function pu1run""")
    pu1run()


def pu2runz():
    label1("""
Running pus1 Crew - from pu2.src.pu2.main import pu2run
Second crew called pu2 being run from inside the same env
""")
    pu2run()


if __name__ == "__main__":
    main()
