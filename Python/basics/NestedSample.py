'''
loop1:
    statements of loop1
    loop2:# considered to be inbuilt part of loop1
        #statements of loop2

'''

for table in range(1,6):
    print("table of",table)
    for num in range(1, 11):
        print(num,"X",table,"=",(num*table))
    print()