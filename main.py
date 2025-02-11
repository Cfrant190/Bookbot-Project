def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    multi_list_of_dictionaries = dict_to_multi_list(char_count)
    multi_list_of_dictionaries.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char_dict in multi_list_of_dictionaries:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    lower = text.lower()
    char_count_dict = {}
    for character in lower:
        if f"{character}" in char_count_dict:
            char_count_dict[f"{character}"] += 1

        elif f"{character}" not in char_count_dict:
            char_count_dict[f"{character}"] = 1

    return char_count_dict

def dict_to_multi_list(char_count):
    char_list = []
    for character in char_count:
        if character.isalpha():
            char_dict = {
                "char": character,
                "count": char_count[character]
            }

            char_list.append(char_dict)

    return char_list

def sort_on(dict):
    return dict["count"]


main()

