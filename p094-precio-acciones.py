# p094-precio-acciones.py
# Análisis de precios de acciones diarias
#• Dada una lista de precios de cierre de una acción durante la semana,
#• Encontrar el precio más alto, el más bajo y el día en que ocurrieron.
print("\033[2J\033[H", end="")
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
precios = [150.25, 152.30, 149.80, 151.00, 153.45, 154.10, 150.75]
precio_max = max(precios)
precio_min = min(precios)
indice_max = precios.index(precio_max)
indice_min = precios.index(precio_min)

print("Análisis de precios de acciones diarias")
print(f"Precio más alto: {precio_max} - Día: {dias[indice_max]}")
print(f"Precio más bajo: {precio_min} - Día: {dias[indice_min]}")