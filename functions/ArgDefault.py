# default argument


def calculateTds(amount=0):
    if amount==0:
        print('No TDS since You are not earned anything')
        return
    elif amount>30000:
        print("TDS is 10 Percent")
        amount-=(amount*0.100)
    else:
        print("TDS is 7.5 Percent")
        amount-=(amount*0.075)
    print(amount,"is take home after TDS deduction")



calculateTds(42000)
calculateTds(18000)
calculateTds()