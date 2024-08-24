def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [int(x) for x in input("Enter a sorted list of numbers: ").split()]
target = int(input("Enter the number to search for: "))
index = binary_search(numbers, target)
if index != -1:
    print(f"Number found at index {index}")
else:
    print("Number not found")

# Binary Search Implementation