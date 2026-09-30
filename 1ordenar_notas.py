
# EJERCICIO 1 - ORDENAR NOTAS ESTUDIANTILES

notas = [85, 42, 93, 67, 28, 75]

bubble = notas.copy()

for i in range(len(bubble)):
    for j in range(0, len(bubble) - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

print("Resultado Bubble Sort:", bubble)


selection = notas.copy()

for i in range(len(selection)):
    minimo = i

    for j in range(i + 1, len(selection)):
        if selection[j] < selection[minimo]:
            minimo = j

    selection[i], selection[minimo] = selection[minimo], selection[i]

print("Resultado Selection Sort:", selection)


minima = min(notas)
maxima = max(notas)
promedio = sum(notas) / len(notas)

print("Nota mínima:", minima)
print("Nota máxima:", maxima)
print("Promedio:", promedio)