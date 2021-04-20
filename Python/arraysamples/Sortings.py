# sort

from array import *

save=array('d',[1.2,9.2,0.3])
kItems=[12300,8900,100,320,450,260,1200]
save.fromlist(kItems)
save.extend([1.2,8.9])

print(save)# O(1)

'''
#selection sort: O(n2)  
for select in range(len(save)):
    for com in range(select+1,len(save)):
        if save[select]>save[com]:
            save[select]*=save[com]
            save[com]=save[select]/save[com]
            save[select]/=save[com]
'''


'''
#bubble sort:O(n2)
third=0.0
for steps in range(len(save)-1):
    for bub in range(len(save)-steps-1):
        if save[bub]<save[bub+1]:
            third=save[bub]
            save[bub]=save[bub+1]
            save[bub+1]=third
'''

#insertion sort:O(n2)
for each in range(1,len(save)):
    select=save[each]
    com=each-1
    while com>=0 and select<save[com]:
        save[com+1]=save[com]
        com-=1
    save[com+1]=select



#print(save)
for data in save:
    print(data)