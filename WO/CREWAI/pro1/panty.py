# Standard imports
from ut.utils import label1
from crz.p1.src.p1.main import p1_run


# --- Imports from rich for better errors
from rich.traceback import install

install(show_locals=False)


# --- Main Function ---
def main():
    label1("Exdcuting...crz/C1 - Crew 1")
    P1RUN()


# --- Functions being called from the crews -
def P1RUN():
    label1("crz/P1 Run")
    p1_run()


if __name__ == "__main__":
    main()
