# p076-piramide-caracter.py
# Imprime una piramide de caracteres
print("\033[2J\033[H", end="")
print("Imprime una piramide de caracteres \n ")
altura=11
c="*"
esp=0
for i in range(1,altura+1):
    esp= altura-i
    caracter= 2*i-1
    for e in range(esp):
        print(" ", end="")
    for j in range(caracter):
        print(c, end="")
    print()