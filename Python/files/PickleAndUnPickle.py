import pickle as pic


best={
    2021:[2.5,6.7,12.5,9.2,4.4,2.5],
    2022:[3.1,7.2,13.1,10.6,4.9,2.9],
    2012:[1.8,4.2,8.6,6.9,2.9,0.98]
}

'''file=open("binaries.doc","ab")

pic.dump(best, file);
print("Pickling into file has done")

file.close()'''

file=open("binaries.doc","rb")

yet=pic.load(file)
for k,v in yet.items():
    print(k,v)

file.close()