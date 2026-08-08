# List Comprehension: List Comprehension provides a concise way of creating lists.

# **** newlist = [expression for item in iterable if condition == True]

# Advantages of List Comprehension

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.


# without list comprehension

# Add 1 to 10 numbers to a list
l=[]
for i in range(1,11):
    l.append(i)
print(l)


# with list comprehension
l=[i for i in range(1,11)]
print(l)
