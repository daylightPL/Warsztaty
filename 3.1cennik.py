cennik = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
}
lista = {'olej': 2, 'kawa': 1}


def zakupy(cennik, lista):
    koszt = 0
    for k in lista:
        koszt += lista[k]*cennik[k]
    return koszt


print(zakupy(cennik, lista))