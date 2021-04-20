import pickle

loc=open("D:\\Course backups\\Python\\Kasthuri\\kitkat.txt","rb")


print("Contents inside",loc.name)
print(pickle.load(loc))




loc.close()