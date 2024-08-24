def word_lengths(sentence):
    return {word: len(word) for word in sentence.split()}

sentence = input("Enter a sentence: ")
print(word_lengths(sentence))

# Create a Python function that takes a sentence as input and returns a dictionary with words as keys and their lengths as values.