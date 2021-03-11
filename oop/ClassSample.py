# class syntax and illustration


class Account:
    accountNo=0
    accountBal=0.0
    def enquiry(self):
        print(self.accountNo,self.accountBal)


ac1=Account()

ac1.accountNo=8765445634
ac1.accountBal=5600.4
ac1.enquiry()


kasthoori=Account()
kasthoori.accountNo=87655678442
kasthoori.accountBal=129443.11
kasthoori.enquiry()


print(hasattr(ac1,"accountNum"))
delattr(kasthoori,"accountBal")
print(hasattr(kasthoori,"accountBal"))
kasthoori.enquiry()

setattr(ac1,"holder","mohamed")

print(ac1.holder)
#print(kasthoori.holder)

print(getattr(ac1,"accountBal"))

kasthoori.ifsc="AB0001289"

print(kasthoori.ifsc)
print(ac1.ifsc)