# Ordenar matriz

matriz = [
    [4, 6, 1],
    [2, 9, 7],
    [3, 5, 8]
]


lista = []
for fila in matriz:
    for num in fila:
        lista.append(num)


n = len(lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            # Intercambiar elementos
            lista[j], lista[j + 1] = lista[j + 1], lista[j]


k = 0
for i in range(3):
    for j in range(3):
        matriz[i][j] = lista[k]
        k += 1


for fila in matriz:
    print(fila)

