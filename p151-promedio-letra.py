# p151-promedio-letra.py
# dado un promedio regresar la letra correspondiente y un mensaje
print("\033c", end="")

def promedio_a_letra(promedio: float) -> tuple:
    """
    Regresa la letra correspondiente al promedio y un mensaje
    """
    if promedio >= 90 and promedio <= 100:
         letra = 'A'
         mensaje = 'Excelente'
    elif promedio >= 80 and promedio < 90:
         letra = 'B'
         mensaje = 'Bien'
    elif promedio >= 70 and promedio < 80:
         letra = 'C'
         mensaje = 'Suficiente'
    elif promedio >= 60 and promedio < 70:
         letra = 'D'
         mensaje = 'Insuficiente'
    else:
         letra = 'F'
         mensaje = 'Reprobado'
    return letra, mensaje

def main() -> None:
    print('Dame el promedio: ')
    promedio = float(input())
    letra, mensaje = promedio_a_letra(promedio)
    print(f'El promedio {promedio} corresponde a la letra {letra} - {mensaje}')

if __name__ == '__main__':
    main()