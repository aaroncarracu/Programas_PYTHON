# p011-operadores-asignacion.py
# ejemplificar el uso de operadores de asignacion
print("\033[2J\033[H", end="")
print("Operadores de asignacion en PYTHON \n")

x =float(input("dame el valor de x: "))
x+= 5
print(f"Suma 5 a x         : {x} ")
x-= 3
print(f"Resta 3 a x        : {x}")
x*= 2
print(f"multiplica x por 2 : {x}")
x/= 4
print(f"divide x entre 4   : {x}")
x%= 4
print(f"modulo de x entre 4: {x}")
x**= 2
print(f"pot de x elev a 2  : {x}")
x//= 2
print(f"div entera entre 2 : {x}")
