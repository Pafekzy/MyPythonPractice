def common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
print("Common elements:", common_elements(list1, list2))

#Common Elements in Two Lists