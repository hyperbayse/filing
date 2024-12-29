#!/usr/bin/env python3
"""
Module: utils.docx_extractor.py
Author: Sheriff Abdulfatai
"""
from docx import Document

def docx_extractor(file):
    """ saves the content of a .docx file to a temporary
    .txt file for processing """
    doc = Document(file)
    with open(".tmpbuffer.txt", 'w') as write:
        for para in doc.paragraphs:
            write.write(para.text)
    return ".tmpbuffer.txt"