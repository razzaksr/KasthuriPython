# Multiple inheritance

class SkillSet:
    def __init__(self,name="",exp=0,poc=0):
        self.skill=name
        self.exp=exp
        self.poc=poc
    def view(self):
        return self.skill+" "+str(self.exp)+" "+str(self.poc)


class Personal:
    def __init__(self,name,qual="",con=0,mail=""):
        self.name=name
        self.qualification=qual
        self.contact=con
        self.mail=mail
    def __str__(self):
        return self.name+" "+self.qualification+" "+str(self.contact)+" "+self.mail


#multiple
class Profile(Personal,SkillSet):
    def __init__(self,user="",q="",c=0,m="",s="",e=0,p=0):
        super(Profile, self).__init__(user,q,c,m)
        self.skill=s;self.exp=e;self.poc=p
    def __str__(self):
        return super(Profile, self).__str__()+" "+self.view()


pro=Profile("kasthuri","MCA",8765678767,"kashui@gmail.com","python",2,3)
print(pro)