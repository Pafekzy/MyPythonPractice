def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

rows = int(input("Enter the number of rows: "))
matrix = [list(map(int, input(f"Enter row {i+1} values: ").split())) for i in range(rows)]
print("Transposed matrix:", transpose(matrix))


#Transpose of a Matrix