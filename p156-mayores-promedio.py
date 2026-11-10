# p156-mayores-promedio.py 
# calcularemos el promedio de una lista con una funcion
# creamos una lista con los mayores al promedio con otra funcion 

def promedio(lista: list[float]) -> float:
    if not lista:
        return 0.0
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_al_promedio(lista: list[float]) -> list[float]:
    prom = promedio(lista)
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores
# program principal
numeros = [12.22,1.5, 2.3, 3.7, 4.1, 10.22, 34.5]
print(f"Los números en la lista son: {numeros}")
prom = promedio(numeros)
print(f"El promedio de los elementos en la lista es: {prom:.2f}")
mayores = mayores_al_promedio(numeros)
print(f"Los números mayores al promedio son: {mayores}")