#Hybrid Inheritance
from oop.ClassSample import Account


class NetBanking(Account):
    def __mul__(self, other):#obj*['EB',120]
        if self.accountBal>=other[1]:
            self.accountBal-=other[1]
            print(other[0],"bill",other[1]," has paid successfully")
        else:
            print("insufficient to pay bill",other[1],"to",other[0])

class Card(Account):
    def __init__(self,pin=0):
        self.__pin=pin
    def __and__(self, other):#obj&9982
        cpin=int(input("Enter the current PIN inordeer to validate: "))
        if cpin==self.pin:
            self.pin=other
            print("pin has changed for the account",self.accountNo)
        else:
            print("Unauthorised access")

class User(Card,NetBanking):
    def __init__(self,num=0,bal=0.0,pin=0):
        self.accountNo=num
        self.accountBal=bal
        self.pin=pin
        #super(User, self).__init__(pin)
    def __sub__(self, other):#obj-'bill'
        if other == 'bill':
            whom=input("Tell us what bill u wish to pay: ")
            amt=int(input("TEll us amount of bill for "+whom))
            self*[whom,amt]
        elif other == 'pin change':
            newPin=int(input("TEll us new pin: "))
            self&newPin
        elif other == 'enquiry':
            self.enquiry()
        else:
            print("invalid choice")

use=User(876545678,3450.5,1122)
use-input("Tell us choice: ")