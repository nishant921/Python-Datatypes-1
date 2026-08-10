# Problem 1: Combine two lists index-wise(columns wise)
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given List:

# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
# Output:

# [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]

# using zip only there're equal numbers of items
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
# list3=list(zip(list1,list2)) gives tuple
list_c = [list(i) for i in zip(list1,list2)]
print(list_c)



# without zip
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an",1,2]

list3 = []
if len(list1)>=len(list2):
    for i in range(len(list1)):
        if i<len(list2):
            list3.append([list1[i],list2[i]])
        else:
            list3.append([list1[i]])
        # list3.append([list1[i], list2[i]])
else:
    for i in range(len(list2)):
        if i<len(list1):
            list3.append([list1[i],list2[i]])
        else:
            list3.append([list2[i]])

print(list3)


# Another way 
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an", 1, 2]

result = []

max_len = max(len(list1), len(list2))

for i in range(max_len):
    temp = []

    if i < len(list1):
        temp.append(list1[i])

    if i < len(list2):
        temp.append(list2[i])

    result.append(temp)

print(result)
