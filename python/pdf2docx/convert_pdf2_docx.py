#!/usr/bin/python3

from pdf2docx import parse
from sys import argv


# check
def convert_pdf_to_docx(original=argv[1], converted=argv[2]):
    """This function covert pdf file to docx file"""
    to_convert = f"./{original}"
    converted_to = f"./{converted}"
    
    parse(to_convert, converted_to)


if __name__ == "__main__":
    convert_pdf_to_docx()
