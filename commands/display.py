#!/usr/bin/env python3
"""
Module: commands.display.py
Author: Sheriff Abdulfatai
"""

def count(file):
    for line in file.readlines():
        print(line)