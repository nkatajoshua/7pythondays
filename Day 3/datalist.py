#list Data Structure
lst = [1,2,"Jo",5.6,"ucu",False]
print(lst[2])

lst2 = [3,5,[6,7,8]]
print(lst2[2])
print(lst2[2][1])

lst3 = lst + lst2
print(lst3)

lst4 = [1,4] * 5 #number of times the list is to repeat
print(lst4)

for i in lst3:
    print(i)

print (1 in lst4) #does 1 exist in the list lst4

#LIST METHODS
lst8 = [5,3,10,30,24,67,21]
lst8.append(90)
lst8.append(78)
print(lst8)

lst8.remove(78)
print(lst8)

"""lst8.clear()
print(lst8)"""

lst8copy = lst8.copy()
print(lst8copy)

nindex = lst8.index(10)
print(nindex)

lst8copy.insert(0,70)#(position,the item you want)

lst8copy.pop(5)
print(lst8copy)