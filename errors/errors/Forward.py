ipl={"teams":["csk","mi","rr","dc","kkr","rcb"],
     "points":[12,9,10,11,7,4]}

def extract(key):
    try:
        print(ipl[key])
    except KeyError as kerror:
        print("Extract except block",kerror)
        raise kerror

try:
    extract(input("Tell us what you want: "))
except KeyError as ke:
    print("Main except block",ke)
    extract(input("Tell us what you want: "))