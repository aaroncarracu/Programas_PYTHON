# p157-pares-impares.py
# funcion para obtener los elementos pares e impares de una lista y nos regrese dos nuevas listas con esos elementos
def lista_pares_impares(lista: list[int]) -> tuple[list[int], list[int]]:
    pares = []
    impares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
        else:
            impares.append(elemento)
    return (pares, impares)

# programa principal
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Los números en la lista son: {numeros}")
pares, impares = lista_pares_impares(numeros)
print(f"Los elementos pares en la lista son: {pares}")
print(f"Los elementos impares en la lista son: {impares}")