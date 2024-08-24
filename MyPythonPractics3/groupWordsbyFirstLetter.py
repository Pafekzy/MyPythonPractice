from collections import defaultdict

def group_by_first_letter(words):
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)
    return dict(grouped)

words = input("Enter a list of words separated by spaces: ").split()
print("Grouped by first letter:", group_by_first_letter(words))


#  GroupWordsbyFirstLetter