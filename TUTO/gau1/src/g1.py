# Simple text generation with Gemini
# Code taken from -https://ai.google.dev/gemini-api/docs/quickstart?lang=python

# --- Import zone ---
import os
import datetime
from rich import print as rprint
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# --- Variables zone ---
GA_KEY1 = os.environ.get("GAKE")
genai.configure(api_key=GA_KEY1)
model = genai.GenerativeModel("gemini-1.5-flash")
question_1 = "Explain how AI Booty Dancer works what it he logical tech stack"


# --- Functions zone ---
def text1():
    """Text to LLM Generation"""
    response = model.generate_content(question_1)
    rprint(response.text)
    filewrite(response.text)


def sp_txt():
    """Speech to tect Generation"""
    myfile = genai.upload_file("audio/t.wav")
    rprint(f"{myfile=}")
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content([myfile, "Describe this audio clip"])
    rprint(f"{result.text=}")
    filewrite(result.text)


def filewrite(content):
    """Function to write the file content in a file"""
    now = datetime.datetime.now()
    current_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"rez/my_file_{current_datetime}.md"

    # Create file content (replace with your actual content)
    os.makedirs("rez", exist_ok=True)
    file_content = (
        current_datetime + "---\n\n\n---" + question_1 + "---\n\n\n---" + content + "\n"
    )

    # Write content to file
    with open(filename, "w") as f:
        f.write(file_content)

    rprint(f"File created successfully: {filename}")
