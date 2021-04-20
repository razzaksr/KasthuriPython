#Bus booking chart

chart=''
for row in range(1,5):
    for col in range(1,5):
        amt=int(input("Ticket amount: "))
        if amt>=320:
            chart+='$'
        else:
            chart+='#'
        if col==2:
            chart+=' '
    chart+='\n'
else:
    print(chart)
