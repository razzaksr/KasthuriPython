#KeyError


candidate={"name":['riyaz','aravind','sasi','arunachalam'],
           "skills":['javaee','java','flask','spring'],
           "poc":[2,3,10,5],
           "annum":[5.6,9.3,12.8,10.8],
           "org":'Zealous'}

#print(candidate['name'][3])

try:
    phrase = input("Tell us what you want: ")
    print(candidate[phrase])
except KeyError as kerror:
    print(kerror)
    print("Column/ credential",phrase,"not found")
    phrase = input("Tell us what you want: ")
    print(candidate[phrase])
finally:
    print("Wish satisfied")
