# Ejercicio 1 - Ordenar notas estudiantiles

def ordenar_notas(notas):
    n = len(notas)

    for i in range(n):
        intercambiado = False
        for j in range(0, n-i-1):
            if notas[j] > notas[j+1]:
                notas[j], notas[j+1] = notas[j+1], notas[j]
                intercambiado = True
        if not intercambiado:
            break


notas = [85, 42, 93, 67, 28, 75]
print(f"Lista desordenada: {notas}")
ordenar_notas(notas)

print("Lista ordenada:", notas)

notamin= min(notas)
notamax = max(notas)
promedio = sum(notas)/len(notas)

print(f"La nota mínima es: {notamin} | La nota máxima es: {notamax} | El promedio de notas es: {promedio}")