# Operator overloading:
# overload/ define the custom logic when operator comes between class object

from oop.Constrtuctors import Account

alpha=20
beta=89

print(alpha+beta)


acc1=Account("Mohamed",23432234323,9800.3)
acc2=Account("Rasheedha",876567767433,1800.3)

acc1<<2000
acc2>>1000

print(acc1)
print(acc2)
