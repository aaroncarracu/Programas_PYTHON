# p037-numero-mayor.py
# Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.
print("\033[2J\033[H", end="")
print("Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor \n")

n1 = int(input("Dame el primer numero : "))
n2 = int(input("Dame el segundo numero: "))
n3 = int(input("Dame el tercer numero : "))
if n1 > n2 and n1 > n3 :
    print (f"De los numeros {n1},{n2},{n3} el mayor es: n1= {n1} ")
elif n2 > n1 and n2 > n3 :
    print (f"De los numeros {n1},{n2},{n3} el mayor es: n2= {n2} ")
else :
    print (f"De los numeros {n1},{n2},{n3} el mayor es: n3= {n3} ")

print ("\n Proceso terminado..... ")