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
def sort_on(item):
    return item["num"]
def char_count_list(char_dict):
    list_of_letter_count_dict=[]
    dict_char_num={}
    for val in char_dict:
        dict_char_num["char"]= val  
        dict_char_num["num"] = char_dict[val]
        if dict_char_num["char"].isalpha():
            list_of_letter_count_dict.append(dict_char_num)
        dict_char_num={}
    list_of_letter_count_dict.sort(reverse=True, key=sort_on)
    
    return list_of_letter_count_dict
    





