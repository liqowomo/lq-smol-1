#!/usr/bin/env python
import sys
import warnings

from .crew import Grew1

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def grew1_run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Describe the highest paying bugs in bug bounty programs and how to find them also draw mermaid diagrams, also write code examples for testing vulnerability."
    }
    Grew1().crew().kickoff(inputs=inputs)


def grew1_train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        Grew1().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def grew1_replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Grew1().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def grew1_test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        Grew1().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
