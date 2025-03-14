def get_words(book_text):
    words = book_text.split()
    return len(words)

def num_of_characters(book_text):
    character_counts = {}

    for c in book_text:
        lower = c.lower()
        if lower in character_counts:
            character_counts[lower] += 1
        else:
            character_counts[lower] = 1
    
    return character_counts

def sort_on(dict):
    return dict["num"]


def sort_chars(chars):
    sorted_chars = []
    for char in chars:
        my_dict = {}
        my_dict["char"] = char
        my_dict["num"] = chars[char]
        sorted_chars.append(my_dict)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
