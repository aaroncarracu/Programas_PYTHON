# p010-operaciones-matematicas.py 
# Demuestra el uso de operadores aritmeticos 
print("\033[2J\033[H", end="")
print("-"*50)
print("calculadora de operadores aritmeticos \n")
print("-"*50)
x = float(input("dame un numero: "))
y = float(input("dame otro numero: "))

suma = x + y
resta = x-y 
multi= x*y
div = x/y
mod = x % y
pot = x**y
dive = x//y
print ("Resultados de las operaciones realizadas \n")
print("="*50)
print(f"Numeros           : {x}, {y}")
print(f"La suma           : {suma:>15.2f}")
print(f"La resta          : {resta:>15.2f}")
print(f"La multiplicación : {multi:>15.2f}")
print(f"La división       : {div:>15.2f}")
print(f"El módulo         : {mod:>15.2f}")
print(f"La potencia       : {pot:>15.2f}")
print(f"La división entera: {dive:>15.2f}")
print("="*50)
