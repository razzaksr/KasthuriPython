# Positional Argument

credits=[45,78,12,90,3,5,10,300]
'''print(len(credits))
print(credits[7])
print(credits[len(credits)-1])'''


def shift(side,count=0):
    print(side,"shift gonna happen")
    for data in range(len(credits)):
        print(data, credits[data])

        if side == 'left':
            credits[data]<<=count
        else:
            credits[data]>>=count

        print(data,credits[data])

#shift(count=2,side='right')#positional arg



def check(beta,alpha=0):
    print("Alpha is: ",alpha,"Beta is",beta)
    print(alpha+beta)

check(12,56)
check(beta=77,alpha=10)
check(alpha=20,beta=78)
check(100)
