# Problem 14: Write a list comprehension that can transpose a given matrix

# import numpy as np
# matrix = np.array([
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ])
# print(matrix.T)

matrix =[
[1,2,3],
[4,5,6],
[7,8,9]
]
trans=[list(i)for i in zip(*matrix)]

print(trans)


