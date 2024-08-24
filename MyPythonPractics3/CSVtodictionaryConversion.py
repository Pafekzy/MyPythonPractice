import csv

filename = input("Enter the CSV filename: ")
data = {}
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        key = row[0]
        values = row[1:]
        data[key] = values
print(data)

#CSV to Dictionary Conversion