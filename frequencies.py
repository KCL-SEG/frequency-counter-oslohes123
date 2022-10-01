"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(*items):
    frequencies = {}
    for value in items:
        if str(value) in frequencies:
            frequencies[str(value)] = frequencies[str(value)] + 1
        else:
            frequencies[str(value)] = 0
    return frequencies
