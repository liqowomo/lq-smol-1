# Python file to execute marimo basically
import subprocess
from rich import print as rprint
from rich.traceback import install
install(show_locals=True)

def main():
    rprint("""[magenta]
Executing file - marimopanty.py[/magenta]""")
    run_marimo()

def run_marimo():
    subprocess.run("uv", "run", "marimo", "edit" ,"marimopanty.py")

if __name__ == "__main__":
    main()
