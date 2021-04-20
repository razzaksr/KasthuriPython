from errors.CustomError import KasthuriError


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


b1=Bike("Avenger Cruise",220,2016,99000.34,40,20)
b2=Bike()
b2.setModel("CT100");b2.setQty(30);b2.setCc(100);b2.setYear(2021);b2.setMilage(65);b2.setOnRoadPrice(78900.3)
b3=Bike("Vikrant",150,2018,87600.34,45,10)
b4=Bike("Platina",100,2021,73000.34,70,50)

stock=[b1,b2,b4]
'''
for x in stock:
    print(str(x))
'''

try:
    for x in stock:
        if (x.getModel() == 'Avenger'):
            print(str(x))
            break
    else:
        raise KasthuriError
except KasthuriError as kerror:
    print(kerror,"gonna handled here")
    name=input("TEll us model once again")
    for x in stock:
        if (x.getModel() == name):
            print(str(x))
            break
