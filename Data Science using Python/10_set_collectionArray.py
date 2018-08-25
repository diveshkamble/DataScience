    #Python Sets
# Unordered--unindexed--written in culry brackets

#Create a Set:
thisset = {"c++", "java", "python"}
print(thisset)
''' Note: the set list is unordered,
so the result will display the items in a random order.
'''

'''#Display a Set:
thisset = {"c++", "java", "python"}
print(thisset[0:2]) # unindexed hence gives error
'''
#Using the set() constructor to make a set:
thisset = set(("c++", "java", "python"))
print(thisset)
''' Note: the set list is unordered, so the result will display
the items in a random order.
'''

#Using the add() method to add an item:
thisset = set(("c++", "java", "python"))
thisset.add("damson")
print(thisset)

#Using the remove() method to remove an item:
thisset = set(("c++", "java", "python"))
thisset.remove("java")
print(thisset)

#Using the len() method to return the number of items:
thisset = set(("c++", "java", "python"))
print(len(thisset))

#nested set
thisset1 = {"c++", "java", "python"}
thisset2=thisset1,{1,2,3.4,4E5,7j}
print(thisset2)

