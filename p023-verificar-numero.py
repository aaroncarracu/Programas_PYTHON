# p023-verificar-numero.py
# Cear un programa que verifique si el numero ingresado es positivo, negativo o cero.
print("\033[2J\033[H", end="")
print("Verificar si un número es positivo, negativo o cero \n")
numero = float(input("Ingrese un número: "))
if numero > 0 :
    print("El numero ingresado es positivo. 👍")
else:
    if numero < 0 :
        print("El numero ingresado es negativo. 👎")
    else:
        print("El numero ingresado es cero. 🤔")

print("\n Aqui termina las desiciones ")
