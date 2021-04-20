capacity=int(input("Seating capacity: "))# 15

seat=1
while seat<=capacity:
    if seat%2!=0:
        print(seat, "Reserved online already")
        seat+=1
        continue

    else:
        # open ticket
        amt = int(input("enter the amount: "))
        if amt >= 200:
            print(seat, "has booked successfully")
            seat+=1
        else:
            print("can't travel")
    #seat+=1