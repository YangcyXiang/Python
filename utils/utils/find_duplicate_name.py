def find_duplicate_words(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            text = file.read()

        words = text.split()
        word_count = {}
        duplicates = []

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for word, count in word_count.items():
            if count > 1:
                duplicates.append(word)

        return duplicates
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return []

# Example usage:
filename = 'data/find_duplicate_name_list_input.txt'
duplicates = find_duplicate_words(filename)
print(f"Duplicate words: {duplicates}")
