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
      "\nit is an open-source app that can be used to do some basic document manipulation\n"
      "among the currently supported commands are -sort- -count- -search- -extract- **")

commands = ['sort', 'count', 'search', 'display']

# open the provided file for text manipulation
while True:
    filename = input("\nEnter file you are working with or exit to quit:- ")
    print()

    if filename == 'exit':
        exit()
    # filename = "text.txst"

    extn = extn_checker(filename)

    if os.path.exists(filename):
        break

# convert all text to .txt first
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
    print("f\File not found\nCheck your input")

# ensure the buffer file is deleted
try:
    os.remove(".tmpbuffer.txt")
except:
    pass