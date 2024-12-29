#!/usr/bin/env python3
"""
Module: filing.py
Author: Sheriff Abdulfatai
"""

import os

#utils
from utils.pdf_extractor import pdf_extractor
from utils.extn_checker import extn_checker
from utils.docx_extractor import docx_extractor

#commands
from commands.sort import sort
from commands.search import search
from commands.count import count


print("** Thanks for using filing!"
      "\nIt is an open-source app that can be used to access some basic document content\n"
      "Among the currently supported functions are -sort- -count- -search- -display-"
      "\nAnd supported file extensions are .pdf, .txt, .docx **")

commands = ['sort', 'count', 'search', 'display']

# open the provided file for text manipulation
while True:
    filename = input("\nEnter file you are working with or exit to quit:- ")
    print()

    extn = extn_checker(filename)

    if filename == 'exit':
        exit()

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

            if command == "quit":
                break

            if command not in commands:
                print("Command not supported now \"will be updated in future\"")
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