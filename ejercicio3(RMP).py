cola = []

def tomar_turno(cliente):
    cola.append(cliente)
    print (f"{cliente} entro en la cola")

def atender ():
    cliente_atendido = cola.pop(0)
    print (f"Atendiendo a {cliente_atendido}")
    return cliente_atendido

def mostrar_cola():
    print (f"Clientes en espera ({len(cola)}): {cola}")
tomar_turno("Ana")
tomar_turno("Rosa")
tomar_turno("clotilda")
mostrar_cola()

atender()
mostrar_cola()

tomar_turno ("Grace")
mostrar_cola()

atender ()
atender () 
mostrar_cola()


