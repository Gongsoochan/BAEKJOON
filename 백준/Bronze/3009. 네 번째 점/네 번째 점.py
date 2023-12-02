lista = []
listb = []
for i in range(3):
    a, b = map(int,input().split())
    if a in lista:
        lista.remove(a)
    else:
        lista.append(a)
    if b in listb:
        listb.remove(b)
    else:
        listb.append(b)
print(lista[0], listb[0])