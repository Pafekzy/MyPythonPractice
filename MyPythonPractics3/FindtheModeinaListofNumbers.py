from collections import Counter

def find_mode(numbers):
    counter = Counter(numbers)
    max_count = max(counter.values())
    mode = [num for num, count in counter.items() if count == max_count]
    return mode

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Mode:", find_mode(numbers))


# FindtheModeinaListofNumbers