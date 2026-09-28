# # Ejercicio 1 - Ordenar notas estudiantiles (ordenamiento por seleccion)

def ordenar_notas(notas):
    n = len(notas)
    for i in range(n -1):
        idx_min = i
        for j in range(i + 1,n):
            if notas[j] < notas[idx_min]:
                idx_min = j

        if idx_min !=i:
            notas[i], notas[idx_min] = notas[idx_min], notas[i]

notas = [85, 42, 93, 67, 28, 75]

print(f"Notas desordenadas: {notas}")      

ordenar_notas(notas)

print(f"Notas ordenadas: {notas}")

notamin= min(notas)
notamax = max(notas)
promedio = sum(notas)/len(notas)

print(f"La nota mínima es: {notamin} | La nota máxima es: {notamax} | El promedio de notas es: {promedio}")