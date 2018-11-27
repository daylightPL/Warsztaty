def suma_dzielnikow(n):
    suma = 0
    lista = []


    for i in range(1,n-1):
        if n % i == 0:
            lista.append(i)
            suma = suma+i
    return lista


print (suma_dzielnikow(6))