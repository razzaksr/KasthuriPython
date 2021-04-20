# crudl

from array import *

save=array('d',[1.2,9.2,0.3])

print(save)

save.append(4.5)
save.insert(2,5.6)

print(save)

kItems=[12300,8900,100,320,450,260,1200]

save.fromlist(kItems)

print(save)

save.extend([1.2,8.9])

print(save)

#read/slicing
print(save[2])
print(save[:])
print(save[::-1])
print(save[3:8])

#update
save[4]-=(save[4]*0.045)
print(save)

#delete
save.pop()
save.pop(3)
save.remove(260.0)
del save[1]

print(save)

print(len(save))
print(max(save))
print(min(save))

save.reverse()

#print(save)

#listing
'''
O(n)>>O(10)
for index in range(len(save)):
    print(save[index])
'''

for data in save:
    print(data)

