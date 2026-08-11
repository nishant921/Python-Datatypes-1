rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter Elements: ").split()))
    if len(row) != cols:
        print("Invalid number of elements!")
        break
    matrix.append(row)

print(matrix)


# 3d
layers = int(input("Enter layers: "))
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

arr = []

for l in range(layers):
    matrix = []

    for r in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    arr.append(matrix)

print(arr)