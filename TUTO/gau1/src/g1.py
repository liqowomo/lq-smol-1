# Simple text generation with Gemini
# Code taken from -https://ai.google.dev/gemini-api/docs/quickstart?lang=python

from rich import print as rprint
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def text1():
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    rprint(response.text)
