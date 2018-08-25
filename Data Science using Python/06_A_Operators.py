''' python arithmetic operator '''

x=5
y=3

print(x + y)
print(x - y)
print(x * y)
print(x / y)# returns float division
print(x % y)
print(x ** y)# gives x^y
print(x//y) # returns int division

# Python Assignment Operators
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x%=3
print(x)

x = 5
x//=3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x <<= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x >>= 3
print(x)




#Python Comparison Operators

x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3

x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3

x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3

x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3


x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3

# Python Logical Operators

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

x = 5
print(x > 3 or x < 4)
'''returns True because one of the conditions are true
(5 is greater than 3, but 5 is not less than 4)
'''

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

# Python Identity Operators
'''Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location:'''

x = ["c++", "java"]
y = ["c++", "java"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
""" returns False because x is not the same object as y,
even if they have thew same content
"""
print(x == y)
""" to demonstrate the difference betweeen "is" and "==":
this comparison returns True because x is equal to y
"""


x = ["c++", "java"]
y = ["c++", "java"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
''' returns True because x is not the same object as y,
even if they have the same content
'''
print(x!=y)
''' to demonstrate the difference betweeen "is not" and "<>":
this comparison returns False because x is equal to y
'''


'''Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:
'''

x = ["c++", "java"]
print("java" in x)
# returns True because a sequence with the value "java" is in the list

x = ["c++", "java"]
print("pinec++" not in x)
# returns True because a sequence with the value "pinec++" is not in the list


