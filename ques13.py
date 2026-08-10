# Problem 13: Write a list comprehension to print the following matrix
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


l=[[i+j*3 for i in range(3)] for j in range(3)]
print(l)

w=[]
for i in range(3):
    row=[]
    for j in range(3):
      row.append(i*3+j)
    w.append(row)
print(w)