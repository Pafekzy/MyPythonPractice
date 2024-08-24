def unique_elements(lst):
    return list(set(lst))

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
print("Unique elements:", unique_elements(numbers))


#Unique Elements from a List