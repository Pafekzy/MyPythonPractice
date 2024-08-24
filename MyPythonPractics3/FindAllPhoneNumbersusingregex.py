import re

text = input("Enter a string containing phone numbers: ")
phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
print("Phone numbers found:", phone_numbers)

# Find All Phone Numbers Using Regex