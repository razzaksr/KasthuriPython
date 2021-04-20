# persons entering to attend interview panel members of 4

recruitedCount=0
while input('Is anyone there to attend the interview: ')=='yes':
    status = 0
    for hr in range(1, 5):
        each = int(input("Tell us decision: "))
        print("Decision of HR", hr, "is", each)
        status += each
    else:
        print("total result of all hr's", status)
        if status >= 2:
            print("You are recruited")
            recruitedCount+=1
        else:
            print("We'll get back to you soon")
else:
    print("Total no of recruitment",recruitedCount)
