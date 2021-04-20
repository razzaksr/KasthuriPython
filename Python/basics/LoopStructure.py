'''
Looping statements:
1. Repeatation: reduce time complexity by avoid to write same code again and again
2. Series, Patterns: eg: 1,2,4,8,16,32,....., 2,4,6,8,10......., 1,3,5,7,9,11,.......,
	1
	12
	123
	1234
	12345

start		initialization
step up		iteration
end		condition

while
syntax:
#init
while condition:
	#body of loop
	#iteration

for in range
syntax:
for obj in range(init,cond,iter):
	#body of loop


for in
syntax:
for object in sourcesStructure:
	#body
'''

#eg:timing based sale

timing=11.00

while timing<=11.41:
    print("Entry number: %.2f"%timing)
    #printf("Entry number: %f",timing)
    quan = int(input("Tell us how many mobiles you required: "))
    if quan > 0:
        amt = (quan * 9000)
        amt += (amt * 0.06)
        print("Your order placed and invoice amount is", amt)
        timing += 0.05
    else:
        print("Invalid Quantity")
    '''quan = int(input("Tell us how many mobiles you required: "))
    if quan > 0:
        amt = (quan * 9000)
        amt += (amt * 0.06)
        print("Your order placed and invoice amount is", amt)
    else:
        print("Invalid Quantity")
    timing+=0.05'''