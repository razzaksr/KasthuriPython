# Decision Making: if else

'''
if condition:
    # true block
elif condition:
    # elif true
else:
    #false
'''

#simple example
print("-------------TNSTC Bus booking---------------")
fare=int(input("Tell us amount: "))
if fare >= 300 and fare <500:
    print("You can travel in Ultra Delux")
elif fare >=100 and fare<300:
    print("You can travel in Ordinary")
elif fare>=500:
    print("You can travel in Sleeper")
else:
    print("Amount insufficient to travel")