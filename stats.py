def get_num_words(text):
    words = text.split()
    return len(words)

def get_char(text):
    lowercase_text = text.lower()
    list_of_characters = list(lowercase_text)
    dictionary = {}
    for letter in list_of_characters:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

def sort_on(d):
    return d["num"]


def sorted_dictionary(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list