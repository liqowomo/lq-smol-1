#!/usr/bin/env python
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start


class MeetingMintuesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMintuesFlow(Flow[MeetingMintuesState]):
    @start()
    def trascribe_meeting(self):
        print(
            "Generating Transcription"
        )  # Transcribe the meeting here - from voice/t.wav

        import google.generativeai as genai

        myfile = genai.upload_file("../t.wav")
        print(f"{myfile=}")

        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content([myfile, "Describe this audio clip"])
        print(f"{result.text=}")


def kickoff():
    meeting_minutes_flow = MeetingMintuesFlow()
    meeting_minutes_flow.kickoff()


if __name__ == "__main__":
    kickoff()
