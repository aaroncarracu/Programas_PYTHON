# p116-conversion-divisas.py
# implemetar un conversor de divisas usando diccionarios a pesos mexicanos
# Definir un diccionario conversiones con las tasas de
# cambio (ej. 'USD', 'EUR', 'GBP', 'JPY', 'CAD') a MXN.
print("\033[2J\033[H", end="")
# definir el diccionario de conversiones
conversiones = {
    "USD": 17.5,
    "EUR": 20.0,
    "GBP": 22.5,
    "JPY": 0.12,
    "CAD": 12.5
}
# Mostrar Opciones: Iterar sobre las llaves del diccionario para mostrar al usuario
# todas las monedas disponibles.
print("Monedas disponibles:")
for moneda in conversiones:
    print(f"- {moneda}") 
#

# Entrada y Validación: Solicitar al usuario la moneda y validar que la moneda
# exista en el diccionario.
cantidad = float(input("Ingrese la cantidad a convertir:  "))
while True:
    divisa_origen = input("ingresa la divisa a convertir: USD , EUR , GBP , JPY , CAD ? ").upper()
    if divisa_origen in conversiones:
        break
    print("Moneda no válida. Intente nuevamente.")
# mostrar resultado final de la conversión a pesos mexicanos
resultado = cantidad * conversiones[divisa_origen]
print(f"\n{cantidad} {divisa_origen} equivalen a {resultado:.2f} MXN")