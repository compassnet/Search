#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

"""
Search - A program to search for text patterns
Copyright (C) 2020 Compass 
Website: https://8kun.top/slackware/
IRC Channels: #slackware@irc.rizon.net, ##python@irc.rizon.net or ##linux@irc.rizon.net

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
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
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
        message = "\nWelcome to the Search program!"
        message += "\nThis program is designed to search for ___case insensitive text patterns___.\n"
        message += "\nInstructions:\n"
        message += "\n1. It is recommended (but not required) to put search.py in the same directory where the files you want to"
        message += "\nsearch from are, or use the full path (eg.: /home/python3/file.txt (for *nix) or C:\Documents\\file.txt (for Windows))"
        message += "\n2. Search requires you to type the name of the file you want to search from."
        message += "\n3. Search requires you to type the name of the file containing the search patterns (one pattern per line)."
        print(message)

    def file_name(self):
        """Obtain and read the filename to search from."""
        file_name = "\nPlease type the name of the file you want to search from ('q' to quit): "
        while True:
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
                    print(f"\"{self.filename}\" was not found! Please try again!")

    def file_pattern(self):
        """Obtain and read the filename that contains the patterns."""
        pattern_names = "\nPlease type the name of the file containing the patterns ('q' to quit): "
        while True:
            self.pattern = input(pattern_names)
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
                    print(f"\"{self.pattern}\" was not found! Please try again!")

    def strip_files(self):
        """Strip both file names."""
        # Make all the list items lowercase and remove all the whitespaces.
        while True:
            if self.filename_lines == 'q' or self.pattern_lines == 'q':
                exit()
            else:
                self.filename_lines = [self.filename_lines.lower().strip() for self.filename_lines in self.filename_lines]
                self.pattern_lines = [self.pattern_lines.lower().strip() for self.pattern_lines in self.pattern_lines]
                break

    def find_patterns(self):
        """Use the patterns to search."""
        print("\n", end = "")
        matches = [item for item in self.pattern_lines if any(item in item for item in self.filename_lines)]
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
