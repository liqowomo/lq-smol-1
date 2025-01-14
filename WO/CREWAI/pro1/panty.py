# Standard imports
from ut.utils import label1
from crz.p1.src.p1.main import p1_run
from crz.poem_flow.src.poem_flow.main import kickoff, plot

# --- Imports from rich for better errors
from rich.traceback import install

install(show_locals=False)


# --- Main Function ---
def main():
    powem_flowRUN()


# --- Functions being called from the crews -
def P1RUN():
    label1("crz/P1 Run")
    p1_run()


def powem_flowRUN():
    label1("crz/poemflow/kickoff and plot")
    kickoff()
    plot()


if __name__ == "__main__":
    main()
