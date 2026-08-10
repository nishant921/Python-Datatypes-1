# creating list

# 1. empty list
l=[]
print(l)

# 2. 1D list
l=[1,2,3,4,5]  #also homo list as all elements are from same data class
print(l)

# 3.  2D list
l=[1,2,3,[4,5]]   #int and list so it is hetero
print(l)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 4.  3D list
l=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(l)

# heterogenous list
l=[1,True,2.3,'nishant',2+5j]
print(l)

# using type conversion
s="nishant"
print(list(s))