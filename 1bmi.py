val = 0


def bmi(masa, wzrost):
    val = round(masa/(wzrost*wzrost), 2)
    print ('Twój wskaźnik BMI wynosi ' + str(val) + '.')
    return val


print('Podaj wagę w kg')
A=int(input())

print('Podaj wzrost w cm')
B=int(input())/100


def komentarz(bmi):
    if bmi < 18.5:
        print('Niedowaga')
    elif bmi < 24.99:
        print('Norma')
    else:
        print('Nadwaga')


komentarz(bmi(A, B))
