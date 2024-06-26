#mutable and immutable
#can be changed
lit = [1,2,3,4,5]
lit[0]=10
print(lit[1])

#can't be changed
tple =(1,2,3,4)
tple[1] = 10
print(tple[1])

#non sequence
set ={1, 2, 3, 4}
print(set[0])

group = range(1,10,2)#(startnumber,stopnumber,stepstoskip)