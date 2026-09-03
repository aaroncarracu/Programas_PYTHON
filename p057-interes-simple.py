# p057-interes-simple.py
# calcular los años necesarios para alcanzar un meta de ahorro
print("\033[2J\033[H", end="")
print("Calcular los años necesarios para alcanzar un meta de ahorro \n")
ca = float(input("capital inicial:  "))
ti = float(input("tasa de interes anual (%):  "))
ma = float(input("meta de ahorro:  "))

años = iaf = 0
td = (ti / 100)

while ca < ma:
    iaf = ca * td
    ca += iaf
    años += 1
print(f"Para llegar a {ma} deben pasar {años} años, el capital es {ca}")
