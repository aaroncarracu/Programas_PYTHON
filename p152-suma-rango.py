# p152-suma-rango.py
# Funcion que suma los valores en el rango ini ... fin
# 1 ... 5 = 1 + 2 + 3 + 4 + 5 = 15

def suma_rango(ini: int, fin: int) -> int:
    """ Regresa la suma de los valores en el rango ini ... fin """
    suma = 0
    for i in range(ini, fin + 1):
        suma += i
    return suma


def main() -> None:
    print('Dame el valor inicial del rango: ')
    ini = int(input())

    print('Dame el valor final del rango: ')
    fin = int(input())

    print(f'La suma de los valores en el rango {ini} ... {fin} es: {suma_rango(ini, fin)}')


if __name__ == '__main__':
    main()