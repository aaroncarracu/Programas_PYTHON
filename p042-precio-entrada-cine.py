# p042-precio-entrada-cine.py
# Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del
# cliente. El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas:
print("\033[2J\033[H", end="")
print("Escribe un programa que solicite la edad, para calcular el precio del boleto")
edad = int (input("Dame la edad de la del cliente: "))
if edad < 5 :
    print("Entra gratis")
elif edad >= 5 and edad <= 12 :
    print("Paga = 5 Pesos")
elif edad >= 13 and edad <= 65 :
    print("Paga = 10 Pesos")
elif edad > 65 :
    print("Paga = 7 Pesos")

print("Proceso terminado..... ")