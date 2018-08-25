        #Python For Loops
print ('simple for loop')
fruits = ["c++", "java", "python"]
for x in fruits:
  print(x) 


#The break Statement
print ('***break****')
fruits = ["c++", "java", "python"]
for x in fruits:
  if x == "java":
    break
  print(x)

#The continue Statement
print ('***continue****')
fruits = ["c++", "java", "python"]
for x in fruits:
  if x == "java":
    continue
  print(x) 

#The range() Function
print ('***range****')
for x in range(6): #  from 0 to 5
  print(x) 

#range(2, 6)
print("start and end range()")
for x in range(2, 6): # from 2 to 5
  print(x)

#Increment the sequence with 3 (default is 1):
print("start and end and increment range()") 
for x in range(2, 30, 3):
  print(x)

#Recursion
  print('Recursion')
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
