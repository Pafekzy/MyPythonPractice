def bubble_sort(number_list):
    list_length = len(number_list)
    for iteration in range(list_length):
        for index in range(0, list_length - iteration - 1):
            if number_list[index] > number_list[index + 1]:
                number_list[index], number_list[index + 1] = number_list[index + 1], number_list[index]
    return number_list

user_input = input("Enter a list of integers separated by spaces: ")
number_list = [int(x) for x in user_input.split()]
sorted_numbers = bubble_sort(number_list)
print("Sorted list:", sorted_numbers)

#TASK;  List Sorting without sort() Function