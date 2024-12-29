#!/usr/bin/env python3
"""
Module: filing.py
Author: Sheriff Abdulfatai
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#utils
from utils.pdf_extractor import pdf_extractor
from utils.extn_checker import extn_checker
from utils.docx_extractor import docx_extractor

#commands
from commands.sort import sort
from commands.search import search
from commands.count import count
from commands.display import display


print("** Thanks for using filing!"
      "\nIt is an open-source app that can be used to access some basic document content\n"
      "Among the currently supported functions are -sort- -count- -search- -display-"
      "\nAnd supported file extensions are .pdf, .txt, .docx **")

commands = ['sort', 'count', 'search', 'display']

# open the provided file for text manipulation
while True:
    filename = input("\nEnter file you are working with or exit to quit:- ")
    print()

    if filename == 'exit':
        sys.exit()

    extn = extn_checker(filename)

    if os.path.exists(filename) and type(extn) == str:
        break

# convert all text to tmp .txt first
if extn == "pdf":
    filename = pdf_extractor(filename)
if extn == "docx":
    filename = docx_extractor(filename)

try:
    with open(f"{filename}", 'r') as file:
        while True:
            # check for the input command
            command = input("Enter your operation:- ")

            if command == "exit":
                sys.exit()

            if command not in commands:
                print("Operation not supported")
                print("Re-enter operation or exit to quit")
            else:
                break
        
        if command == "sort":
            sort(file)
        if command == "search":
            search(file)
        if command == "count":
            count(file)
        if command == "display":
            display(file)
        
except FileNotFoundError:
    print("File not found\nCheck your input")

# ensure the buffer file is deleted
try:
    os.remove(".tmpbuffer.txt")
except:
    pass