# p084-triangulo-invertido-numeros.py
# Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido.
print("\033[2J\033[H", end="")
print("Imprimir Triangulo invertido de numeros \n")
num= int(input("De un numero ? "))
c=0
for i in range(num,0,-1):
    for j in range(1,i+1):
        c+=1
        print(f"{c} ", end="")
    print()
    c=0