fo=open(r"c:\python\student.txt","a")#append
str1=input(" enter text : ")
fo.write(str1)
fo.write('\n we are using file handling')
fo.close()

print(" work done")
