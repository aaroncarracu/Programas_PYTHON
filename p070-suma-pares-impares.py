# p070-suma-pares-impares.py
# imprime numeros pares o impares segun el usuario lo decida 
print("\033[2J\033[H", end="")
print("imprime numeros pares o impares segun el usuario lo decida ")
print("[!] voy de 1 a n con pares")
print("[2] voy de 1 a n con impares")
suma =0
op = int(input("Elige? "))
if op == 1:
    print("\n voy de 1 a n con pares")
    n = int (input("Dame el valor de n: "))
    for i in range(2, n+1, 2):
        print(i, end=" ")
        suma = suma +i
    print (f"\n La suma de los pares es igual a: {suma}")
elif op == 2:
    print("\n voy de 1 a n con impares")
    n = int (input("Dame el valor de n: "))
    for i in range(1, n+1, 2):
            print(i, end=" ")
            suma = suma +i
    print (f"\n La suma de los impares es igual a: {suma}")
else: 
    print("\n respuesta incorrecta")
print("\n Proceso terminado..... ") 