def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    longest = s[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub
    return longest

text = input("Enter a string: ")
print("Longest palindrome substring:", longest_palindrome(text))


#Longest Palindrome Substring