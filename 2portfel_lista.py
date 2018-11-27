ilosc_nominalow={}
nominaly = [20, 10, 5, 2, 1]
portmonetka = [0, 2, 3, 0, 0, 5, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
skarbonka = [0, 0, 3, 0, 0, 5]
cena1 = 0
cena2 = 1122
cena3 = 18
cena4 = 38
cena5 = 3


def suma_portfela(portfel):
    val = 0
    for i in range(len(portfel)):
        val = val + i*portfel[i]
    return val


def rozmien(portfel, kwota):
    if kwota <= 0:
        print('Wybierz dodatnią kwotę')
        return kwota

    if kwota > suma_portfela(portfel):
        print('Kwota to ' + str(kwota) + 'zł, a ty masz tylko ' + str(suma_portfela(portfel)) + 'zł')

    else:
        print('Dla kwoty ' + str(kwota) + 'zł należy wyjąć:')
        # portfel[20] - ilosc 20zlotowek
        # portfel[10] - ilosc 10zlotowek
        ilosc_nominalow = {}
        for i in nominaly:
            if len(portfel)>i:
                licznik = 0
                while kwota >= i and portfel[i] > 0:
                    licznik += 1
                    portfel[i] -= 1
                    kwota -= i
                ilosc_nominalow[i]=licznik
        while kwota > 0:
            print('uwaga kwota nie bedzie rowna')
            for i in portfel:
                if i > 0:
                    ilosc_nominalow[i] += 1
                    kwota = kwota - i
                    if kwota <= 0:
                        break

        for k, v in ilosc_nominalow.items():
            print(str(k) + 'zł x ' + str(v))
        print('\n')


rozmien(portmonetka, cena1)
rozmien(portmonetka, cena2)
rozmien(portmonetka, cena3)
rozmien(portmonetka, cena4)
rozmien(skarbonka, cena5)