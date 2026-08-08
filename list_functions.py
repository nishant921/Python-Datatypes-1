# List Functions

# common function:
# len/min/max/sorted

l=[2,4,7,5,2,10]

print(len(l))
print(min(l)) #works for homo type         
print(max(l)) #works for homo type         
print(sorted(l))
print(sorted(l,reverse=True))
sorted(l,reverse=True) #no permanent changes
print(l)


l=[2,4,7,5,2,10,10,1,2,3,4,1,2]
# count()
print(l.count(2))

# index= if multiple same value gives index of first occurenece of that item
print(l.index(2))


# reverse =  permanent operation change the list completely 
l.reverse()
print(l)


# sort (vs sorted)= permanent change the list
l=[2,4,7,5,2,10]
print(l)
print(sorted(l))
print(l)

l.sort(reverse=True)
print(l)


# copy() : create a copy of list in memory--shallow copy
l=[2,4,7,5,2,10]
print(id(l))
l1=l.copy()
print(l1)
print(id(l1))
