from stats import get_words, num_of_characters,sort_chars
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        book = get_book_text(sys.argv[1])
        word_count = get_words(book)
        characters_in_book = num_of_characters(book)
        sorted_chars = sort_chars(characters_in_book)
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for char in sorted_chars:
            character = char["char"]
            count = char["num"]
            print(f"{character}: {count}")
        print("============= END ===============")

main()