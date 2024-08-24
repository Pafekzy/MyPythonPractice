def is_palindrome(lst):
    return lst == lst[::-1]

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Is palindrome:", is_palindrome(numbers))


#CheckifListofIntegersisaPalindrome