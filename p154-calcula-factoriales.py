# p154-calcula-factoriales.py
# Desarrolla un programa que calcule el factorial de cada número en una lista. Debes implementar:
# 1. Una función que lea y devuelva una lista de números enteros
# 2. Una función que reciba un número entero y devuelva su factorial (ej: 5! = 5*4*3*2*1 = 120)
# Una función principal que reciba la lista de números. Esta debe usar la función factorial para crear y
# devolver una nueva lista con los factoriales de cada número.
def leer_lista():
    numeros = input("Dame los números (separados por espacio): ")
    lista = [int(num) for num in numeros.split()]
    return lista

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def procesar_factoriales(lista):
    return [factorial(n) for n in lista]

# Programa principal
numeros = leer_lista()
factoriales = procesar_factoriales(numeros)
print("La lista de números original          :", numeros)
print("La lista con los factoriales es       :", factoriales)