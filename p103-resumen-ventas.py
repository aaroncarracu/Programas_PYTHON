# p103-resumen-ventas.py
# Trasforma y filtra ventas con comprensión de listas
print("\033[2J\033[H", end="")
print("\033[1;34m"+"Resumen de ventas" + "\033[0m")
ventas = [1000, 2000, 3000, 400, 500]
# Tventas mayores a 1000 aplica 10% de descuento, menores a 1000 un 5% de descuento
ventas_con_descuento = [venta * 0.9 if venta >= 1000 else venta * 0.95 for venta in ventas]
# sacar ventas relevantes mayores a 1000
ventas_relevantes = [venta for venta in ventas_con_descuento if venta >= 1000]
print("Ventas originales:", ventas)
print("Ventas con descuento:", ventas_con_descuento)
print("Ventas relevantes mayores a 1000:", ventas_relevantes)