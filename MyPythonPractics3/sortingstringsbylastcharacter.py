def sort_by_last_char(strings):
    return sorted(strings, key=lambda x: x[-1])

words = input("Enter a list of words separated by spaces: ").split()
sorted_words = sort_by_last_char(words)
print("Words sorted by last character:", sorted_words)
