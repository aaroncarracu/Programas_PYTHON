# p016-tercer-angulo.py
# Calcular el tercer ángulo de un triángulo
print("\033[2J\033[H", end="")
print("Calcular el tercer ángulo de un triángulo \n")
angulo1 = float(input("dame el valor del ángulo 1: "))
angulo2 = float(input("dame el valor del ángulo 2: "))
angulo3 = 180 - (angulo1 + angulo2)
print(f"El ángulo 1 es: {angulo1}")
print(f"El ángulo 2 es: {angulo2}")
print(f"El ángulo 3 es: {angulo3}")