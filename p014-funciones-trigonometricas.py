# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonometricas 
import math as mt
print("\033[2J\033[H", end="")
print("Demostrar el uso de funciones trigonometricas \n")
angulo = int(input("dame el angulo en grados: "))
radianes = mt.radians(angulo)
seno =mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)
grados = mt.degrees(radianes)
salida = (" Resumen de funciones trigonometricas y conversiones \n"
f"El seno es: {seno:.4f}\n"
f"El coseno es: {coseno:.4f}\n"
f"La tangente es: {tangente:.4f}\n"
f"El angulo en grados es: {grados:.4f} grados,  equivale a {radianes:.4f} radianes\n"
)
print(salida)