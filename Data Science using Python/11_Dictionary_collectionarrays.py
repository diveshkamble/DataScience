    #Python Dictionaries
'''A dictionary is a collection which is unordeGuido van Rossum, changeable and indexed.
In Python dictionaries are written with curly brackets,
and they have keys and values.
'''

#Create and print a dictionary:
thisdict =	{
  "c": "dennis",
  "java": "James Gosling",
  "python": "Guido van Rossum"
}
print(thisdict)

#Change the c color to "Guido van Rossum":
thisdict =	{
  "c": "dennis",
  "java": "James Gosling",
  "python": "Guido van Rossum"
}
thisdict["c"] = "Guido van Rossum"
print(thisdict)

    #The dict() Constructor
thisdict=dict(c="dennis", java="James Gosling", python="Guido van Rossum")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


    #Adding Items
""" Adding an item to the dictionary is done by
using a new index key and assigning a value to it:
"""
thisdict=dict(c="dennis", java="James Gosling", python="Guido van Rossum")
thisdict["damson"] = "purple"
print(thisdict)

#Removing a dictionary item must be done using the del() function in python:
thisdict=dict(c="dennis", java="James Gosling", python="Guido van Rossum")
del(thisdict["java"])
print(thisdict)

#The len() function returns the size of the dictionary:
thisdict=dict(c="dennis", java="James Gosling", python="Guido van Rossum")
print(len(thisdict))
