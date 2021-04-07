# Error handling:



try:
    annual = input("Tell us Annual salary: ")
    print(annual / 12)
except TypeError as terror:
    print('went inside except block')
    print(terror)
    annual = int(input("Tell us Annual salary: "))
    print((annual / 12)*100000)

print("Calculation done")