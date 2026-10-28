# p132-coordenadas.py
# Registro de coordenadas
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)
# aceso a las tuplas usando indices
print("--- Coordenadas ---")
print("Tipo:", type(zacatecas))
print("Ciudad:", zacatecas[0])
print("Latitud:", zacatecas[1])
print("Longitud:", zacatecas[-1])
ciudad, latitud, longitud = guadalupe
# usando desempaquetado
print("\nCoordenadas de Guadalupe:")
print("Tipo      : ", type(guadalupe))
print("Ciudad    : ", ciudad)
print("Latitud   : ", latitud)
print("Longitud  : ", longitud)
#interaccion sobre las tuplas
for lugar in [zacatecas, guadalupe]:
    print("\nCoordenadas de", lugar[0])
    print("Latitud  : ", lugar[1])
    print("Longitud : ", lugar[2])

_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe
# Calculo del punto medio entre las dos coordenadas
centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print("Punto medio:", centro)

# Verificar pertenencia
print("Zacatecas pertenece a la tupla:", "Zacatecas" in zacatecas)

# Crear otra tupla con datos extra
ampliada = zacatecas + ("México",)

print("Tupla original:", zacatecas)
print("Tupla ampliada:", ampliada)