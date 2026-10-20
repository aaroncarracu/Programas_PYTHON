# p128-municipios.py
# Gestion de un padron municipal usando conjuntos

municipios = {"Zacatecas", "Guadalupe", "Fresnillo", "Jerez", "Sombrerete",
              "Fresnillo"}

# Borrar pantalla
print("\033[H\033[J")

print("Padron de municipios")
print("--------------------")
print("Municipios registrados:")
print(type(municipios))

for municipio in municipios:
    print(municipio)

# Consultar si un municipio esta registrado
print("¿Esta Zacatecas dentro de los municipios registrados? ",
      "Zacatecas" in municipios)

# Altas al padron de municipios
print("Agregando un municipio al padron")
municipios.add("Calera")

print(f"Municipios registrados: {municipios} - {len(municipios)}")
# Agregar varios municipios al padron
print("\nAgregando varios municipios al padron")
otros = {"Concepcion del Oro", "Jalpa", "Villanueva"}
municipios.update(otros)
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con remove
print("\nEliminando un municipio del padron que es jerez")
municipios.remove("Jerez")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con discard
print("\nEliminando un municipio del padron que es sombrerete")
municipios.discard("Sombrerete")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con pop
print("\nEliminando un municipio del padron al asar")
municipio_eliminado = municipios.pop()
print(f"Municipio eliminado: {municipio_eliminado}")
print(f"Municipios registrados: {municipios} - {len(municipios)}")
# Eliminar todo el padron de municipios
print("\nEliminando todo el padron de municipios")
municipios.clear()
print(f"Municipios registrados: {municipios} - {len(municipios)}")
