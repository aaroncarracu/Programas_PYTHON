# p106-mes-día-nombre.py
# Guardar los días de cada mes en una lista y los nombres de los meses en otra
#lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente
print("\033[2J\033[H", end="")
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
introducido = int(input("Ingrese un número de mes (1-12): "))
if 1 <= introducido <= 12:
    i = introducido - 1
    print(f"{meses[i]} tiene {dias[i]} días.")
else:
    print("Número de mes inválido.")