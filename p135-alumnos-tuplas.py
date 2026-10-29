# p135-alumnos-tuplas.py
# Modela el siguiente registro escolar como una tupla de alumnos. Cada alumno contiene nombre, carrera y una
# tupla de calificaciones:
print("\033[H\033[J")
alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Maria", "ISC", (10, 9, 10, 10))
)
# Crear y mostrar la tupla externa con los tres registros. Imprimir cuántos alumnos contiene.
print("la tupla externa con los tres registro : ", alumnos)
print("Y Total de alumnos: ", len(alumnos))
# Recorrer los registros mediante desempaquetado y mostrar el nombre, la carrera y el promedio de cada
# alumno con dos decimales.
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre} - {carrera} - {calificaciones} : {promedio:.2f}")
# Construir y mostrar una nueva tupla con pares (nombre, promedio). Identificar e imprimir el alumno con el
# promedio más alto.
# Crear una tupla con pares (nombre, promedio)
pares_promedio = tuple(
    (nombre, sum(calificaciones) / len(calificaciones))
    for nombre, carrera, calificaciones in alumnos
)

print("Tupla de nombres y promedios:")
print(pares_promedio)
mejor_alumno = max(pares_promedio, key=lambda alumno: alumno[1])
print("\nAlumno con el promedio más alto:")
print(f"Nombre: {mejor_alumno[0]}, Promedio: {mejor_alumno[1]:.2f}")
# Consultar las calificaciones usando índices de tuplas anidadas. Para cada alumno, mostrar cuántas veces
# aparece 10 con count() y la posición de la primera calificación con index().
# 2. Consultar calificaciones usando índices anidados
print("\n Consulta de calificaciones:")

for alumno in alumnos:
    nombre = alumno[0]
    calificaciones = alumno[2]

    print(f"\nAlumno: {nombre}")
    print("Calificaciones:", calificaciones)
    print("Cantidad de veces que aparece 10:", calificaciones.count(10))
    print("Posición de la primera calificación:", calificaciones.index(calificaciones[0]))
# Ordenar los pares (nombre, promedio) por promedio de menor a mayor usando sorted() y mostrar el
# resultado como una tupla.
ordenados = tuple(sorted(pares_promedio, key=lambda alumno: alumno[1]))

print("\nAlumnos ordenados por promedio:")
print(ordenados)
# Formar y mostrar una tupla nueva con el nombre "Eva", la carrera "ISC" y las calificaciones (9, 9, 10), sin
# modificar la tupla original de alumnos.
eva = ("Eva", "ISC", (9, 9, 10))

print("\nNueva tupla de Eva:")
print(eva)

print("\nTupla original de alumnos:")
print(alumnos)