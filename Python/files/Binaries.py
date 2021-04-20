import pickle

loc=open("D:\\Course backups\\Python\\Kasthuri\\kitkat.txt","ab")

#loc.write(input("Tell us what you wish to write: "))
str=input("Tell us what you wish to write: ")

hi=[12,45,6778,132.7,45.7,'zealous']

pickle.dump(str,loc)
pickle.dump(hi,loc)

print("File has created")

loc.close()