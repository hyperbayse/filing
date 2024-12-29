#!/usr/bin/env python3
"""
Module: utils.pdf_extractor.py
Author: Sheriff Abdulfatai
"""

from PyPDF2 import PdfFileReader

def pdf_extractor(file):
    with open(file, 'rb') as buffer:
        pdf = PdfFileReader(buffer)
        readable = []
        for page in pdf.pages:
            readable.append(page.extract_text())
    with open(".tmpbuffer.txt", 'w') as write:
        for x in readable:
            write.write(x)
    return ".tmpbuffer.txt"