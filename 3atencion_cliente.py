
# EJERCICIO 3 - SISTEMA DE ATENCIÓN AL CLIENTE
# Cola (Queue) - FIFO

cola = []


def tomar_turno(cliente):
    cola.append(cliente)
    print("Cliente", cliente, "tomó su turno.")


def atender():
    if len(cola) > 0:
        cliente = cola.pop(0)
        print("Atendiendo a:", cliente)
    else:
        print("No hay clientes en espera.")


def mostrar_cola():
    print("Clientes esperando:", len(cola))
    print("Cola:", cola)


# Simulación

tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Carlos")
tomar_turno("María")

mostrar_cola()

atender()
atender()

mostrar_cola()

tomar_turno("Pedro")

mostrar_cola()

atender()
atender()
atender()

mostrar_cola()