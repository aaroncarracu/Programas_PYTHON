# p092-procesar-calificaciones.py
# Procesar n calificaciones en una lista entre 1 y 10 hasta introducir 999
# al final muestra, suma, promedio, la mas alta, la mas baja
# Cuantos alumnos mayores al promedio
# validad que no introduzca letras en lugar de numeros
calfis = []
suma = 0
print('\033[H\033[J') 
while True:
    try:
        calificacion = float(input("Introduce una calificación entre 1 y 10 (999 para terminar): "))
        if calificacion == 999:
            break
        elif 1 <= calificacion <= 10:
            calfis.append(calificacion)
            suma += calificacion
        else:
            print("Calificación inválida. Debe estar entre 1 y 10.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")

if calfis:
    promedio = suma / len(calfis)
    print("Resultados ")
    print(f"Calificaciones ingresadas: {calfis}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Calificación más alta: {max(calfis)}")
    print(f"Calificación más baja: {min(calfis)}")
    mayores_al_promedio = sum(1 for cal in calfis if cal > promedio)
    print(f"Alumnos con calificación mayor al promedio: {mayores_al_promedio}")
else:
    print("No se introdujeron calificaciones válidas.")