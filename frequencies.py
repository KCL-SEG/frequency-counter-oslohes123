"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for value in items:
        if str(value) in frequencies:
            frequencies[str(value)] = frequencies[str(value)] + 1
        else:
            frequencies[str(value)] = 1
    return frequencies


input = ['0', 4,4,'4','d','d','e',0,'a','d','4']
frequencies(input)