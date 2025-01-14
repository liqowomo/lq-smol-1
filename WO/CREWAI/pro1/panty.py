# Standard imports
from ut.utils import label1
from crz.p1.src.p1.main import p1_run


# --- Imports from rich for better errors
from rich.traceback import install

install(show_locals=True)


# --- Main Function ---
def main():
    label1("Exdcuting...crz/C1 - Crew 1")


# --- Functions being called from the crews -
# def C1RUN():
#     label1("crz/C1 Run")
#     C1_run()


if __name__ == "__main__":
    main()
