import sys

from stats import count_words, character_count_dictionary, rank_character_count

def get_book_text(filepath: str) -> str:
    with open(filepath) as book_file:
        book_text = book_file.read()
    return book_text

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)
    book_word_count = count_words(book_text)
    book_character_counts = character_count_dictionary(book_text)
    ranking = rank_character_count(book_character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")

    for character_data in ranking:
        character = character_data["char"]
        if character.isalpha():
            count = character_data["num"]
            print(f"{character}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
