# p134-coordenadas-tuplas.py
# Representa mediante tuplas las coordenadas de las siguientes ciudades:
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)
print("\033[H\033[J")
# Crear y mostrar las tuplas de Zacatecas y Guadalupe. Imprimir su tipo y consultar el nombre, la latitud y la
# longitud usando índices positivos y negativos.
print("Tipo:", type(zacatecas))
print("Ciudad:", zacatecas[0])
print("Latitud:", zacatecas[1])
print("Longitud:", zacatecas[-1])
print("\nDatos de Guadalupe usando índices positivos:")
print("Nombre:", guadalupe[0])
print("Latitud:", guadalupe[1])
print("Longitud:", guadalupe[2])
# Consultar los datos usando índices negativos
print("\nDatos de Zacatecas usando índices negativos:")
print("Nombre:", zacatecas[-3])
print("Latitud:", zacatecas[-2])
print("Longitud:", zacatecas[-1])

# Desempaquetar las tuplas en variables
nombre_z, latitud_z, longitud_z = zacatecas
nombre_g, latitud_g, longitud_g = guadalupe

# Imprimir las coordenadas con el formato solicitado
print("\nCoordenadas de las ciudades:")
print(f"{nombre_z}: ({latitud_z}, {longitud_z})")
print(f"{nombre_g}: ({latitud_g}, {longitud_g})")

# Guardar ambas ubicaciones en una tupla
ciudades = (zacatecas, guadalupe)

# Recorrer las ubicaciones y mostrar el nombre y las coordenadas
# obtenidas mediante slicing
print("\nRecorrido de las ubicaciones usando slicing:")
for ciudad in ciudades:
    nombre = ciudad[0]
    coordenadas = ciudad[1:3]
    print(f"{nombre}: {coordenadas}")
latitud_media = (zacatecas[1] + guadalupe[1]) / 2
longitud_media = (zacatecas[2] + guadalupe[2]) / 2

print("\nPunto medio aproximado entre las dos ciudades:")
print(f"Coordenadas: ({latitud_media}, {longitud_media})")

# Crear una nueva tupla para Zacatecas que incluya el código "ZAC"
zacatecas_nuevo = zacatecas + ("ZAC",)

print("\nTupla original de Zacatecas:", zacatecas)
print("Nueva tupla de Zacatecas:", zacatecas_nuevo)

# Comprobar que la tupla original no cambió
print("¿La tupla original sigue igual?:", zacatecas == ("Zacatecas", 22.77, -102.58))

# Verificar si "Zacatecas" pertenece a su tupla
print("\n¿'Zacatecas' pertenece a su tupla?:", "Zacatecas" in zacatecas)