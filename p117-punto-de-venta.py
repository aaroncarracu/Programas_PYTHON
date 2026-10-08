# p117-punto-de-venta.py
# crear un sistema simple de punto de venta (pos) para un puesto de comida

print("\033[2J\033[H", end="")
# crear un diccionario para almacenar los productos y sus precios
productos = {
    "Hamburguesa": 5.0,
    "Papas fritas": 2.5,
    "Refresco": 1.5,
    "HOT DOG": 3.0,
    "Pizza": 8.0
}
#Mostrar menu de productos disponibles
print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"- {producto}: ${precio:.2f}")
#Tomar Orden: Preguntar al usuario qué desea ordenar en un bucle.
#• Si el producto no está en el menú, informarle.
#• Si el producto existe, solicitar la cantidad.
orden = {}
while True:
    producto = input("Ingrese el producto que desea ordenar (o presione <enter> para finalizar): ")
    if producto == "":
        break
    if producto not in productos:
        print("Producto no disponible. Intente nuevamente.")
        continue
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    if producto in orden:
        orden[producto] += cantidad
    else:
        orden[producto] = cantidad
# mostrar un recibo con el subtotal por producto y el total general de la compra.
print("\nRecibo:")
total_general = 0
for producto, cantidad in orden.items():
    subtotal = cantidad * productos[producto]
    print(f"- {producto}: {cantidad} x ${productos[producto]:.2f} = ${subtotal:.2f}")
    total_general += subtotal
print(f"\nTotal general: ${total_general:.2f}")
