#!/usr/bin/env python
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start


class MimuFlowState(BaseModel):
    transcription: str = ""
    mimu_minutes: str = ""


class MimuFlow(Flow[PoemState]):
    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
