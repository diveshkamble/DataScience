""" A list is a collection data type which is ordered and changeable.
In Python lists are written with square brackets.

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

print('Create a List:')
thislist = ["c++", "java", "python"]
print(thislist)

print('Display a List:')
thislist = ["c++", "java", "python",1,2,3,4,5,2.3,3.6]
print(thislist[3])
print(thislist[2:10])
print(thislist[-1:])
print(thislist[::-1])     #to print list in reverse order
print(thislist[-4:-1])# [4, 5, 2.3]

print("change the second item")
thislist = ["c++", "java", "python"]
thislist[1] = "blackcurrant"
print(thislist)


print("Using the list() constructor to make a List:")
thislist = list(("c++", "java", "python"))
print(thislist)



print("Using the append() method to append an item:")
thislist = list(("c++", "java", "python"))
thislist.append("damson")
print(thislist)

print("Using the remove() method to remove an item:")
thislist = list(("c++", "java", "python"))
thislist.remove("java")
print(thislist)

print("The len() method returns the number of items in a list:")
thislist = list(("c++", "java", "python"))
print(len(thislist))

print("Removes all the elements from the list")
thislist = list(("c++", "java", "python"))
thislist.clear()
print(thislist)

print('Returns a copy of the list')
thislist = list(("c++", "java", "python"))
print(thislist)
print(thislist.copy())

print("Returns the number of elements with the specified value ")
thislist = list(("c++", "java", "python","c++"))
print(thislist.count('c++'))

print("Add the elements of a list (or any iterable), to the end of the current list ")
fruits = ['c++', 'java', 'python']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

print("extend")
fruits = ['c++', 'java', 'python']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

#Python List index() Method
print("What is the position of the value python:")
fruits = ['c++', 'java', 'python']
x = fruits.index("python")
print(x)

print("index on same data")
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

#Python List insert() Method
print("Insert the value orange as the second elemnent of the fruit list:")
fruits = ['c++', 'java', 'python']
fruits.insert(1, "orange")
print(fruits)

#Python List pop() Method
fruits = ['c++', 'java', 'python']
fruits.pop(1)
print(fruits)

fruits = ['c++', 'java', 'python']
x = fruits.pop(1)
print(x)

#Python List reverse() Method
print("Reverse the order of the fruit list:")
fruits = ['c++', 'java', 'python']
fruits.reverse()
print(fruits)


'''alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)   '''


#Python List sort() Method
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

'''# A function that returns the length of the value:
def myFunc(e):
  return len(e)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)   ''''



#  ZIp function
test = zip()

# referring a zip class
print('The type of an empty zip : ', type(test))

list1 = [1,2,3,4]
list2 = [5,6,7,8]

test = zip(list1, list2)  # zip the values


print('\nPrinting the values of zip')
for values in test:
    print(values)  # print each tuples


