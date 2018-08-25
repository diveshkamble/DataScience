#  Python Tuples 
''' Ordered--unchangeable--written with round brackets'''

#Create a Tuple:
thistuple=("c++","java","python")
print (thistuple)

#Return the item in position 1:
thistuple = ("c++", "java", "python")
print(thistuple[1])

#Return the item in range:
thistuple = ("c++", "java", "python",1,2,3,4,5)
print(thistuple[1:6])


#You cannot change values in a tuple:
"""
thistuple = ("c++", "java", "python")
thistuple[1] = "blackcurrant"# it gives an error bcoz tuple is unchangeable
    # the value is stille the same:
print(thistuple)

"""

    #The tuple() Constructor
#Using the tuple() method to make a tuple:
thistuple = tuple(("c++", "java", "python"))
print(thistuple)

#The len() method returns the number of items in a tuple:
thistuple = tuple(("c++", "java", "python"))
print(len(thistuple))

#nested tuples
month=("jan" ,"feb" ,"march")
#month[1]="Dec"
print(month)
month=month,("Mon","tue","wed")
print(month)

# built in functions
marks=(45,55,56,38,78,98,100)
print("Maximu marks : ",max(marks))
print("Minimum marks : ",min(marks))
print("Type marks : ",type(marks))
print("Sorted marks : ",sorted(marks))
print("Sum marks : ",sum(marks))

#repeatation operator
repeat=('python',)*4
print(repeat)
print(type(repeat))
