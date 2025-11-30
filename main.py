import sys
from stats import *

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

   
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    

    num_characters = count_characters(book_text)

    dict_list = create_dictionary_list(num_characters)

    sort_dictionary_list(dict_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1]+"...")

    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count ---------")
    for entry in dict_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

    print("============= END =============")


main()

