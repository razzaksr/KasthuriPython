#index error: list,tuple,array, str


lst=[12,'mohamed',7.8,87,6,23]

tup=(45,78,98,3,'Razak')

from array import *
arr=array('f',[1.2,5.6,8.9,12.4])

s="@Zea"


#print(lst[0],tup[3],arr[2],s[4])

try:
    index = int(input("Tell us index inorder to extract: "))
    print(lst[index], tup[index], arr[index], s[index])
except IndexError as ierror:
    print(ierror)
    print("Please provide index within ",len(s))
    index = int(input("Tell us index inorder to extract: "))
    print(lst[index], tup[index], arr[index], s[index])
finally:
    print("EXtraction done")