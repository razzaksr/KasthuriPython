# Dictionary {key:value,key:value,key:value}

'''
key: shouldn't duplicate
create: obj[key]=value
read: obj[key]
update: obj[key]=value
delete: del obj[key]
obj.pop(key)
list:
keys()
values()
items()
'''

amazeUsers={"razak":12900,"rasheedha":7600,"mohamed":11000,"kasthoori":12900,987654:1200}

#list
print(amazeUsers)

print(amazeUsers.keys())

print(amazeUsers['mohamed'])


for key in amazeUsers.keys():
    #print(key, amazeUsers[key])
    print(key, amazeUsers.get(key))

#create>> insert
amazeUsers['sabari']=23900

print(amazeUsers)

#update
amazeUsers['rasheedha']=12800

print(amazeUsers)

#list via values
print(amazeUsers.values())

#list via items
for pair in amazeUsers.items():
    print(pair)

#deletion
amazeUsers.pop('razak')

print(amazeUsers)

amazeUsers.popitem()
print(amazeUsers)

del amazeUsers['kasthoori']
print(amazeUsers)

mineList=list(amazeUsers)
print(mineList)

mineValList=list(amazeUsers.items())
print(mineValList)
print(mineValList[0][1])




