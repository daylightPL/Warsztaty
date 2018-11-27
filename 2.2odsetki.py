def odsetki(oproc, czas, kwota):
    return kwota*(oproc/100)*(czas/12)


a = 3
b = 3
c = 1000

print(odsetki(a, b, c))

print('Lokata 12 miesieczna')
print(odsetki (a, 12, c))

kapital = c
for i in range(4):
    o = odsetki(a, b, c)
    c = c + o


print(c-kapital)

