def subsets(s):
    if not s:
        return [[]]
    rest_subsets = subsets(s[1:])
    return rest_subsets + [[s[0]] + subset for subset in rest_subsets]

set_elements = input("Enter elements of the set separated by spaces: ").split()
print("Subsets:", subsets(set_elements))


#Find All Subsets of a Set Using Recursion