# p160–numero-menor.py
# Crea un programa que incluya una función. Dicha función debe solicitar 3 números enteros al usuario y devolver el
# menor.
def menor_numero():
    # Solicitar 3 números enteros al usuario
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    num3 = int(input("Ingrese el tercer número entero: "))

    # Determinar el menor número
    menor = min(num1, num2, num3)

    return menor
print("El menor número es:", menor_numero())