#!/usr/bin/env python3
"""
Module: commands.search.py
Author: Sheriff Abdulfatai
"""

import re

def count(file):
    """ this does the search operation on a file """
    countable = input("Counting:- ")

    # line counter
    count = re.findall(f"{countable}", file.read())

    # for line in file.readlines():
    #     occurence = re
    #     if countable in line:
    #         count += 1

    print(f"'{countable}' found **{len(count)}** times")