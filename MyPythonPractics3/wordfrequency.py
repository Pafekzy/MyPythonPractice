from collections import Counter

filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    words = file.read().split()
    word_count = Counter(words)
    print(word_count)

#Write a Python program that reads a text file and counts the frequency of each word in the file.