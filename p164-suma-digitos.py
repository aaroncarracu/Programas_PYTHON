# p164-suma-digitos.py
# Escribe un programa que procese una lista de números. Debes implementar lo siguiente:
# 1. Una función que lea y devuelva una lista de números enteros (puedes reusar la hecha en clase).
# 2. Una función que reciba un número entero y devuelva la suma de sus dígitos individuales (ej: 1971 ->
# 1+9+7+1 = 18).
# 3. Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y
# devolver una nueva lista que contenga la suma de los dígitos de cada número original.
# El programa debe imprimir la lista original y la nueva lista con las sumas.
# Funcion para leer una lista de numeros enteros
def leer_lista():
    numeros = input("Dame los números (separados por espacio): ")
    lista = [int(num) for num in numeros.split()]
    return lista


# Funcion para sumar los digitos de un numero
def suma_digitos(numero):
    suma = 0

    numero = abs(numero)

    while numero > 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10

    return suma


# Funcion principal para crear una nueva lista
def procesar_lista(lista):
    nueva_lista = []

    for numero in lista:
        resultado = suma_digitos(numero)
        nueva_lista.append(resultado)

    return nueva_lista


# Programa principal
numeros = leer_lista()

lista_sumas = procesar_lista(numeros)

print("La lista de números original          :", numeros)
print("La lista con las sumas de dígitos es   :", lista_sumas)

