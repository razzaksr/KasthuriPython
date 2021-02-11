# Temple Winch system

persons=0
coach=600.0
while coach>1.0:
    weight = float(input("Enter the weight: "))
    if coach >= weight:# if weight<=coach
        print("We let you in")
        persons+=1
        coach -= weight#iteration
    else:
        print("Please wait for next coach")
else:
    print("coach has started to travel with",persons,"weight of remaining%.2f"%coach)
