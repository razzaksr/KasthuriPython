# Constructor:def __inti__

class Account:

    #constructor
    def __init__(self,name="",num=0,bal=0.0):
        print("Constructor called")
        self.__holder=name
        self.__accNum=num
        self.__accBal=bal

    #overloaing operator

    # obj<<obj:accountObject<<deposite_value
    def __lshift__(self, other):
        self.__accBal+=other
        print(other,"credited to your account",self.__accNum)
    # obj>>obj:accountObject>>debitValue
    def __rshift__(self, other):
        if self.__accBal>=other:
            self.__accBal-=other
            print(other,"debited from account",self.__accNum)
        else:
            print(self.__accNum,"has insufficient amount")


    def __str__(self):
        return self.__holder+" "+str(self.__accNum)+" "+str(self.__accBal)+"\n"


    def setHolder(self,name=""):self.__holder=name
    def getHolder(self):return self.__holder
    def setAccNum(self,num=0):self.__accNum=num
    def getAccNum(self):return self.__accNum
    def setAccBal(self,bal=0.0):self.__accBal=bal
    def getAccBal(self):return self.__accBal


'''acc1=Account()
acc1.setAccNum(87654567343)
acc1.setAccBal(3400.5)
acc1.setHolder("Kasthoori")
print(acc1)

acc2=Account("Mohamed",23432234323,9800.3)
print(acc2.getAccBal())'''

