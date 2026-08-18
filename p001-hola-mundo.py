# p001-hola-mundo.py
# Lee datos y envia un saludo 
print("leyendo datos y eviando un saludo")
# leer datos
print("\033[2J\033[H", end="") # limpiar pantalla
nombre = input("ingresa tu nombre:")
edad = int(input("ingresa tu edad:"))
peso = float(input("ingresa tu peso:"))
print(f"{nombre}, Bienvenido a Python, tu edad es {edad}, tu peso es {peso}")
print(nombre + " bienvenido a python, tu edad es " + str(edad) + ", tu peso es " + str(peso))