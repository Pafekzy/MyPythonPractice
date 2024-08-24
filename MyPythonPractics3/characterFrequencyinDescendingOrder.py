from collections import Counter

text = input("Enter a string: ")
frequency = Counter(text)
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print("Character frequency (descending order):")
for char, freq in sorted_frequency:
    print(f"{char}: {freq}")

#Character Frequency in Descending Order