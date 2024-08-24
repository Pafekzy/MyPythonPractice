def has_unique_chars(s):
    return len(s) == len(set(s))

string = input("Enter a string: ")
print("Contains only unique characters:", has_unique_chars(string))


# Check if String Contains Only Unique Characters