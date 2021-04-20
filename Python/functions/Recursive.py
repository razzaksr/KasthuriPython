# function calls by itself

def ask():
    print("Asking for jio network")

def enquiry(begin=1):
    if begin>10:
        return
    print("Enquiry for updating new skillset")
    begin+=1
    enquiry(begin)#recursive





#main section
ask()
enquiry()



limit=int(input("Limit of fibonacci: "))#10
num1=0
num2=1
if limit>=2:
    print(num1)
    print(num2)
    for count in range(3,limit+1):
        sum=num1+num2
        print(sum)
        num1=num2
        num2=sum