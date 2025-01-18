# Testing Text generation with Gemini and then moving on to audi processing

from ut.utils import label1
from src.g1 import text1
from src.g2 import sp_txt


from rich.traceback import install

install(show_locals=True)


def main():
    label1("Transcribing audio/t.wav to text")
    sp_txt()


if __name__ == "__main__":
    main()
