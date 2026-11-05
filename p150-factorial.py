# p150-factorial.py
# Ejemplo de una funcion que calcula el factorial de un numero
print("\033c", end="")

def factorial(n: int) -> int:
    """
    Regresa el factorial de un numero entero
    """
    res =1
    for i in range(1, n + 1):
        res *= i
    return res


def main() -> None:
    print('Dame un numero entero: ')
    n = int(input())
    print(f'El factorial de {n} es: {factorial(n)}')


if __name__ == '__main__':
    main()