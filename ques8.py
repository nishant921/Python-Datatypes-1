# Problem 8: Split String of list on K character.

# Example :
# Input:
# ['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:
# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

list1=list(input("Enter String of List: ").split(","))
k=input("Enter Charcter from you want split: ")
l=[]
for i in list1:
    l.extend(i.split(k))
print(l)