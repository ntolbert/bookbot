from re import split
from typing import Counter


def word_count(result):
    strg = result.split()
    c = len(strg)
    return c

def letter_count(result):
    chars ={}
    for letter in result:
        s = letter.lower()
        if s in chars:
            chars[s]+=1 
        else:
            chars[s] = 1
    return chars

