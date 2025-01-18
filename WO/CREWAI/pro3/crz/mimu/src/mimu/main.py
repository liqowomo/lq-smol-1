#!/usr/bin/env python
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start


class MeetingMintuesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMintuesFlow(Flow[MeetingMintuesState]):
    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")


def kickoff():
    meeting_minutes_flow = MeetingMintuesFlow()
    meeting_minutes_flow.kickoff()


if __name__ == "__main__":
    kickoff()
