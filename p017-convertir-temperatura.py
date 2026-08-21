# p017-convertir-temperatura.py
print("\033[2J\033[H", end="")
print("Convertir temperatura en Celsius a grados Fahrenheit \n")
celsius = float(input("dame el valor en grados Celsius: \n"))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados celsius es   : {celsius:.2f} °C")
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f} °F")