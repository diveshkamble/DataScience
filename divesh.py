def print_name(name):
    print("Name: "+name)
def take_name():
    name = input("Enter your name: ")
    return name
def take_age():
    age = int(input("Enter your age: "))
    return age
def print_age(age):
    print("age: ",age )
def __main__():
    name=take_name()
    print_name(name)
    age = take_age()
    print_age(age)

__main__()
