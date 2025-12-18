


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
            dict_of_chars[current_letter] = 2
    return dict_of_chars
#def sort_on():
    #return item["num"]
def char_count_list(char_dict):
    list_of_letter_count_dict=[]
    dict_char_num={}
    for val in char_dict:
        dict_char_num["char"]= val
        dict_char_num["num"] = char_dict[val]
    for k in char_dict:
        list_of_letter_count_dict.append(k)
    print(list_of_letter_count_dict)
    return char_dict
    





