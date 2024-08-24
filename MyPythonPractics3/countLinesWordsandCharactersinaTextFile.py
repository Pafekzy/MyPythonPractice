def count_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_lines, num_words, num_chars

filename = input("Enter the filename: ")
lines, words, chars = count_file(filename)
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")


# Count Lines, Words, and Characters in a Text File