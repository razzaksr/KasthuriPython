# multi level inheritance:
from oop.Constrtuctors import Account


class DebitCard(Account):
    def __init__(self,name="",num=0,bal=0.0,atm=0):
        self.__aPin=atm
        super(DebitCard, self).__init__(name,num,bal)
    def credit(self):
        tmp=int(input("Tell us ATM pin inorder to deposit: "))
        if tmp==self.__aPin:
            amt=int(input('Tell us amount to deposite: '))
            self<<amt
        else:
            print("invalid pin")
    def debit(self):
        tmp = int(input("Tell us ATM pin inorder to withdraw: "))
        if tmp==self.__aPin:
            amt=int(input('Tell us amount to withdraw: '))
            self>>amt
        else:
            print("invalid pin")


class Wallet(DebitCard):
    def __init__(self,name="",num=0,bal=0.0,pin=0,upipin=0):
        self.__upiPin=upipin
        super(Wallet, self).__init__(name,num,bal,pin)
    def __xor__(self, other):
        amt=int(input("Tell us amount: "))
        tmp=int(input("Type the UPI Pin number: "))
        if self.getAccBal()>=amt and tmp==self.__upiPin:
            self.setAccBal(self.getAccBal()-amt)
            other.setAccBal(other.getAccBal()+amt)
            print(self.getHolder(),"has transferred",amt,"to",other.getHolder())
        else:
            print(self.getHolder(),"failed to transfer the",amt)

wal1=Wallet("kasthuri",87656789,12900.3,1122,112233)
wal2=Wallet("mohamed",4567898767,3200.4,9988,123456)

wal2.debit()

print(wal2)

wal1^wal2

print(wal1,wal2)