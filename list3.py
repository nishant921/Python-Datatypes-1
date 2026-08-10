# Accessing Items from a List

# indexing
l=[1,2,3,45,6]

# positive--left to right and index starts from zero
print(l[0])
print(l[4])
# print(l[56])  error

# negative--right to left and index starts from -1
print(l[-1])
print(l[-2])
# print(l[-21])


# if   2D LIST  
l=[1,2,4,[3,5]]
print(l[-1][-2])
print(l[3][1])  #positive

l=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(l[0][0][1])


# slicing
l=[1,2,3,4,5,4,5]
print(l[0:2])
print(l[-3:])

# skips
print(l[0::2])
print(l[-5:-2:2])

# reversing list
print(l[::-1])