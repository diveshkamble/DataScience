# program calling with variable parameters

# function definition here
def printinfo(arg1,*vartuple):
    print("output :")
    print(arg1)
    print("content of variable length tuple is :")
    for i in vartuple:
        print(i,end=',')
    return

#now call printiinfo function
printinfo(10)
printinfo(70,60,50)
printinfo(70,60,'tea','samosa','chips','cake',50)

