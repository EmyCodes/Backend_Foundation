#!/usr/bin/python3

from pdf2docx import parse
from sys import argv


# check
def convert_pdf_to_docx(original=argv[1], converted=argv[2]):
        to_convert = f"./{argv[1]}"
        converted_to = f"./{argv[2]}"
        
        parse(to_convert, converted_to)

convert_pdf_to_docx()
