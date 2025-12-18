from stats import  letter_count, word_count,char_count_list  
filepath = "books/frankenstein.txt"

def get_book_text(filepath):
        with open(filepath) as f:
            booktext = f.read()
            return booktext
def main():
    result = get_book_text(filepath)
    num_words = word_count(result)
    num_letters = letter_count(result)
    sorted_char_count = char_count_list(letter_count(result))
    #print(num_letters)

    print(
    f"""
    ============ BOOKBOT ============
    Analying book found at {filepath}...
    ----------- Word Count ----------
    {num_words} words found in the document
    --------- Character Count -------
    {sorted_char_count}

    """)

main()
