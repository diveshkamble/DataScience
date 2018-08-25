from random import *
print (" ramdom no between 0-1")
print(random()) # generate random number between 0-1
print (" ramdom no between 1-100")
print(randint(1,100)) # generate random number between 1-100
print (" floating no between 1-10")
print(uniform(1,10)) # generate random floating number between 1-10


# we can shuffle a list with thid code
items=[1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print (" shufflled number")
print(items)

# To pick a random number from a alist
items=[1,2,3,4,5,6,7,8,9,10]
print (" pick 1 random number from items")
x=sample(items,1) # pick 01 random items from list
print("x=",x)
print(x[0])# elements of above statements

print (" pick 4 random number from items")
y=sample(items,4)# pick 4 random items from list
print("y=",y)
