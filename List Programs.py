# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers 

L = [1,2,3,4,5,6]
odd=[i for i in L if i%2!=0]
even=[i for i in L if i%2==0]
print("Odd list: ",odd)
print("Even list: ",even)


# map() is a built-in function used to apply a function to every item of an iterable (like a list or input values)
L = input().split()
for i in range(len(L)):
    L[i] = int(L[i])

# How to take list as input from user
# list(map(int, input().split()))    # Integer list
# list(map(float, input().split()))  # Float list
# list(input())                      # Character list
# input().split()                    # String list
L2 = list(input("Enter elements: "))
print(L2)
L3 = list((input("Enter elements: ").split()))
print(L3)

# L = list(map(datatype, input().split()))
L4=list(map(int,input("Enter Elements: ").split()))
L5=list(map(float,input("Enter Elements: ").split()))
print(L4)
print(L5)

