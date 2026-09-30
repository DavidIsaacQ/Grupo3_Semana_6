
# EJERCICIO 2 - HISTORIAL DE NAVEGACIÓN
# Pila (Stack) - LIFO

historial = []


def visitar(url):
    historial.append(url)
    print("Visitando:", url)
    print("Pila actual:", historial)


def retroceder():
    if len(historial) > 1:
        historial.pop()
        print("Regresando a:", historial[-1])
        print("Pila actual:", historial)
    else:
        print("No hay páginas anteriores.")


def pagina_actual():
    if len(historial) > 0:
        print("Página actual:", historial[-1])
    else:
        print("No hay ninguna página abierta.")


# Prueba
visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()

retroceder()
retroceder()