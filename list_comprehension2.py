# scalar multiplication on a vector

# without

v=[1,3,4]
s=4
l1=[]
for i in v:
    l1.append(i*s)

print(l1)


# with comprehension
v=[1,3,4]
s=4
print([i*s for i in v])

# Add squares
v=[1,3,4]
v2=[i**2 for i in v]
print(v2)

# Print all numbers divisible by 5 in the range of 1 to 50
print([i for i in range(1,51) if i%5==0])

# find languages which start with letter p
languages = ['java','python','php','c','javascript']
print([language for language in languages if language.startswith('p')])

# Nested if with List Comprehension
# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a' 
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith("a") ])