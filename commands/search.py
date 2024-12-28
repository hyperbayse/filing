#!/usr/bin/env python3
"""
Module: commands.search.py
Author: Sheriff Abdulfatai
"""

def search(file):
    """ this does the search operation on a file """
    searchable = input("Searching for:- ")
    save_name = input("Enter save_name or return to display only:- ")

    # line counter
    count = 0
    if len(save_name) == 0:
        print("para\ttext")
    elif len(save_name) > 0:
        with open(save_name, 'w') as write:
            write.write("para\ttext\n")

    for line in file.readlines():
        count += 1
        if searchable in line and len(save_name) == 0:
            print(f"{count}\t{line}")
        elif searchable in line and len(save_name) > 0:
            with open(save_name, 'a') as write:
                write.write(f"{count}\t{line}")

    if count == 0 and len(save_name) == 0:
        print(f"{searchable} not found")
    elif count == 0 and len(save_name) > 0:
        with open(save_name, 'w') as write:
            write.write(f"{searchable} not found")
