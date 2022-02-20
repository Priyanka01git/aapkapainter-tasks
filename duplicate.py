#first occurrence of a duplicate in a given array of integers
list = [1,2,3,2,1]
mylist = []
for i in range(len(list)):
    if list[i] in mylist:
        print(list[i])
        break
    else:
         mylist.append(list[i])