# Standard imports
from ut.utils import label1


# --- Imports from rich for better errors
from rich.traceback import install

install(show_locals=True)

# --- Main Function ---


def main():
    label1("Panty.py")


# --- Functions being called from the crews -


if __name__ == "__main__":
    main()
