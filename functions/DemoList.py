# list functions

'''
List is type used to store multiple data in single object
and it has following functions:
Create Read Update Delete List

append
insert
slicing operation:list[pos]

list[pos]=value

pop(pos)
remove(data)

len(list)>> count of data
max(list)>> maximum data
min(list)>> minimum data
list.count(data)>> no of occurance in list of specific data
list.index(data)
sort
reverse
'''

kItems=[12300,8900,100,320,450,260,1200]

print(kItems)
print(len(kItems))
print(max(kItems))
print(min(kItems))

print(kItems.index(320))
print(kItems.count(100))

kItems.append(320)
kItems.insert(1,260)

print(kItems)

print(kItems.count(260))

kItems.pop()

print(kItems)

kItems.pop(4)

print(kItems)

kItems.remove(260)

print(kItems)


for pos in range(2,len(kItems)):
    print(kItems[pos])
print("Iterate via for in")
for object in kItems:
    print(object)

kItems.sort()
kItems.reverse()

print(kItems)

#Slicing/Reading: [start:end:order]

print(kItems[2])
kItems[3]+=10#update

print(kItems)

print(kItems[0:3])

print(kItems[:])
print(kItems[::-1])

print(kItems)
