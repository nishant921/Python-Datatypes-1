# Problem 11: Write a program that can perform union operation on 2 lists
# Example:

# Input:
# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:

# [1,2,3,4,5,7,8]

l1=list(map(int,input("Enter Elements: ").split()))
l2=list(map(int,input("Enter Elements: ").split()))
result=[]
for i in l1:
    if i not in result:
        result.append(i)
for j in l2:
    if j not in result:
        result.append(j)
print(result)

# Here:
# | = Union operator for sets.
print(list(set(l1) | set(l2)))


# method 2
l1 = [1,2,3,4,5,1]
l2 = [2,3,5,7,8]

result = []
[result.append(i) for i in l1+l2 if i not in result]
print(result)