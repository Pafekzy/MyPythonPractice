def is_balanced(s):
    stack = []
    matching_parentheses = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if stack == [] or matching_parentheses[char] != stack.pop():
                return False
    return stack == []

string = input("Enter a string of parentheses: ")
print("Balanced:", is_balanced(string))


#Check Balanced Parentheses Using Stack