def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

tuples_list = [(1, 2), (3, 1), (4, 5)]
print("Sorted list of tuples:", sort_tuples(tuples_list))



# Sorting List of Tuples by Second Element