import subprocess
import signal
import os
from rich import print as rprint


def main():
    rprint("Executing AutoGen Studio ... Press Ctrl+C to exit")
    try:
        run_autogen()
    except KeyboardInterrupt:
        rprint("[bold red]AutoGen Studio execution interrupted.[/bold red]")
        cleanup()


def run_autogen():
    try:
        process = subprocess.Popen(
            ["bash", "-c", "uv run autogenstudio ui"], preexec_fn=os.setsid
        )
        process.wait()
        if process.returncode != 0:
            rprint(f"AutoGen Studio exited with code: {process.returncode}")
    except FileNotFoundError:
        rprint(
            "Error: 'uv' command not found. Check AutoGen Studio installation and ensure 'uv' is in your PATH."
        )
    except OSError as e:  # Catch OSError for permission or execution errors
        rprint(f"OS Error executing AutoGen Studio: {e}")
    except Exception as e:
        rprint(f"An unexpected error occurred: {e}")


def cleanup():
    rprint("[bold yellow]Performing cleanup...[/bold yellow]")
    rprint("[green]Cleanup complete.[/green]")


if __name__ == "__main__":
    main()
