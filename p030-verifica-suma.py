# p030-verifica-suma.py
# Verificar la suma de dos numeros es igual a un tercero
# 10 20 30   10 30 20    30 20 10
print("\033[2J\033[H", end="")
print("Verificar la suma de dos numeros es igual a un tercero\n")
print("Dame tres numeros enteros separadas por espacio")
n1, n2, n3 = map (int, input().split())

if n1 + n2 == n3:
	print(f"n1 + n2 es igual a n3 : {n1} + {n2} = {n3}")
elif n1 + n3 == n2:
	print(f"n1 + n3 es igual a n2 : {n1} + {n3} = {n2}")
elif n2 + n3 == n1:
	print(f"n2 + n3 es igual a n1 : {n2} + {n3} = {n1}")
else:
	print("Ningun numero es la suma de los otros dos")
