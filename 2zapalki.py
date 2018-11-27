import random

zapalki = random.randrange(7, 30)
print('wylosowana liczba zapałek: ' + str(zapalki))


while zapalki > 0:
    print('ile zapałek chcesz zabrać?')
    u_bierze = input('Podaj swój ruch: ')
    if int(u_bierze) in [1, 2, 3] and int(u_bierze) <= zapalki:

        zapalki= zapalki - int(u_bierze)
        print('wziąłeś ' + str(u_bierze) + ' zapałki, zostało ' + str(zapalki))
        if zapalki <= 0:
            print('Przegrałeś, zabrałeś ostatnią zapałkę.')
            break
        else:
            if zapalki > 3:
                k_bierze = random.randint(1, 3)

            elif zapalki == 3:
                k_bierze = 2
            elif zapalki == 2:
                k_bierze = 1
            elif zapalki == 1:
                k_bierze = 1
            zapalki = zapalki - int(k_bierze)
            print('przeciwnik zabrał ' + str(k_bierze) + ' zapałki, zostało ' + str(zapalki))
            if zapalki <= 0:
                print('Wygrałeś, przeciwnik zabrał ostatnią zapałkę.')
                break

    elif int(u_bierze) > zapalki:
        print('Chcesz wziąć więcej zapałek niż zostało')

    else:
        print('Możesz wziąć tylko 1, 2 lub 3 zapałki')
