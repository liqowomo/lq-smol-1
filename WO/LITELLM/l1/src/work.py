import os
from litellm import completion

from rich import print as rprint
from rich.traceback import install

install(show_locals=True)

os.environ["OPENROUTER_API_KEY"] = os.environ.get("PANTY")


msg = [
    {
        "content": "Tell me 3 things to become a super duper Bug Bounty Hunter?",
        "role": "user",
    }
]
mdl = "openrouter/google/gemini-2.0-flash-thinking-exp:free"


def or_run1():
    response = completion(
        model=mdl,
        messages=msg,
    )
    rprint(response)
    rprint(response["choices"][0]["message"]["content"])
    content = response["choices"][0]["message"]["content"]

    with open("PantyResponse.txt", "w", encoding="utf-8") as f:  # Write to file
        f.write(content)
