#hierarchy inheritance
from oop.SimpleInheritance import Gmail, Youtube


class Flipkart(Gmail):
    profile={}
    def __init__(self,user="",pas="",profileNAme="",kitems=[],ohis=[]):
        self.profile={"kart":kitems,"orders":ohis,"proName":profileNAme}
        super(Flipkart, self).__init__(user,pas)
    def __add__(self,other):
        self.profile["kart"].append(other)
        print(other,"has added to kart")
    def __or__(self, other):
        self.profile['orders'].append(other)
        print(other,"Order made")


you1=Youtube(['shinchan','jackichan'],"razzaksr","12345678")

you1.upload('GST',0.30)

you1.viewLibrary()

fp1=Flipkart('kasthoori','kas',"Kasthuri",['kid cloth','shoe'],['nokia 6.1plus','realme 5s'])
fp1+'Dell Vostro 1014'
fp1|'kid cloths'
