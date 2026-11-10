# p155-mayor-menor.py
# funcion para obtener el mayor y menor elemento de una lista y nos regrese una tupla con esos elementos
# se crea una funcion mas que captura los datos del usuario y entrega la lista de numeros
def capturar_numeros() -> list[float]:
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return numeros

def mayor_menor(lista: list[float]) -> tuple[float, float]:
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    mayor = lista[0]
    menor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
        if elemento < menor:
            menor = elemento
    return (mayor, menor)
numeros = capturar_numeros()
print(f"Los números ingresados son: {numeros}")
num_mayor = mayor_menor(numeros)[0]
num_menor = mayor_menor(numeros)[1]
print(f"El número mayor es: {num_mayor}")
print(f"El número menor es: {num_menor}")