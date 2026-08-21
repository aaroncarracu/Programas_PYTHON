# p020-numero-suerte.py
#Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos
print("\033[2J\033[H", end="")
print("Escribe un programa que solicite al usuario su año de nacimiento como un número \n")
año = int(input("dame tu año de nacimiento: \n"))
a = año //1000
a1= int(a)
b = (año //100) % 10
c = (año //10) % 10
d = año % 10
suma_numeros = a1 + b + c + d
print(f"El año de nacimiento es   : {año}")
print(f"Los digitos del año son   : {a1}, {b}, {c}, {d}")
print(f"La sumas de los digitos es: {suma_numeros}")