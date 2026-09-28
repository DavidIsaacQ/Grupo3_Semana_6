# #Un profesor tiene las notas de 6 estudiantes en una lista 
# desordenada:
# [85, 42, 93, 67, 28, 75]
# Se pide:
# a) Ordenar la lista usando 
# Bubble Sort e imprimir el resultado.
notas = [85, 42, 93, 67, 28, 75]

def bubble_sort (notas):
    total = len(notas)
    nota_minima = min(notas)
    nota_maxima = max(notas)
    promedio = sum(notas) / total
    for i in range (total): #0 / 1 / 2
        cambio = False

        for j in range (0, total - i - 1):
            if notas[j] > notas [j+1]:
                notas [j], notas [j+1] = notas [j+1] , notas [j]
                cambio = True
        if not cambio:
            break
    print (f"Nota minima = {nota_minima}")
    print (f"Nota maxima = {nota_maxima}")
    print (f"Promedio = {promedio}")
    return notas

def selection_sort (notas):
    total = len(notas)
    for i in range (total):
        idx_min = i
        for j in range (i+1,total):
            if notas[j] < notas[idx_min]:
                j = idx_min

        if idx_min != i:
            notas[i], notas[idx_min] = notas[idx_min], notas[i]
    return notas



lista_ordenada = bubble_sort(notas)
lista_ordenada1 = selection_sort(notas)
print (f"Bubble Sort ={lista_ordenada}")
print (f"Selection Sort = {lista_ordenada1}")