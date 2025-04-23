import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def main():
    # check if user provided a path argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    char_counts = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()