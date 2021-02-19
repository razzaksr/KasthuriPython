'''
@@@@@
@@@@@
@@@@@
@@@@@
@@@@@
'''

'''
for row in range(1,6):
    for col in range(1,6):
        print("@",end="")
    print()
'''

'''
Left upper floyd
@
@@
@@@
@@@@
@@@@@
'''
'''
for row in range(1,6):
    for col in range(1,row+1):
        print("@",end="")
    print()
'''

'''
Right upper floyd
    @
   @@
  @@@
 @@@@
@@@@@
'''
'''
for row in range(1,6):
    for space in range(4,row-1,-1):
        print(" ",end="")
    for col in range(1,row+1):
        print("@",end="")
    print()
'''

'''
#Dynamic right upper floyd
row=int(input("TEll us how many row: "))
initiate=row-1
for line in range(1,row+1):
    for space in range(initiate,line-1,-1):
        print(" ",end="")
    for col in range(1,line+1):
        print("@",end="")
    print()
'''

'''
    @
   @ @
  @ @ @
 @ @ @ @
@ @ @ @ @
'''
'''
for row in range(1,6):
    for space in range(4,row-1,-1):
        print(" ",end="")
    for col in range(1,row+1):
        print("@ ",end="")
    print()
'''

'''
   @
  @@@
 @@@@@
@@@@@@@
'''
'''
limit=1
for row in range(1,5):
    for space in range(3,row-1,-1):
        print(" ",end="")
    for col in range(1,limit+1):
        print("@",end="")
    print()
    limit+=2
'''

#dynamic pyramid
row=int(input("Tell us no of rows: "))
limit=1
initiate=row-1
for line in range(1,row+1):
    for space in range(initiate,line-1,-1):
        print(" ",end="")
    for col in range(1,limit+1):
        print("@",end="")
    print()
    limit+=2