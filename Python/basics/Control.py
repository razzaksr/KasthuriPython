#  Decision Making

print("-----------Welcome to AXIS Fund Transfer---------------")

accBal=34500

amount=float(input("Tell us amount to transfer: "))
if accBal>=amount:
    transType=input("Tell us type of transfer(NEFT,IMPS,RTGS)")
    if transType=='neft' or transType=='NEFT':
        accBal -= amount
        print(amount, "will be transferred within 3 hours")
    elif transType=='rtgs' or transType=='RTGS':
        if amount>=50000:
            accBal -= amount
            print(amount, "transferred successfully")
        else:
            print(amount,"insufficient interms of RTGS")
    elif transType=='imps' or transType=='IMPS':
        if accBal>=(amount+10):
            accBal -= (amount+10)
            print(amount, "transferred successfully through IMPS")
            print((amount+10),"debited from account")
        else:
            print(amount,"insufficient interms of IMPS")
    else:
        print("Invalid transfer type leads process termination")
else:
    print("Insufficient balance to transfer",amount)

print("Account balance is",accBal)