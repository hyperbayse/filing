#!/usr/bin/python3

from docx import Document


doc = Document("RISKIYAT CV.docx")

print(doc)

print(doc.paragraphs[16].text)