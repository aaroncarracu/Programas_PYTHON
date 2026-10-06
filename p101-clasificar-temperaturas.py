# p101-clasificar-temperaturas.py
# clasfica temperaturas en grados centigrados en frio, templado y caliente usando comprensión de listas
print("\033[2J\033[H", end="")
print("\033[1;34m"+"Clasificar temperaturas" + "\033[0m")
temperaturas = [0, 15, 22, 28, 35, 40]
# Clasificar temperaturas en grados centigrados en frio, templado y caliente usando comprensión de listas
clasificacion = ["frio" if temp < 20 else "templado" if temp <= 30 else "caliente" for temp in temperaturas]
print("Temperaturas:", temperaturas)
print("Clasificación:", clasificacion)
