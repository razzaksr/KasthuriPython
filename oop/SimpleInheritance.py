'''
Inheritance:
derive/ copy class attributes and functions from one class to another
inorder to avoid creating objects for all classes

type:
single
multi level
hierarchy

multiple
hybrid
'''

class Gmail:
    def __init__(self,user="",pas=""):
        self.__user=user
        self.__pas=pas

    def setUser(self,user):self.__user=user
    def getUser(self):return self.__user
    def setPas(self,pas):self.__pas=pas
    def getPas(self):return self.__pas


class Youtube(Gmail):
    def __init__(self,vidList=[],user="",pas=""):
        self.__videos=vidList
        super(Youtube, self).__init__(user,pas)
    def upload(self,name="",duration=0.0):
        self.__videos.append(name)
        print(name,"video with duration of",duration,"uploaded in your",self.getUser())


you1=Youtube(['shinchan','jackichan'],"razzaksr","12345678")

you1.upload('GST',0.30)
