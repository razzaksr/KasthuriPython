# Member Operator : in, not in

'''
Bulk data storage objects are: key/index

index always starts with 0

static/fixed within the execution:
tuple>> (12,45,'razak',5.6)
0,1,2,3

dynamic: it also contains index like tuple
list>> [data1,data2,.......]

dict>> {key:value}

'''


disney=('batman','justice league','shazam')
marvel=['iron man','captain america','vision','hulk']
indian={"tamil":"robot","telugu":"bahubali",'hindi':'krish',5:'luficifer'}

print(disney)
print(marvel)
print(indian)

print('super man' in disney)
print('Winter Solider' not in marvel)
print('raone' in indian)# key checking
print('raone' in indian['hindi'])# value checking
print(indian['hindi'])