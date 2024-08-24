def three_largest(numbers):
    return sorted(numbers)[-3:]

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Three largest numbers:", three_largest(numbers))


#Find the Three Largest Numbers