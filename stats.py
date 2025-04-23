def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def chars_dict_to_sorted_list(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
    