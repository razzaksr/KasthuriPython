# array creation
#creation syntax: object=array('type',[])

# i,f,s,d
'''
import array
obj=array.array('i',[])
obj.append(12)
obj.append(90)
print(obj)'''

'''
import array as ar
obj=ar.array('i',[])
obj.append(12)
obj.append(90)
print(obj)'''

from array import *

obj=array('i',[])
obj.append(12)
obj.append(90)
print(obj)