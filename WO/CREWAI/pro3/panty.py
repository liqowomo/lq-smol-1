# Crew actual entry point
import agentops
from ut.utils import label1

from rich.traceback import install

agentops.init()  # Required fro agentops
install(show_locals=False)  # Required for prettier errors


def main():
    label1("Flowza")


if __name__ == "__main__":
    main()
