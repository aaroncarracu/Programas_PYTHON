# p039-numeros-romanos.py
# Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en
# números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.
print("\033[2J\033[H", end="")
print("Escribe un programa que solicite un número entero del 1 al 10 y muestre numero equivalente en romano \n")
num = int (input("Dame el numero entero entre 1 a 10: "))
if num == 1 :
    print(f"El numero {1} es el numero romano: I")
elif num == 2 :
    print(f"El numero {2} es el numero romano: II")
elif num == 3 :
    print(f"El numero {3} es el numero romano: III")
elif num == 4 :
    print(f"El numero {4} es el numero romano: IV")
elif num == 5 :
    print(f"El numero {5} es el numero romano: V")
elif num == 6 :
    print(f"El numero {6} es el numero romano: VI")
elif num == 7 :
    print(f"El numero {7} es el numero romano: VII")
elif num == 8 :
    print(f"El numero {8} es el numero romano: VIII")
elif num == 9 :
    print(f"El numero {9} es el numero romano: IX")
elif num == 10 :
    print(f"El numero {10} es el numero romano: X")
else :
    print("Error esta fuera de rango")
print("\n Proceso terminado... ")