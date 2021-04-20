# Relational operator: True/False: > >= < <= == !=
# logical operator: and or not


print("---------------Kasthoori Loan Agency--------------")
cibil=int(input("Tell us cibil score: "))
print("Are deserved to get 1Lack PL",(cibil>=700))


print("---------------Electrol Check-----------------")
age=int(input("Tell us your age to check eligibility to become candidate in assembly election: "))
print("Eligibility",(age<45 and age>=18))


print("------------------Ration Store---------------------")
cardType=input("Tell us card type: ")
print("Eligibility to get Rs.2500",(cardType!='Sugar' and cardType!='sugar' and cardType!='SUGAR'))
print("Eligibility to get RS.1000 for covid19",(cardType=='Rice' or cardType=='Sugar'))






