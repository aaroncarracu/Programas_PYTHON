# p013-funciones-matematicas-precios.py 
# demostrar el uso de funciones matematicas de redondeo
import math as mt
print("\033[2J\033[H", end="")
precio = 15.65
print(f"Precio original         $ {precio:.2f}")
print(f"Redondeo hacia arriba  $ {mt.ceil(precio):.2f}")
print(f"Redondeo hacia abajo   $ {mt.floor(precio):.2f}")
print(f"Truncar                $ {mt.trunc(precio):.2f}")
print(f"Automatico             $ {round(precio):.2f}")
print(f"Automatico decimal     $ {round(precio,3):.2f}")