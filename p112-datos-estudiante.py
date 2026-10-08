# p112-datos-estudiante.py
# gestión de datos de un estudiante usando diccionarios

print("\033[2J\033[H", end="")
print("Gestión de datos de un estudiante usando diccionarios \n")
# crear un diccionario para almacenar los datos de un estudiante
estudiante = {
    "nombre": "Juan Pérez",
    "edad": 20,
    "carrera": "Ingeniería en Sistemas",
    "email": "juan.perez@example.com"
}
# mostrar los datos del estudiante
print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")
# cambiar el la edad del estudiante
estudiante["edad"] = 21
print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")
# agregar un nuevo dato al diccionario
estudiante["promedio"] = 8.5
print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")
# mostrar llaves del diccionario
print("LLaves del diccionario")
for key in estudiante.keys():
    print(f"  {key}")
# mostrar valores del diccionario
print("Valores del diccionario")
for value in estudiante.values():
    print(f"  {value}")
# mostrar llaves y valores del diccionario
print("Llaves y valores del diccionario")
for key, value in estudiante.items():
    print(f"  {key}: {value}")