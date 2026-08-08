# Editing items in list

# s[0]=34 you cannot do this in string as it is immutable but in list you can change items directly

# editing with indexing
l=[1,2,3,4,5]
l[0]=2
print(l)
# editing with slicing
l[2:]=[100,200,300]
print(l)



# Deleting items in list
l=[1,2,3,4,5]

# del
# del l  # it's not deletion at meomory level it doesnt delete
del l[-1]
print(l)
del l[1:3]
print(l)


l=[1,2,3,4,5]
# remove(): item deletion happens on value base not index help in removing items from dynamic data genertion
# l.remove(10) error value error
l.remove(5)
print(l)


l=[1,2,3,4,5]
# pop(): 1. can delete a iteam from a particular index
#  2. without index : delete last element default
l.pop()
print(l)
l.pop(0)
print(l)


# clear()= remove all elements make the list empty
l.clear()
print(l)
