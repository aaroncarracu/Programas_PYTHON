# p083-rombo-caracter.py
# Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. El
# programa deberá dibujar el rombo utilizando el carácter que el usuario elija.
print("\033[2J\033[H", end="")
print("Imprimir rombo utilizando el carácter que el usuario elija\n")
al= int(input("Dame la aluta del rombo numero impar: "))
s=input("Dame el caracter: ")
espacios=caracteres=0
for i in range(1,al+1):
    espacios=al-i
    caracteres=2*i-1
    for e in range(espacios):
        print(" ", end="")
    for j in range(caracteres):
        print(s, end="")
    print() 
for i in range(al-1,0,-1):
    espacios=al-i
    caracteres=2*i-1
    for e in range(espacios):
        print(" ", end="")
    for j in range(caracteres):
        print(s, end="")
    print() 