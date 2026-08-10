l=[6,7,8,9]
l1=[1,2,3,4]
print(l*2)
# print(l-l1)
print(l+l1)
print(l>l1)
print(l!=l1)
print(l in l1)
print(l not in l1)

l=[1,2,3]
l2=[4,4]
print(l and l2)
print(l or l2)
print(not l2)
l=[1,2,3]
l2=l
print(l is l2)
l2=l.copy()
print(l is l2)
print(l is not l2)