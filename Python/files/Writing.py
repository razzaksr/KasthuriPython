
#create/replace
#loc=open("D:\\Course backups\\Python\\Kasthuri\\applepie.txt","w")#

#append
loc=open("D:\\Course backups\\Python\\Kasthuri\\applepie.txt","a")

loc.write(input("Tell us what you wish to write: "))
print("File has created")

loc.close()