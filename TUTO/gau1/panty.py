# Testing Text generation with Gemini and then moving on to audi processing

from ut.utils import label1
from src.g1 import text1, fu_long
from src.g2 import sp_txt, tr_txt, list_uploaded_files


from rich.traceback import install

install(show_locals=True)


def main():
    fu_long()
    list_uploaded_files()


def fulong():
    label1("Long File Upload Test - Find Vulnerabilities")
    fu_long()


if __name__ == "__main__":
    main()
