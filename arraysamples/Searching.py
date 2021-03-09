# searching via linear and binary

from array import *

ware=array('i',[12300,8900,100,320,450,260,1200])

# linear search
def linear(data):
    for pos in range(len(ware)):
        if ware[pos] == data:
            return pos
    else:return -1


desired=int(input("Tell us desired data to get position: "))
#print(ware.index(desired))

#print(linear(desired))


def binary(start,end):
    mid=(start+end)//2
    if desired==ware[mid]:
        return mid
    elif desired>ware[mid]:
        return binary(mid+1,end)
    elif desired<ware[mid]:
        return binary(start,mid)
    else:
        return -1

def selection():
    for select in range(len(ware)):
        for com in range(select + 1, len(ware)):
            if ware[select] > ware[com]:
                ware[select] ^= ware[com]
                ware[com] ^= ware[select]
                ware[select] ^= ware[com]

selection()
print(ware)
print(binary(0,len(ware)-1))
