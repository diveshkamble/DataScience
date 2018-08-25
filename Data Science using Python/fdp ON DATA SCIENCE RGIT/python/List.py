# remove duplicates
lst=[11,8,5,21,5,11,28,8]
print(lst)
new_lst=list()
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
