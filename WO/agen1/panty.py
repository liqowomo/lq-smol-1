import subprocess
import signal
import os
from rich import print as rprint


def main():
    run_au()


def run_au():
    rprint("Executing AutoGen Studio ... Press Ctrl+C to exit")
    try:
        process = subprocess.Popen(
            ["bash", "-c", "uv run autogenstudio ui"], preexec_fn=os.setsid
        )
        try:
            process.wait()
            if process.returncode != 0:
                rprint(f"AutoGen Studio exited with code: {process.returncode}")
        except KeyboardInterrupt:
            rprint("[bold yellow]Sending SIGTERM to process group...[/bold yellow]")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            process.wait()
            raise
    except FileNotFoundError:
        rprint(
            "Error: 'uv' command not found. Check AutoGen Studio installation and ensure 'uv' is in your PATH."
        )
    except OSError as e:
        rprint(f"OS Error executing AutoGen Studio: {e}")
    except Exception as e:
        rprint(f"An unexpected error occurred: {e}")
    finally:
        rprint("[bold yellow]Performing cleanup...[/bold yellow]")
        rprint("[green]Cleanup complete.[/green]")


if __name__ == "__main__":
    main()
