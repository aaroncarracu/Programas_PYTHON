# p025-verificar-suma.py
# Dados tres numeros enteros, verifica si la suma de los dos primeros es igual al tercero
print("\033[2J\033[H", end="")
print("Verificar si la suma de los dos primeros es igual al tercero \n")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
if a + b == c:
    print(f'✅ {a} + {b} = {c} SON IGUALES')
else:
    print(f'❌ {a} + {b} = {c} SON DIFERENTES')

print("\n Aqui termina las desiciones ")
