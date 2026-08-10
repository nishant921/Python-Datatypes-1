# Problem 4: Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:

# Input:
# list1 = [1,2,3,4,5,6]
# Output:
# [1,3,6,10,15,21]

list1=list(map(int,input("Enter Elements: ").split()))
l=[]
total=0

for i in list1:
    total+=i
    l.append(total)
print(f"Running sum list: {l}")


# pure list comprehension
list1 = list(map(int, input("Enter Elements: ").split()))
result = [sum(list1[:i+1]) for i in range(len(list1))]
print(result)