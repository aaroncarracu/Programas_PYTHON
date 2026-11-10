# p159-nombres.py
# funciones que toma dos listas de cadenas y regresa una lista 
# juntar ambas listas
# invertir la lista
# convertir a mayusculas
def capturanombres() -> list[str]:
    nombres = []
    while True:
        nombre = input("Ingrese un nombre (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        nombres.append(nombre)
    return nombres
def procesar_nombres(lista1: list[str], lista2: list[str]) -> list[str]:
    # juntar ambas listas
    lista_combinada = lista1 + lista2
    # invertir la lista
    lista_invertida = lista_combinada[::-1]
    # convertir a mayusculas
    lista_mayusculas = [nombre.upper() for nombre in lista_invertida]
    return lista_mayusculas

nombres1 = ["ana", "juan", "maria", "pedro", "luis"]
nombres2 = capturanombres()
print(f"Los nombres de la primera lista son: {nombres1} - len: {len(nombres1)}")
print(f"Los nombres de la segunda lista son: {nombres2} - len: {len(nombres2)}")
todos = procesar_nombres(nombres1, nombres2)
print(f"Todos los nombres procesados son: {todos} - len: {len(todos)}")