# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:
# ['1ac21', '23fg', '456', '098d','1','kls']
# Output:
# ['456', '23fg', '1ac21', '1', 'kls', '098d']



list1 = ['1ac21', '23fg', '456', '098d', '1', 'kls']

temp = []

for s in list1:
    product = 1

    for ch in s:
        if ch.isdigit():
            product *= int(ch)

    temp.append([product, s])

temp.sort(reverse=True)
print(temp)

result = [item[1] for item in temp]

print(result)