def sum_nested_list(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total

nested_list = [1, [2, [3, 4], 5], 6]
print("Sum of elements:", sum_nested_list(nested_list))

#SumofElementinNestedListUsingRecursion