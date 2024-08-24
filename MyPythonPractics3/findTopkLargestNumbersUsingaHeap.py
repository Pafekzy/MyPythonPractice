import heapq

def find_top_k_largest(numbers, k):
    return heapq.nlargest(k, numbers)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
k = int(input("Enter the value of k: "))
print(f"Top {k} largest numbers:", find_top_k_largest(numbers, k))


# Find Top k Largest Numbers Using a Heap