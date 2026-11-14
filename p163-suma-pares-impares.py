# p163-suma-pares-impares.py
# Crea un programa que sume números pares o impares dentro de un rango especificado. El programa debe tener
# una función que reciba tres parámetros: un número de inicio, un número de fin y una letra ('P' o 'I').
def suma_pares_impares(inicio, fin, tipo):
    suma = 0
    for numero in range(inicio, fin + 1):
        if tipo == 'P' and numero % 2 == 0:
            suma += numero
        elif tipo == 'I' and numero % 2 != 0:
            suma += numero
    return suma
inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))
tipo = input("Ingrese 'P' para sumar pares o 'I' para sumar impares: ").upper()
resultado = suma_pares_impares(inicio, fin, tipo)
print("\nNúmeros sumados:")
print(" + ".join(str(numero) for numero in range(inicio, fin + 1) if (tipo == 'P' and numero % 2 == 0) or (tipo == 'I' and numero % 2 != 0)))
print(f"La suma de los números es: {resultado}")