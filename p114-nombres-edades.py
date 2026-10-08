# p114-nombres-edades.py
# censo de nombres y edades en un diccionario, hasta <enter> vacio
print("\033[2J\033[H", end="")

# crear un diccionario para almacenar los nombres y edades
censo = {}
# Solicitar al usuario que ingrese nombres y edades hasta que ingrese un nombre vacío
while True:
    nombre = input("Ingrese un nombre (o presione <enter> para salir): ")
    if nombre == "":
        break
    censo[nombre] = int(input(f"Ingrese la edad de {nombre}: "))
# mostrar los nombres y edades del censo
print(f"\nCenso de nombres y edades: {censo} - {len(censo)} elementos")

# Mostrar resumen del censo
print("\nResumen del censo")
for nombre, edad in censo.items():
    print(f"  {nombre}: {edad} años")

print() 

suma_edades = sum(censo.values())
promedio_edades = suma_edades / len(censo) if len(censo) > 0 else 0
print(f"Suma de edades: {suma_edades}")
print(f"Promedio de edades: {promedio_edades:.2f}")
