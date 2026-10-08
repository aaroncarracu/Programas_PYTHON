# p115-conversor-unidades.py
# crear un conversor de unidades de longitud
# Definir un diccionario con las unidades de longitud y sus equivalencias en metros
# factores a convertir "km", "m", "cm", "mm"
print("\033[2J\033[H", end="")
unidades = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001
}
# solicitar al usuario que ingrese la unidad de origen, la unidad de destino y el valor a convertir
cantidad=float(input("Ingrese la cantidad a convertir: "))
while True:
    unidad_origen = input("Ingrese la unidad de origen (km, m, cm, mm): ")
    if unidad_origen in unidades:
        break
    print("Unidad de origen no válida. Intente nuevamente.")
# Mostrar los resultados de conversion en metros
metros = cantidad * unidades[unidad_origen]
print("Resultados de la conversión a metros:")
print(f"\n{cantidad} {unidad_origen} equivalen a {metros:.4f} metros")

