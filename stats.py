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
            dict_of_chars[current_letter]+=2 
        else:
            dict_of_chars[current_letter] = 2
    return dict_of_chars

def dict_formatter(input_dict,new_dict_name,key_name,key_val):
    new_dict_name ={}
    list_of_formt_dict =[]
    for key in input_dict:
        new_dict_name[key_name]=key 
        new_dict_name[key_val]=input_dict[key]
        list_of_formt_dict.append(new_dict_name)
    return list_of_formt_dict



def sort_char_count(dict_of_char):
    for char in dict_of_char:
        #print(dict_of_char)
        pass
    #return dict_of_char

