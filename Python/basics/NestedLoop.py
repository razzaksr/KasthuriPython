# Shift based billing process


total=0
# number of persons
for per in range(1,3):
    print("Sales person",per)
    # timing for per person
    net = 0
    time = 1.0
    while time < 1.61:
        print(time)
        bill = int(input("Bring the bill with amount: "))
        net += bill
        print("bill paid")
        time += 0.10
    else:
        print("collected bill is", net, "by",per)
        total+=net
else:
    print("Total income of the day",total)