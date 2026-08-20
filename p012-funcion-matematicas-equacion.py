# p012-funcion-matematicas-equacion.py 
# Ejemplifica el uso de funciones matematicas dentro de math

import math as mt
print("\033[2J\033[H", end="")
x= float(input("dame el valor de x: "))
y= float(input("dame el valor de y: "))
fxy = 3*mt.pow(x,2) + mt.sqrt(mt.pow(x,2)+mt.pow(y,2))+ mt.exp(mt.log(x))
print(f"el resultado es: {fxy:,.2f}")
