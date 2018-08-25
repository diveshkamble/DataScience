fo=open(r"c:\python\student.txt","r")
str1=fo.read(10) #read upto 10 character
print(str1)
# close opened file
fo.close()
print ("work done")
