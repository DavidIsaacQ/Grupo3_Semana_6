# Ejercicio 2 - Sistema de historial de navegación (Pila)

historial = []

def visitar(url):
    historial.append(url)
    print()
    print(f"Visitando: {url}")
    print(historial)
    

def retroceder():
    retroceder = historial.pop()
    print()
    print(f"Retrocediendo desde {retroceder} | Ahora estás en: {historial[-1]}")
    print()


def pagina_actual():
        print(f"Página actual: {historial[-1]}")
        return historial[-1]

  
visitar("Google")
pagina_actual()
visitar("YouTube")
pagina_actual()
visitar("GitHub")
pagina_actual()

retroceder()
retroceder()