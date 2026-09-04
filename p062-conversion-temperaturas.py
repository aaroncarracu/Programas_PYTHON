# p062-conversion-temperaturas.py
# El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión
# a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.
while True:
    print("\033[2J\033[H", end="")
    print("Conversión de temperaturas de Celsius a Fahrenheit")
    initial_temp = float(input("Introduce la temperatura inicial en Celsius: "))
    final_temp = float(input("Introduce la temperatura final en Celsius: "))

    while initial_temp <= final_temp:
        fahrenheit = (initial_temp * 9/5) + 32
        print(f"{initial_temp:.2f}°C = {fahrenheit:.2f}°F")
        initial_temp += 1
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break

print("\n Proceso terminado...")