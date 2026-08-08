# 2 ways to traverse a list


# itemwise
l=[1,2,3,4]
for i in l:
    print(i)



# indexwise
l=[2,3,4,56]
for i in range(0,len(l)):
    print(i,end="-")  #print index number
    print(l[i])  #print value on that index
