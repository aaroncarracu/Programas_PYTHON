# p021-distancia-entre-puntos.py
# Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano
import math as mt
print("\033[2J\033[H", end="")
print("Calcular la distancia entre dos puntos en el plano cartesiano \n")
x1 = float(input("dame la coordenada x del primer punto: \n"))
y1 = float(input("dame la coordenada y del primer punto: \n"))
x2 = float(input("dame la coordenada x del segundo punto: \n"))
y2 = float(input("dame la coordenada y del segundo punto: \n"))
d= mt.sqrt(mt.pow(x2-x1,2)+ mt.pow(y2-y1,2))
print("Los puntos son:")
print(f"({x1}, {y1}) y ({x2}, {y2})")
print(f"La distancia entre los dos puntos es: {d:.3f}")