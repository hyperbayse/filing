#!/usr/bin/env python3
"""
Module: commands.sort.py
Author: Sheriff Abdulfatai
"""

def sort(file, save_name):
    """
    the function that takes in the file from buffer and
    do a sort activity on it then write it back to file"""
    lines = []
    for buffer in file.readlines():
        lines.append(buffer)
    lines[len(lines) - 1] = lines[len(lines) - 1] + "\n"

    order = input("Sort *asce* for ascending, *desc* for descending and *q* to terminate:- ")
    if order == "asce":
        lines.sort()
    elif order == "desc":
        lines.sort(reverse=True)
    elif order == "q":
        return
    else:
        print("Order operation not correct!\n")
        sort(file, save_name)

    # write the sorted into file
    try:
        with open(save_name, 'w') as save_file:
            for x in lines:
                re = False
                for y in x[:-1]:
                    if y == " ":
                        re = True
                    else:
                        re = False
                        break
                if re == False:
                    save_file.write(x)
    except:
        print("\nError saving file\n")
