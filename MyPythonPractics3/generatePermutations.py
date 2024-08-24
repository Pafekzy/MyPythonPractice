from itertools import permutations

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
perms = list(permutations(numbers))
print("Permutations:", perms)


#Generate Permutations Using itertools