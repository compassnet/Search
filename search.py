#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

"""
Search - A program to search for text patterns
Copyright (C) 2020 Compass 
Websites:
    https://8kun.top/slackware/
    https://github.com/compassnet
IRC Channels:
    #slackware@irc.rizon.net
    ##python@irc.rizon.net
    ##linux@irc.rizon.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""


class Search:
    """Class that represents a text pattern searching program."""

    def __init__(self):
        """Initialize the attributes below if present."""
        self.filename_lines = ''
        self.pattern_lines = ''

    def instructions(self):
        """Instructions of the Search program."""
        # Print an introduction of the program.
        message = (
                "Welcome to the Search program!\n"
                "This program is designed to search for case\n"
                "insensitive text patterns.\n"
                "Instructions:\n"
                "1. It is recommended (but not required) to put\n"
                "search.py in the same directory where the files\n"
                "you want to search from are, or use the full\n"
                "path (eg.: /home/python3/file.txt (for *nix) or\n"
                "C:\Documents\\file.txt (for Windows)).\n"
                "2. Search requires you to type the name of the\n"
                "file you want to search from.\n"
                "3. Search requires you to type the name of the\n"
                "file containing the search patterns (one pattern\n"
                "per line).\n"
                "4. Use 'q' at any time to quit the program."
                )
        print(message)

    def file_name(self):
        """Obtain and read the filename to search from."""
        file_name = "\nEnter the name of the file you want to search from: "
        while True:
            """
            The self.filename attribute assumes the value 
            of input(file_name).
            'q' exits the program, else self.filename is read line by
            line and its value returned as self.filename_lines.
            If self.filename is invalid (eg. doesn't exist), the
            program will ask continuously for a proper self.filename.
            """
            self.filename = input(file_name)
            if self.filename == 'q':
                print("Quitting Search...")
                exit()
            else:
                try:
                    with open(self.filename) as file:
                        self.filename_lines = file.readlines()
                    return self.filename_lines
                except FileNotFoundError:
                    print(f"\"{self.filename}\" was not found! Try again!")

    def file_pattern(self):
        """Obtain and read the filename that contains the patterns."""
        pattern_name = "\nName of the file containing the patterns: "
        while True:
            """
            The self.pattern attribute assumes the value of
            input(patten_name). If it's 'q' the program exits, else
            self.pattern is read line by line and its value returned
            as self.pattern_lines.
            If self.pattern is invalid (eg. doesn't exist), the program
            will ask continuously for a proper self.pattern.
            """
            self.pattern = input(pattern_name)
            if self.pattern == 'q':
                print("Quitting Search...")
                exit()
            else:
                try:
                    with open(self.pattern) as file:
                        self.pattern_lines = file.readlines()
                    return self.pattern_lines
                    break
                except FileNotFoundError:
                    print(f"\"{self.pattern}\" was not found! Try again!")

    def strip_files(self):
        """Strip both file names."""
        while True:
            """
            If self.filename_lines or self.pattern_lines are 'q' the
            program exits.
            """
            if self.filename_lines == 'q' or self.pattern_lines == 'q':
                exit()
            else:
                """
                List comprehension that strips the empty spaces and
                makes all the alphabetical characters lowercase.
                I had to Google this. My knowledge of list
                comprehensions is limited.
                I tried using for loops with no success, but if I can
                get that to work I might change the code.
                I'll explain this better later if I can.
                """
                self.filename_lines = [self.filename_lines.lower().strip() 
                        for self.filename_lines in self.filename_lines]
                self.pattern_lines = [self.pattern_lines.lower().strip() 
                        for self.pattern_lines in self.pattern_lines]
                break

    def find_patterns(self):
        """Use the patterns to search."""
        """
        Insert a single newline. If 'end = ""' is removed, you'll get a
        double newline because print itself inserts a newline to the
        output.
        """
        print("\n", end = "")
        """
        List comprehension that compares the patterns with the file name
        obtained from the user.
        I had to Google this. My knowledge of list comprehensions is
        limited.
        I tried using for loops with no success, but if I can get that
        to work I might change the code.
        I'll explain this better later if I can.
        """
        matches = [item for item in self.pattern_lines if any(item in item 
            for item in self.filename_lines)]
        for match1 in matches:
            matches = [item for item in self.filename_lines if match1 in item]
            for match2 in matches:
                print(f"Pattern \"{match1}\" found in line -> \"{match2}\"")


test = Search()
test.instructions()
test.file_name()
test.file_pattern()
test.strip_files()
test.find_patterns()
