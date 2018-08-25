fo=open("c:\python\student.txt","w")# w overwrite file  a append in same file
count=0
while count<5:
    str1=input('eneter text: ')# raw input
    fo.write(str1+'\n')
    count+=1
fo.close()
print(" work done")
