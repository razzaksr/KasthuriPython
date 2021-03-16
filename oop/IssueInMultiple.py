# multiple inheriance issue


class Alpha:
    data1=0
    data2=0
    def setAlpha(self,one=0,two=0):
        self.data1=one
        self.data2=two

class Beta:
    data1=0
    data4=0
    def setBeta(self,three=0,four=0):
        self.data1=three
        self.data4=four

class Combine(Alpha,Beta):
    result=0
    def doCombine(self):
        self.result=(self.data4*self.data2)+(self.data1)
    def __str__(self):
        return str(self.data1)+" "+str(self.data2)+" "+str(self.data4)+" "+str(self.result)

com=Combine()
com.setAlpha(10,3)
com.setBeta(41,4)
com.doCombine()
print(com)