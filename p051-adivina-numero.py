# p051-adivina-numero.py
# Programa que permita adivinar un número entre 1 al 50
import random
print("\033[2J\033[H", end="")
print("Adivina el numero: ")
print("E pensado entre 1 y 50, adivna cual es...")
ns = random.randint(1,50)
ci=0
while True:
    intento = int(input("Cual es?  "))
    ci+=1
    if intento < ns:
        print("Demasiado bajo, intenta con un numero mas alto")
    elif intento > ns:
        print("Demasiado alto, intenta con un numero mas bajo")
    else:
        print(f"Felicidades, adivinaste el numero {ns} en {ci} intentos")
        break
print("\n Proceso terminado...")