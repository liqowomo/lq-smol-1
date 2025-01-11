# Python file to execute marimo basically
import subprocess
from rich import print as rprint

def main():
    rprint("""
    [magenta]Executing file - marimopanty.py""")

def run_marimo():
    subprocess.run("uv", "run", "marimo", "marimopanty.py")

if __name__ == "__main__":
    main()
