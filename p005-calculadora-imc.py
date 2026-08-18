# p005-calculadora-imc.py
# Indice de masa colporal de una person
print("\033[2J\033[H", end="")
print ("calculadora de la masa corporal el IMG \n")

peso_kg = float(input("ingresa el peso en kilogramos "))
altura_m = float(input("ingresa la altura en metros "))
img = peso_kg / (altura_m ** 2)
print(f"si tu altura es {altura_m} metros, y tu peso es {peso_kg} kilogramos, tu IMC es = {img:.2f}")
