#series with controls

# fibonacci series of 10: 0 1 1 2 3 5 8 13 21 34

count=int(input("tell us how many fibo number you wish: "))

num1=0
num2=1

if count>0:#positive number
    if count==1:
        print(num1)
    elif count==2:
        print(num1)
        print(num2)
    elif count>2:# count=8
        print(num1)
        print(num2)
        limit=count-2# 8-2=6
        while limit>0:#for fibo in range(1, limit):
            join = num1 + num2
            num1 = num2
            num2 = join
            print(num2)
            limit-=1
else:print("Invalid range to find fibonacci")