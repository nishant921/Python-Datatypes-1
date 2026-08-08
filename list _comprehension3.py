# Print a (3,3) matrix using list comprehension -> Nested List comprehension
matrix=[[row+column for row in range(1,4)] for column in range(1,4)]
print(matrix)
matrix=[[row*column for row in range(1,4)] for column in range(1,4)]
print(matrix)

# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print([i*j for i in L1 for j in L2])
