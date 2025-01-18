# Speech to text transcribe
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


# --- Functions zone ---


def sp_txt():
    """Explaining the audio"""
    myfile = genai.upload_file("audio/t.wav")
    rprint(f"{myfile=}")
    result = model.generate_content([myfile, "Describe this audio clip"])
    rprint(f"{result.text=}")
    filewrite(result.text)


def tr_txt():
    """Transcribing the audio"""
    audio_file = genai.upload_file("audio/t.wav")
    rprint(f"{audio_file=}")
    prompt = "Generate a transcript of the speech."
    response = model.generate_content([prompt, audio_file])
    rprint(response.text)
    filewrite(response.text)


def filewrite(content):
    """Function to write the file content in a file"""
    now = datetime.datetime.now()
    current_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"rez/transcribez_{current_datetime}.md"

    # Create file content (replace with your actual content)
    os.makedirs("rez", exist_ok=True)
    file_content = current_datetime + "\n---\n" + content + "\n"

    # Write content to file
    with open(filename, "w") as f:
        f.write(file_content)

    rprint(f"File created successfully: {filename}")


# -- File Management Function
def list_uploaded_files():
    # Open a file to write the output
    with open("uploaded_files.txt", "w") as file:
        file.write("My files:\n")  # Write the header
        for f in genai.list_files():
            file.write(f"  {f.name}\n")  # Write each file name to the file
