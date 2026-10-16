# p127-contar-caracteres.py
# Escribe un programa que pida al usuario que ingrese una cadena de texto.
print("\033c", end="")
cadena = input("Dame la cadena a desglozar: ")
# Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
frecuencia = {}

for caracter in cadena:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

print("Frecuencia de cada carácter:", frecuencia)