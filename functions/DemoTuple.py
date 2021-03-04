# Tuple(): index, count
# read, list

ware=('kasthoori',12,8.9,True,'Chennai',8.9,'Zealous',90,12)

print(ware)
'''
for pos in range(len(ware)):
    print(ware[pos])
'''

#listing
for obj in ware:
    print(obj)

#del ware[0]
#ware[1]=90#update



#slicing/reading
print(ware[:])
print(ware[::-1])
print(ware[2:4])

print(ware.count(12))
print(ware.index(8.9))

#print(max(ware))

myList=list(ware)

print(type(myList))

myList.append(12)
myList.insert(1,90)
del myList[3]

print(myList)

myList[len(myList)-1]=34

print(myList)

ware=tuple(myList)

myList.clear()

print(myList)
print(ware)