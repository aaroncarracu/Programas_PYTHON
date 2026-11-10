# p154-lista-pares.py
# funcion para obtener los elementos pares de una lista y nos regrese una nueva lista con esos elementos
def lista_pares(lista: list[int]) -> list[int]:
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return pares

# programa principal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = lista_pares(numeros)
print(f"Los elementos pares en la lista son: {resultado}")