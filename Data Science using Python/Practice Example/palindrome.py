# Program to check if a string
#  is palindrome or not

# change this value for a different output
my_str = 'aIbohPhoBiA'
print(my_str)

# make it suitable for caseless comparison
my_str = my_str.casefold()
print(my_str)

# reverse the string
rev_str = reversed(my_str)
print(rev_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
