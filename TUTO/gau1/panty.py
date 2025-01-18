# Testing Text generation with Gemini and then moving on to audi processing

from ut.utils import label1
from src.g1 import text1
from src.g2 import sp_txt, tr_txt


from rich.traceback import install

install(show_locals=True)


def main():
    tc_audi()


def tc_audi():
    label1("Transcribing Audio - audio/t.wav")
    tr_txt()


if __name__ == "__main__":
    main()
