import subprocess
from rich import print as rprint


def main():
    rprint("Executing AutoGen Studio ... Ctrl + C to exit")
    run_autogen()


def run_autogen():
    try:
        # Try with a shell process (adjust if necessary)
        shell_process = subprocess.Popen(["fish", "-c", "uv run autogen ui"])
        shell_process.wait()  # Wait for the subshell process to finish
    except FileNotFoundError:
        print(
            "Error: 'uv' command not found. Please check the AutoGen Studio installation."
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: AutoGen Studio UI failed to start. Exit code: {e.returncode}")


if __name__ == "__main__":
    main()
