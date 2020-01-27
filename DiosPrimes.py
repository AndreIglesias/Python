casos = int(input())
for i in range(casos):
    intervalo = str(input())
    intervalo = intervalo.split(' ')
    a = int(intervalo[0])
    b = int(intervalo[1])
    lista = []
    if a % 2 == 0:
        for p in range(a+1, b+1, 2):
            if ((2**(p-1))%p is 1) and (p is not 1):
                lista.append(p)
    else:
        for p in range(a, b+1, 2):
            if ((2**(p-1))%p is 1) and ( p is not 1):
                lista.append(p)
    for i in range(len(lista)):
        reverse = int(str(lista[i])[::-1])
        copia1 = list(lista[i])
        copia2 = list(reverse)
        if  (2**(reverse-1))%reverse is 1:
            DiosPrimes = []
            for r in range(len(str(lista[i]))):
                del copia1[0], copia2[0]
                copea1 = int(''.join(map(str,copia1)))
                copea2 = int(''.join(map(str,copia2)))
                if ((2**(copea1-1))%copea1 != 1) or ((2**(copea2-1))%copea2 != 1): break
            if len(copia1) is 0: DiosPrimes.append(lista[i])
    print(DiosPrimes, len(DiosPrimes))
