# p009-promedio-de-calificaciones.py
# Calcular promedio de  3 calificaciones ingresados por el usuario
print("\033[2J\033[H", end="")
print("Calculado el promedio de tres calificaciones \n")
# Entrada
print("dame 3 calificaciones separadas por un espacio \n")
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = float(cal1), float(cal2), float(cal3)
suma = cal1 + cal2 + cal3
promedio = (suma) / 3
# Salida
print(f"Las calificaciones son: {cal1}, {cal2}, {cal3}")
print(f"la suma es: {suma:.2f},\nEl promedio de las tres calificaciones es: {promedio:.2f}")