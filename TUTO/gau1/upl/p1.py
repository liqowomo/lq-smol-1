# Testing Text generation with Gemini and then moving on to audi processing

from ut.utils import label1
from src.g1 import text1
from src.g2 import sp_txt, tr_txt, list_uploaded_files


from rich.traceback import install

install(show_locals=True)


def main():
    list_uploaded_files()


def tc_audi():
    label1("Transcribing Audio - audio/t.wav")
    tr_txt()


if __name__ == "__main__":
    main()
