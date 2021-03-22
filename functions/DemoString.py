# String type functions


email='razzaksr@gmail.com   '
name='razakmohamed'
print(len(email))

email=email.rstrip(' ')
print(len(email))

print(email[:])
print(email[0:3])
print(email[::-1])

print(email.split('a'))

print(name.isalnum())
print(name.isspace())
print(name.islower())
name=name.capitalize()
print(name.isupper())
print(name)
name=name.upper()
print(name.isupper())

print(name.find('ZAK',3,10))

print(name)
name=name.replace('MOHAMED','mohamed')
print(name)

print(name.startswith('R',8))
print(name.endswith('ed',4,8))

print(name.count('A'))

print(name.index('a'))