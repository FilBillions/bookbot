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


