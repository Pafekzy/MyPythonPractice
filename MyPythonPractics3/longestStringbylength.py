words = input("Enter a list of words separated by spaces: ").split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)
