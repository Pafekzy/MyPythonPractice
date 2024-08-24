def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
print("List without duplicates:", remove_duplicates(numbers))
