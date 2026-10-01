# p095-registro-estudiantes.py
# Registro de estudiantes para evento
# Se está organizando un evento y necesitas registrar a los asistentes.
# El programa debe permitir al usuario introducir el nombre y la edad de cada
# persona.
# El registro termina cuando se introduce un * como nombre.
# Al finalizar, el sistema debe mostrar dos informes:
# una lista de todos los asistentes que son mayores de edad (18 años o más).
# y el nombre y la edad de la persona con mayor edad para entregarle un reconocimiento.
print("\033[2J\033[H", end="")
nombres = []
edades = []
# Solicitar nombre y edad de los asistentes
while True:
    nombre = input("Introduce el nombre del asistente (o '*' para terminar): ")
    if nombre == "*":
        break
    try:
        edad = int(input(f"Introduce la edad de {nombre}: ")) # validar que la edad sea un número entero
        nombres.append(nombre)
        edades.append(edad)
    except ValueError: # validar que la edad sea un número entero
        print("Edad inválida. Por favor, introduce un número entero.")
if nombres:
    # filtrar asistentes mayores de edad
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"Asistente mayor de edad: {nombres[i]} - Edad: {edades[i]}")
# encontrar la persona con mayor edad

    max_edad = max(edades)
    indice_max = edades.index(max_edad)
    print(f"\nPersona con mayor edad: {nombres[indice_max]} - Edad: {max_edad}")