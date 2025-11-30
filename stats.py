def count_words(text_string):
    words = text_string.split()
    return len(words)


def count_characters(text_string):
    character_counts = {}

    for character in text_string:
        lowercase = character.lower()
        if lowercase not in character_counts:
            character_counts[lowercase] = 1
        else:
            character_counts[lowercase] += 1

    return character_counts


def sort_dictionary_list(dictionary_list):
    return dictionary_list.sort(reverse=True, key=sort_on)

def sort_on(items):
    return items["num"]


def create_dictionary_list(dictionary):
    dictionary_list = []

    for key, value in dictionary.items():
        new_dict = {"char": key, "num": value}
        
        dictionary_list.append(new_dict)

    return dictionary_list

