# Python file to execute marimo basically
import subprocess
from rich import print as rprint
from rich.traceback import install
install(show_locals=True)

def main():
    rprint("""[magenta]
Executing file - marimopanty.py
[+] Run command - uv run edit marimopanty.py 
[+] Ctrl+c to exit 
[/magenta]""")
    

def run_marimo():
    # This function throws and error
    subprocess.run("uv", "run", "marimo", "edit" ,"marimopanty.py")

if __name__ == "__main__":
    main()
