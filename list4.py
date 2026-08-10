# adding items to list

#append() =  add the value(single item) in the end of list
l=[1,23,4,43]
l.append(7)
print(l) 
l.append(True)
print(l) 
l.append([2.3,3.3]) #it will add the list as an one item
print(l) 

# extend() = adding multiple items in one go but should be in bracket[]
l.extend([2,4,5,4,'nishn'])
print(l) 

l.extend('delhi')  # if you write in list["delhi"] it will be added normally other wise: if you add like string ("dchsbh")
#brekdown the string delhi and add each char into list
# it will breakdown and add multiple items 
print(l) 


# insert() = to add item in list at any position
l.insert(1,'nish')
print(l) 