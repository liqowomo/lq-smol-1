from utils.utils import label1
from pu1.src.pu1.main import pu1run

from rich.traceback import install
from rich import print as rprint


def main():
    label1("""
Running pus1 Crew - from pu1.src.pu1.main import run
function pu1run""")
    pu1run()


if __name__ == "__main__":
    main()
