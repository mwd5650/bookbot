from stats import get_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_words(book)
    print(f"{word_count} words found in the document")

main()