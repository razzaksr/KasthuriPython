#  flipkart order

accountBal=8760.45
UpiPin=776677

proPrice=int(input("Tell us product price: "))# 4300

if proPrice<500:
    proPrice+=50
    print("Shipping charges 50rs added",proPrice)

payMethod=input("Tell us payment option(COD,debit,UPI,EMI): ")# debit

if payMethod == 'COD' or payMethod=='cod':
    print("Order Placed",proPrice)
elif payMethod == 'debit' or payMethod=='DEBIT':
    cardType=input("Tell us card type(visa/master/rupay): ")# visa
    if cardType=='visa' or cardType=='VISA':
        proPrice-=(proPrice*0.08)#
        print("8 percent cash back applied")
    elif cardType=='master' or cardType=='MASTER':
        proPrice-=(proPrice*0.02)
        print("2 percent cash back applied")
    # check with account balance
    if proPrice<=accountBal:
        accountBal-=proPrice
        print("Order Placed",proPrice)
    else:
        print("Order Not placed",proPrice)
elif payMethod=='upi' or payMethod=='UPI':
    pin=int(input("Enter the UPI PIN: "))
    if UpiPin==pin:
        if accountBal>=proPrice:
            accountBal-=proPrice
            print("Order placed",proPrice)
        else:
            print("Order Not placed due to insufficient balance for",proPrice)
    else:
        print("Order",proPrice,"not place due to wrong pin")
elif payMethod=='emi' or payMethod=='EMI':
    if proPrice>=3000:
        bank=input("Tell us EMI bank: ")
        if bank == 'icici' or bank=='axis' or bank=='hdfc':
            print("order",proPrice,"placed")
        else:
            print("order",proPrice,'not placed due to unsupported bank')
    else:
        print("order", proPrice, 'not placed due to emi criteria')
else:
    print('invalid payment option')