# What are Lists: List is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.
#  ex: l = ['hello',300,'are',['you',4,5,4,'&']] index = hello at 0=l[0]

# Array Vs Lists
#    1. Fixed Vs Dynamic Size
#    2. Convenience -> homogennous(same data type) vs  Hetrogeneous(different data type)
#    3. Speed of Execution -> faster execution vs slower execution
#    4. Memory -> less space occupation vs more space occupation

# Disadvantages of Python Lists:
# Slow
# Risky usage
a=[1,2,3]
b=a  #when a=b they are now on same meomory location that's why when we change a and doesn't change b it still get the changes as list is mutable
b=a.copy() #use copy function for preventing risky usage
print(a)
print(b)
a.append(4)
print(a)
print(b)

# eats up more memory


L = [1,2,3]
# How lists are stored in memory
print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))


# Characterstics of a List
# Ordered
l=[1,2,3]
l2=[3,2,1]
print(l==l2)

# Changeble/Mutable

# Hetrogeneous:list can have diff data types in single list

# Can have duplicates
l=[1,2,2,1]

# are dynamic

# can be nested
l=[1,43,32,[2.1,2.2,3.2]]

# items can be accessed
print(l[2])

# can contain any kind of objects in python
# can contain function as it is also objects
l=[1,2,type,print,True,input]
print(l)

