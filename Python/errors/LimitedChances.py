# no of limited chances

from array import *
arr=array('i',[98,23,78,45,24,56,13,45,83,45,13,67])

def extract(index,limit=1):
    try:
        print(arr[index])
    except IndexError as ierror:
        print(ierror)
        limit+=1
        if limit<=3:
            extract(int(input("Tell us index: ")),limit)
        else:
            return
        #print(arr[int(input("Tell us index: "))])


extract(int(input("Tell us index: ")))