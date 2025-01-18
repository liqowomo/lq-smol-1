# Testing Text generation with Gemini and then moving on to audi processing

from ut.utils import label1
from src.g1 import text1
from src.g2 import sp_txt, tr_txt
from src.g3 import img1


from rich.traceback import install

install(show_locals=True)


def main():
    img_maker()


def img_maker():
    label1("Generating Image")
    img1()


if __name__ == "__main__":
    main()
