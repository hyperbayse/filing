#!/usr/bin/env python3
"""
Module: filing.py
Author: Sheriff Abdulfatai
"""


from commands.sort import sort

print("** Thanks for using filing!"
      "\nit is an open-source app that can be used to do some basic document manipulation\n"
      "among the currently supported commands are -sort- -count- -search- -extract- **")

commands = ['sort', 'count', 'search', 'extract']
extension = ['docs', 'txt', 'pdf', 'csv']

# open the provided file for text manipulation
while True:
    filename = input("\ninput the file you are working with :- ")
    print()

    if filename == 'exit':
        exit()
    # filename = "text.txst"

    name, dot, extn = filename.partition('.')

    # check if the file extension is supported
    if extn not in extension:
        print("file ({}) not supported".format(filename))
    else:
        break
        
try:
    with open(f"{filename}", 'r') as file:
        while True:
            # check for the input command
            command = input("enter your operation :- ")
            save_name = input("save file as :- ")

            if command == "quit":
                break

            if command not in commands:
                print("command not supported now \"will be updated in future\"")
            else:
                break
        
        if command == "sort":
            sort(file, save_name)
        
except FileNotFoundError:
    print("file not found\ncheck your input")