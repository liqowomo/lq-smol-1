# Python file to run autogen studio
import subprocess
from rich import print as rprint


def main():
    run_autogen()


# Executing the autogen
def run_autogen():
    rprint("""
Executing autogen stdudio ... Ctrl + C to exit
[+] uv run autogen ui
""")
    # This function throws and error
    subprocess.run("uv", "run", "autogen", "ui")


if __name__ == "__main__":
    main()
