from re import split
from typing import Counter


def word_count(result):
    strg = result.split()
    c = len(strg)
    return c

def letter_count(result):
    dict_of_chars ={}
    for letter in result:
        current_letter = letter.lower()
        if current_letter in dict_of_chars:
            dict_of_chars[current_letter]+=1 
        else:
            dict_of_chars[current_letter] = 1
    return dict_of_chars

def dict_formatter(input_dict,new_dict_name,key_name):
    new_dict_name = []
    for key in input_dict:
        new_dict_name[key_name]= key
        print(new_dict_name)
dict_formatter(letter_count,"test_dict","word")


def sort_char_count(dict_of_char):
    for char in dict_of_char:
        print(dict_of_char)
    return dict_of_char

