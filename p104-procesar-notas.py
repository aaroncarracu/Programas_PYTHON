# p104-procesar-notas.py
# Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzca
# un 0. Validar que todas las notas introducidas estén dentro del rango [0,100].
print("\033[2J\033[H", end="")
notas = []
while True:
    nota = float(input("Ingrese una nota (0 para finalizar): "))
    if nota == 0:
        break
    if nota < 0 or nota > 100:
        print("Nota inválida. Debe estar entre 0 y 100.")
        continue
    notas.append(nota)
# Calcular e imprimir:
# ● Cuántas notas se introdujeron.
# ● La lista de notas completa.
# ● La suma y el promedio de las notas.
# ● La nota máxima y la nota mínima.
# ● Cuántas notas y cuáles son las notas menores al promedio.
# nota maxima y minima, notas menores al promedio, lista de notas menores al promedio
suma=promedio=0
for nota in notas:
    suma += nota
promedio = suma / len(notas) if len(notas) > 0 else 0
nota_maxima = max(notas) if len(notas) > 0 else 0
nota_minima = min(notas) if len(notas) > 0 else 0
notas_menores_al_promedio = [nota for nota in notas if nota < promedio]

print(f"Se introdujeron {len(notas)} notas.")
print(f"Lista de notas: {notas}")
print(f"Suma de notas: {suma}")
print(f"Promedio de notas: {promedio}")
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")
print(f"Notas menores al promedio: {len(notas_menores_al_promedio)}")
print(f"Lista de notas menores al promedio: {notas_menores_al_promedio}")
