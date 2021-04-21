import pickle as pic

best={
    2021:["Karnan","Nenjam marapathillai","Ranasingam"],
    2020:["Asuran","Visawasam"],
    2012:["Vinnai thandi varuvaya","Veeram","Jilla"]
}

encrypted=pic.dumps(best)#pickling

print(encrypted)

#yet=pic.loads(encrypted)# unpickling
for key,value in pic.loads(encrypted).items():
    print(key,value)