# Single try and multi except blocks: over fuel calculation

his = (120, 450, 300, 100, 560, 320, 459, 310, 720)
try:
    lit = int(input("Tell us liter filled: "))
    ind = int(input("Select position inorder to find milage: "))
    print("Selected distance is:",his[ind])
    print(his[ind] / lit)
except ValueError as verror:
    print(verror)
    print("Data are should be whole numeric")
    lit = int(input("Tell us liter filled: "))
    ind = int(input("Select position inorder to find milage: "))
    print("Selected distance is:", his[ind])
    print(his[ind] / lit)
except IndexError as ierror:
    print(ierror)
    print("Index should be within",len(his))
    ind = int(input("Select position inorder to find milage: "))
    print("Selected distance is:", his[ind])
    print(his[ind] / lit)
except ZeroDivisionError as zerror:
    print(zerror)
    print("Liter should not be ZERO")
    lit = int(input("Tell us liter filled: "))
    print("Selected distance is:", his[ind])
    print(his[ind] / lit)
except Exception as error:
    print(error)
