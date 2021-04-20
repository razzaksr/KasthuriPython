# bus reservation


capacity=int(input("Seating capacity: "))# 15

#seat=1
for seat in range(1,capacity+1):#while seat<=capacity:
    if seat%2!=0:
        print(seat, "Reserved online already")
        break

    else:
        # open ticket
        amt = int(input("enter the amount: "))
        if amt >= 200:
            print(seat, "has booked successfully")
        else:
            print("can't travel")
    #seat+=1