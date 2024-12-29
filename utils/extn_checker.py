#!/usr/bin/env python3
"""
Module: utils.extn_checker.py
Author: Sheriff Abdulfatai
"""
import os

def extn_checker(file):
    """ checks and confirm if the file is supported """
    extension = ['docx', 'txt', 'pdf']

    name, dot, extn = file.partition('.')

    # check if the file extension is supported
    if extn not in extension:
        print("File ({}) with .{} not supported".format(file, extn))
    elif not os.path.exists(file):
        print("File does not exist")
    else:
        return extn