#!/usr/bin/python3

from cx_Freeze import setup, Executable

setup(
        name="filing",
        version="1.0",
        description="Filing: used to work with text file",
        executables=[Executable("filing/filing.py")],
        )
