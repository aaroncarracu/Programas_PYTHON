# p146-numero-mayor.py
# Ejemplo de una funcion que devuelve el numero mayor de tres numeros
print("\033c", end="")

def numero_mayor(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Ejemplo de uso
n1 = int(input('Dame el primer numero: '))
n2 = int(input('Dame el segundo numero: '))
n3 = int(input('Dame el tercer numero: '))

print(f'El numero mayor es: {numero_mayor(n1, n2, n3)}')