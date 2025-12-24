from stats import word_count, number_character, sorted_list
import sys

def main():

    if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)


    print("============ BOOKBOT ============")
    print("Analyzing the book")

    print("----------- Word Count ----------")
    num_words = word_count(sys.argv[1])
    print(f"Found {num_words} total words")

    print('--------- Character Count -------')
    character_count = number_character(sys.argv[1])
    sorted_list(character_count)

    print("============= END ===============")



main()