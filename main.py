from stats import letter_count, word_count
def get_book_text(filepath):
        with open(filepath) as f:
            booktext = f.read()
            return booktext
def main():
    result = get_book_text("books/frankenstein.txt")
   # print(result)
    num_words = word_count(result)
    print(f"{num_words} words found in the document")
    l = letter_count(result)
    print(l)
main()
