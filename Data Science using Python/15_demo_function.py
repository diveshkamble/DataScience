#   Python Functions
print("****Creating a Function")
def my_function():
  print("Hello from a function")

# calling a function
print("***function calling")
my_function()


#Parameters passing
print("\n")
print("*****Parameters passing")
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



#Default Parameter Value
print("**Default Parameter Value")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Return Values
print("Return Values")
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
