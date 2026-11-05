# p144-tabla-multiplicar.py
# Ejemplo de una funcion que imprime la tabla de multiplicar de un numero hasta n
print("\033c", end="")
def tabla_multiplicar(numero: int, hasta: int) -> None:
    for i in range(1, hasta + 1):
        print(f'{numero} x {i} = {numero * i}')

# tabla_multiplicar(5, 10)
tabla_multiplicar(int(input('Dame un numero: ')), int(input('Hasta que numero quieres la tabla: ')))