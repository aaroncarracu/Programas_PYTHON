# p082-cuadro-hueco-caracter.py
# El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se
# dibujará
print("\033[2J\033[H", end="")
print("Imprimir en la consola un cuadrado hueco\n")
tam= int(input("De que tamaño sera el lado del cuadro? "))
ca= input("¿Qué carácter quieres usar? ")
for i in range(1, tam+1):
    for j in range(1, tam+1):
        if i == 1 or i == tam or j == 1 or j == tam:
            print(ca, end="")
        else:
            print(" ", end="")
    print() 