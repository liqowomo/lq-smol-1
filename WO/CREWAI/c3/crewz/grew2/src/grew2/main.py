#!/usr/bin/env python
import sys
import warnings

from .crew import Grew2

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def grew2_run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "High Paying bug Bounties in web 3 apps, how to discover, report and make poc of them"
    }
    Grew2().crew().kickoff(inputs=inputs)


def grew2_train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        Grew2().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def grew2_replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Grew2().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def grew2_test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        Grew2().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
