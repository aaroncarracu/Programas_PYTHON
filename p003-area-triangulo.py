# p003-area-triangulo.py
# calcular el area de un triangulo
print("\033[2J\033[H", end="")
print ("calculando el area de un triangulo \n")
print ("Dame la base y la altura del triangulo separadas por <Enter>")
base, altura = int(input()), int(input())
area = (base * altura) / 2
print (f"el triangulo de base {base} y altura {altura}, tiene una area de {area:.2f}")