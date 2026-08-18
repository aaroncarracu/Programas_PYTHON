# p006-conversor-temperatura.py
# calcular una temperatura de Celsius a Fahrenheit
print("\033[2J\033[H", end="")
print("calculando la temperatura de Celsius a Fahrenheit \n")
celsius = float(input("ingresa la temperatura en Celsius "))
fahrenheit = (celsius * 9/5) + 32
print(f"la temperatura en Fahrenheit es: {fahrenheit:.2f}")