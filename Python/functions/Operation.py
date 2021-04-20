# Games of WonderLa

def wetGames(weight):
    if weight >=56.1:
        print("Let customer to go layout 47")
    else:
        print("Dont let them in")

def adventures(age):
    if age>=14:
        print("Enjoy @ layout 31")
    else:
        print("Need to grow up")

def snowPark():
    print("Feel like Kashmir @ layout 89")


#main section
wish=input("Tell us where to go: ")
if wish == 'water':
    wt=float(input("Tell us your weight: "))
    wetGames(wt)
elif wish == 'thrill':
    ag=int(input("Tell us age: "))
    adventures(ag)
elif wish == 'snow':
    snowPark()
else:
    print("Game not available")
