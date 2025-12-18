from stats import dict_formatter, letter_count, word_count,sort_char_count 

def get_book_text(filepath):
        with open(filepath) as f:
            booktext = f.read()
            return booktext
def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = word_count(result)
    print(f"{num_words} words found in the document")
    num_letters = letter_count(result)
    #print(num_letters)
    forrmater = dict_formatter(num_letters,"new_di","name","num")
    print(forrmater)
    #report = sort_char_count(num_letters)
    #print(report)
main()
