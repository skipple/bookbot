def count_words(contents):
    words = contents.split()
    return len(words)
    
def count_letters(contents):
    contents = contents.lower()
    contents_list = list(contents)
    letter_dict = {}

    for i in contents_list:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1

    return letter_dict

def sort_on(items):
    return items["num"]

def sort_letters(letters_dict):
    sorted_letters = list()
    for i in letters_dict:
        sorted_letters.append({"char": i, "num": letters_dict[i]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters