# p153-suma-lista.py
# funcion para sumar los elementos de una lista y nos regrese la suma
def suma_lista(lista: list[float]) -> float:
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
# programa principal
numeros = [1.5, 2.3, 3.7, 4.1]
resultado = suma_lista(numeros)
print(f"La suma de los elementos en la lista es: {resultado}")