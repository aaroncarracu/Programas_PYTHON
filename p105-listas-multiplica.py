# p105-listas-multiplica.py
#Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las
# dos listas correspondientes. Imprimir las tres listas.
print("\033[2J\033[H", end="")
lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    num1 = float(input(f"Ingrese el elemento {i+1} de la primera lista: "))
    lista1.append(num1)
for i in range(5):
    num2 = float(input(f"Ingrese el elemento {i+1} de la segunda lista: "))
    lista2.append(num2)
for i in range(5):
    lista3.append(lista1[i] * lista2[i])
print(f"Primera lista: {lista1}")
print(f"Segunda lista: {lista2}")
print(f"Tercera lista: {lista3}")
