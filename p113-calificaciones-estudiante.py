# p113-calificaciones-estudiante.py
# gestión de calificaciones de un estudiante usando diccionarios
print("\033[2J\033[H", end="")
print("Gestión de calificaciones de un estudiante usando diccionarios \n")
# crear dos listas 1 de calificaciones y otra de materias
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua", "Inglés"]
calificaciones = [8.5, 9.0, 7.5, 8.0, 9.5, 8.5]
# crear un diccionario para almacenar las calificaciones del estudiante
calificaciones_estudiante = dict(zip(materias, calificaciones))

# mostrar las calificaciones del estudiante
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")
# Agregar 2 calificaciones más al diccionario
calificaciones_estudiante["Educación Física"] = 9.0
calificaciones_estudiante["Arte"] = 8.0
# mostrar las calificaciones del estudiante
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")
# Actualizar la calificación de tres materias
calificaciones_estudiante["Matemáticas"] = 9.0
calificaciones_estudiante["Física"] = 8.5
calificaciones_estudiante["Química"] = 8.0
# mostrar las calificaciones del estudiante
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")
# eliminar 2 calificaciones del diccionario usando pop
calificaciones_estudiante.pop("Química")
calificaciones_estudiante.pop("Lengua")
print(f"Calificaciones del estudiante: {calificaciones_estudiante} - {len(calificaciones_estudiante)} elementos")
# Mostrar el par llave-valor de las calificaciones del estudiante, y promedio de calificaciones
print("Llaves y valores del diccionario")
total=0
for materia, calificacion in calificaciones_estudiante.items():
    print(f"  {materia}: {calificacion}")
    total += calificacion
promedio = total / len(calificaciones_estudiante)
print(f"Promedio de calificaciones: {promedio:.2f}")
