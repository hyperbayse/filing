#!/usr/bin/env python3
"""
Module: utils.pdf_extractor.py
Author: Sheriff Abdulfatai
"""

from PyPDF2 import PdfReader

def pdf_extractor(file):
    reader = PdfReader(file)

    with open(".tmpbuffer.txt", 'w') as write:
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            write.write(text)
    return ".tmpbuffer.txt"