filenames = input("Enter filenames separated by spaces: ").split()
total_lines = 0
for filename in filenames:
    with open(filename, 'r') as file:
        total_lines += sum(1 for line in file)
print("Total lines across all files:", total_lines)


# Count Total Lines Across Multiple Files