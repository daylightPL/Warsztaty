import math


def wybierz_pieniadze(val):

    ilosc_nominalow = {}
    nominaly = [20, 10, 5, 2, 1]

    if val <= 0:
        print('Wybierz dodatnią kwotę')
        return val

    print('Dla kwoty ' + str(val) + 'zł należy wyjąć:')
    for i in nominaly:
        if val/i >= 1:
            ilosc_nominalow[i] = math.floor(val/i)
            val = val % i
            if val == 0:

                for k, v in ilosc_nominalow.items():
                    print(str(k) + 'zł x ' + str(v))
                print('\n')

wybierz_pieniadze(115)
wybierz_pieniadze(79)