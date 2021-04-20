# function with returns

def calculate(dollar):
    return dollar*80

def check(greetings):
    if greetings == 'good evening':
        return 'wrong'
    print('have a nice day')


#main section
rupees=calculate(4560)
print("Rupees you will get: ",rupees)

print(check('good morning'))

