#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Inherits form a list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
