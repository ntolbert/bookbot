def get_book_text(filepath):
        with open(filepath) as f:
            booktext = f.read()
            return booktext

def word_count(text):
    c = text.split()
    return c 
def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = word_count(result)
    print(f"{num_words}words found in the document")

main()
