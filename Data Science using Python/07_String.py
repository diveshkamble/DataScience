#  Get the character at position 1
print('Get the character at position 1')
a = "hello"
print(a[1])
print(a[-1])

# Substring. Get the characters from position 2 to position 5
print('Substring. Get the characters from position 2 to position 5')
b = "world"
print(b[2:5])

# The strip() method removes any whitespace from the beginning or the end
print('The strip() method removes any whitespace from the beginning or the end')
a = "Hello, World! "
print(a.strip())


#  The len() method returns the length of a string
print('The len() method returns the length of a string')
a = "Hello, World!"
print(len(a))

# The lower() method returns the string in lower case
print('The lower() method returns the string in lower case')
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case
print('The upper() method returns the string in upper case')
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string
print('The replace() method replaces a string with another string')
a = "Hello, World!"
print(a.replace("H", "J"))


''' The split() method splits the string into substrings
if it finds instances of the separator
'''
print('split() method')
a = "Hello , World!"
b = a.split(",")
print(type(b))
print(b)

# COMMAND LINE STRING INPUT

print("Enter your name:")
x = input()
print("Hello, " + x)
