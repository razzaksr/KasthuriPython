# Clearance sale

stock=int(input("TEll us how many items available: "))
price=int(input("Price of panasonic AC: "))
daily=0
net=0
day=1
while day<=5 and stock>0:
    qty = int(input("TEll us quantity sold "+str(day)))
    if qty <= stock:
        daily = qty * price
        stock -= qty
        print(qty, "of panasonic AC's purchased for ",daily)
        net+=daily
    else:
        print("insufficient stock",stock)
    price-=(price*0.07)
    day+=1
else:
    print("Total sale collection:",net)
    print("Stock available:",stock)