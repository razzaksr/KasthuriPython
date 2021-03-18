# Showroom Management

# entity/business/model/ encapsulated class
class Bike:
    def __init__(self,mod="",cc=0,yr=0,on=0.0,mil=0,q=0):
        self.__model=mod
        self.__cc=cc
        self.__year=yr
        self.__onRoadPrice=on
        self.__milage=mil
        self.__qty=q
    def setModel(self,mod=""):self.__model=mod
    def getModel(self):return self.__model
    def setCc(self,cc=0):self.__cc=cc
    def getCc(self):return self.__cc
    def setYear(self,yr=0):self.__year=yr
    def getYear(self):return self.__year
    def setOnRoadPrice(self,on=0.0):self.__onRoadPrice=on
    def getOnRoadPrice(self):return self.__onRoadPrice
    def setMilage(self,mil=0):self.__milage=mil
    def getMilage(self):return self.__milage
    def setQty(self,q=0):self.__qty=q
    def getQty(self):return self.__qty

    def __str__(self):
        return self.__model+" "+str(self.__cc)+" "+str(self.__year)+" "+str(self.__onRoadPrice)+" "+str(self.__milage)+" "+str(self.__qty)+"\n"

class Rainbow:
    def __init__(self,stk=[],pr=0):
        self.__stock=stk
        self.__income=pr

    #create and add new stock
    def __add__(self, other):
        self.__stock.append(other)
        print(other.getModel(),"has added to our stock")

    #listing
    def __str__(self):
        temp="Available Bikes are:\n"
        for x in self.__stock:
            temp+=str(x)
        temp+=str(self.__income)+"\n"
        return temp


    #read operations: obj<<'milage', obj<<'price', obj<<'model'
    def __lshift__(self, other):
        if other == 'milage':
            mil=int(input("Tell us desired milage: "))
            for x in self.__stock:
                if x.getMilage() >= mil:print(str(x))
        elif other == 'cost':
            price=int(input("Tell us desired cost: "))
            for x in self.__stock:
                if x.getOnRoadPrice() <= price:print(str(x))
        elif other == 'model':
            mod=input("Tell us desired model: ")
            for x in self.__stock:
                if x.getModel() == mod:print(str(x))
        elif other=='pos':
            pos=int(input("Tell us index: "))
            if pos<len(other):print(self.__stock[pos])
            else:print("Invalid position to read")
        elif other in self.__stock:
            print(self.__stock.index(other))
        else:
            print("Unknown data")

    #update stock item by selling bike
    def __sub__(self, other):# obj-['Platina','mohamed']
        for x in range(len(self.__stock)):
            if self.__stock[x].getModel() == other[0]:
                self.__income+=self.__stock[x].getOnRoadPrice()
                self.__stock[x].setQty(self.__stock[x].getQty()-1)
                print("Bike ",self.__stock[x].getModel(),"has sold to",other[1])
                return
        else:print(other[0],"not found for",other[1])

    #update when stock getting over
    def __le__(self, other):#obj<=qty
        for x in range(len(self.__stock)):
            if self.__stock[x].getQty()<=other:
                new=int(input("Tell us how many new "+self.__stock[x].getModel()+" u wish to add: "))
                self.__stock[x].setQty(self.__stock[x].getQty()+new)
                print(new,"amount of new stocks added to",self.__stock[x].getModel())

    #update stock items's cost by offer
    def __eq__(self, other):#obj==[percentage,priceRange]
        for x in range(len(self.__stock)):
            if self.__stock[x].getOnRoadPrice()>=other[1]:
                tmp=self.__stock[x].getOnRoadPrice()-(self.__stock[x].getOnRoadPrice()*other[0])/100
                self.__stock[x].setOnRoadPrice(tmp)
                print(self.__stock[x].getModel(),"has offer price",self.__stock[x].getOnRoadPrice())
                #return
        else:print(other[1],"not match in available bikes")

    def __ne__(self, other):#obj!=year
        delPos=[]
        #collecting deletable positions
        for x in range(len(self.__stock)):
            if self.__stock[x].getYear()<=other:
                '''print(self.__stock[x].getModel(),"gonna stopped to sale")
                self.__stock.pop(x)'''
                delPos.append(x)

        # deleting stock based on delPos loop
        for x in delPos:
            print(self.__stock[x].getModel(), "gonna stopped to sale")
            self.__stock.pop(x)



# verify til stock create and list
b1=Bike("Avenger Cruise",220,2016,99000.34,40,20)
b2=Bike()
b2.setModel("CT100");b2.setQty(30);b2.setCc(100);b2.setYear(2021);b2.setMilage(65);b2.setOnRoadPrice(78900.3)
r=Rainbow()
r+b1
r+b2

print(r)


#to check read
b3=Bike("Vikrant",150,2018,87600.34,45,10)
b4=Bike("Platina",100,2021,73000.34,70,50)
r+b3
r+b4

#reading
'''
r<<'milage'
r<<'cost'
r<<'model'
r<<'cc'
r<<'pos'
r<<b3
'''

#checking selling process
'''
r-['Avenger Cruise','Razak Mohamed']
r-['CT100','Kannan']
r-['Pulsar','Sabari']
r-['Platina','Ibrahim']
r-['Vikrant','Sheik']
'''

print(r)

# update price by offer
#r==[7,80000]


#update stock qty
#r<=10

# deletion based on year
r!=2016

print(r)