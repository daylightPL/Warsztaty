def podatek(kwota):

    if kwota <= 44490:
        val = kwota*0.19

    elif kwota <= 85528:
        val = 44490*0.19+(kwota-44490)*0.3

    else:
        val = 44490*0.19+(85528-44490)*0.3+(kwota-85528)*0.4
    return val


print(podatek(50000))
print(podatek(100000))
