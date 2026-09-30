frutas = ["uva", "pera", "uva", "manzana"]

elemento_eliminar = "uva"
ocurrencia = 2  # Queremos la 2da vez que aparece

contador = 0
for i in range(len(frutas)):
    if frutas[i] == elemento_eliminar:
        contador += 1
        if contador == ocurrencia:
            frutas.pop(i)  
            break 

print(frutas)