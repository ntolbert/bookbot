import sys
from stats import  letter_count, word_count,char_count_list  



def get_book_text(filepath):
        with open(filepath) as f:
            booktext = f.read()
            return booktext
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2: 
        filepath = sys.argv[1] 
        result = get_book_text(filepath)
        num_words = word_count(result)
        sorted_char_count = char_count_list(letter_count(result))

        print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------")
        for i in sorted_char_count:
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
main()
