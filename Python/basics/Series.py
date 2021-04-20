# bit series: 1 2 4 8 16 32 64 128 256 ,....

'''
bit=1
data=1
limit=int(input("Tell us how many bits you want: "))
while bit<=limit:
    print(data, end=" ")
    bit += 1  # bit position
    data *= 2#value
else:
    print("Series ended")'''

data=1
for bit in range(1,9):
    print(data, end=" ")
    bit += 1  # bit position
    data *= 2  # value
else:
    print("Series done")