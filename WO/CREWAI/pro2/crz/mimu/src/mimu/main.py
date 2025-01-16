#!/usr/bin/env python
from rich import print as rprint
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start


class MimuFlowState(BaseModel):
    transcription: str = ""
    mimu_minutes: str = ""


class MimuFlow(Flow[MimuFlowState]):
    @start()
    def transcribe_meeting(self):
        rprint("Generating Transcript")


def kickoff():
    poem_flow = MimuFlowState()
    poem_flow.kickoff()


def plot():
    poem_flow = MimuFlowState()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
