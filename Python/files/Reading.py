file=open("D:\Course backups\Web\Pradeep\PradeepClientSide\Forms.html","r")

#print(len(file.read()))
print(file.read(500))# reads first 500 chars
file.seek(300,0)# reassign cursor to the 300th char from the beginning
print("Seek by manual")
print("Cursors location:",file.tell())
print(file.read())# read til end from the last change of cursor

file.close()
