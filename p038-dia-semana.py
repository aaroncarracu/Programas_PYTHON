# p038-dia-semana.py
# Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana
# correspondiente, considerando que 1 es domingo y 7 es sábado.
print("\033[2J\033[H", end="")
print("Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana \n")
dia = int (input("Dame el numero entero entre 1 a 7: "))
if dia == 1 :
    print("El dia es Domingo")
elif dia == 2 :
    print("El dia es Lunes")
elif dia == 3 :
    print("El dia es Martes")
elif dia == 4 :
    print("El dia es Miercoles")
elif dia == 5 :
    print("El dia es Jueves")
elif dia == 6 :
    print("El dia es Viernes")
elif dia == 7 :
    print("El dia es Sabado")
else :
    print("Error esta fuera de rango")
print("\n Proceso terminado... ")