#overriding

class Dealer:
    name=""
    price=0.0
    def __str__(self):
        return self.name+" "+str(self.price)
    def __sub__(self, other):
        print("5 percent discount gonna applied soon")
        self.price-=(self.price*0.050)
        print("5 percent discount applied")

class Retailer(Dealer):
    qty=0
    def __str__(self):
        return super(Retailer, self).__str__()+" "+str(self.qty)+" \n"
    def __sub__(self, other):
        print("15 percent discount gonna applied soon")
        self.price-=(self.price*0.150)
        print("15 percent discount applied")
        super(Retailer, self).__sub__(other)


ret=Retailer()
ret.name="DEnver Dio";
ret.price=431.9
ret.qty=80

print(ret)

ret-'hey'

print(ret)