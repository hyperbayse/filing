#!/usr/bin/env python3
"""
Module: filing.py
Author: Sheriff Abdulfatai
"""


from commands.sort import sort
from commands.search import search
from commands.count import count

print("** Thanks for using filing!"
      "\nit is an open-source app that can be used to do some basic document manipulation\n"
      "among the currently supported commands are -sort- -count- -search- -extract- **")

commands = ['sort', 'count', 'search', 'extract']
extension = ['docs', 'txt', 'pdf', 'csv']
no_save = ['count', 'search']

# open the provided file for text manipulation
while True:
    filename = input("\nFile you are working with or exit to exit:- ")
    print()

    if filename == 'exit':
        exit()
    # filename = "text.txst"

    name, dot, extn = filename.partition('.')

    # check if the file extension is supported
    if extn not in extension:
        print("File ({}) with .{} not supported".format(filename, extn))
    else:
        break
        
try:
    with open(f"{filename}", 'r') as file:
        while True:
            # check for the input command
            command = input("Enter your operation:- ")
            if command not in no_save and command in commands:
                save_name = input("Save file as:- ")

            if command == "quit":
                break

            if command not in commands:
                print("Command not supported now \"will be updated in future\"")
            else:
                break
        
        if command == "sort":
            sort(file, save_name)
        if command == "search":
            search(file)
        if command == "count":
            count(file)
        
except FileNotFoundError:
    print("f\File not found\nCheck your input")