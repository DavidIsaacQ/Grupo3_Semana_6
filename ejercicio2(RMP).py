pila_historial = []


pila_historial.append("Google")
print(f"Visitando: Google -> Historial actual: {pila_historial}")

pila_historial.append("YouTube")
print(f"Visitando: YouTube -> Historial actual: {pila_historial}")

pila_historial.append("GitHub")
print(f"Visitando: GitHub -> Historial actual: {pila_historial}")

print(f"\nPágina actual en pantalla: {pila_historial[-1]}\n")

pagina_eliminada = pila_historial.pop()
pagina_regreso = pila_historial[-1] if len(pila_historial) > 0 else "Ninguna"
print(f"Retrocediendo (saliendo de {pagina_eliminada}) -> Regresó a: {pagina_regreso}")

pagina_eliminada = pila_historial.pop()
pagina_regreso = pila_historial[-1] if len(pila_historial) > 0 else "Ninguna"
print(f"Retrocediendo (saliendo de {pagina_eliminada}) -> Regresó a: {pagina_regreso}")
