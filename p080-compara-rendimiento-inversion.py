# p080-compara-rendimiento-inversion.py
# Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años.
print("\033[2J\033[H", end="")
print("Imprimir el crecimiento de dos fondos de inversión a lo largo de varios años. \n")
fa = int(input("Fondo de Inversión A monto inicial "))
tia = float(input("Tasa de interés anual fondo A (%): "))
fb = int(input("Fondo de Inversión B monto inicial "))
tib = float(input("Tasa de interés anual fondo B (%): "))
años = int(input("Años de inversion"))
gan1=tia/100
a=b=0
print("Comparación de Rendimientos Anuales \n")
print("Año       Fondo A             Fondo B ")
print("-"*40)
for i in range(1,años+1):
    fa+=((fa*tia)/100)
    fb+=((fb*tib)/100)
    print(f"{i} {"$":>8}{fa:>9.2f} {"$":>10}{fb:>8.2f}\n")
if fa>fb :
   print(f"Resultado final: el Fondo A {fa:.2f} es superó al Fondo B {fb:.2f}")
else:
   print(f"Resultado final: el Fondo B {fb:.2f} es superó al Fondo A {fa:.2f}") 