# p120-reporte-ventas.py
# # Cada compra registra el nombre del cliente, el producto, la cantidad y el precio.
# Cada compra debe ser un diccionario almacenado en una lista de compras.

compras = []

# Borrar el contenido anterior de la pantalla de la consola.
print("\033c", end="")

# Mostrar el título del registro de compras de la tienda.
print("\nRegistro de compras de la tienda\n")

# Solicitar al usuario el número de compras que desea registrar.
n = int(input("Ingrese el número de compras a registrar: "))

# Recorrer el número de compras que se van a registrar.
for i in range(1, n + 1):
    # Mostrar el número de la compra que se está registrando.
    print(f"\nCompra {i}:")

    # Crear un diccionario con los datos de la compra.
    compra = {
        # Solicitar el nombre del cliente que realiza la compra.
        "cliente": input("Nombre: "),

        # Solicitar el nombre del producto comprado.
        "producto": input("Producto: "),

        # Solicitar la cantidad de unidades compradas y convertirla a entero.
        "cantidad": int(input("Cantidad: ")),

        # Solicitar el precio del producto y convertirlo a número decimal.
        "precio": float(input("Precio: "))
    }

    # Agregar el diccionario de la compra a la lista de compras.
    compras.append(compra)

# Mostrar todas las compras registradas y la cantidad de elementos almacenados.
print(f"\nTodas las compras: {compras} - {len(compras)} elementos")
# Consolidar las compras por cliente.
# Al final, quiero saber el total de productos y el dinero gastado por cada cliente.

clientes = {}

for compra in compras:
    cliente = compra["cliente"]

    if cliente not in clientes:
        clientes[cliente] = {
            "total_productos": 0,
            "total_gastado": 0.0
        }

    clientes[cliente]["total_productos"] += compra["cantidad"]
    clientes[cliente]["total_gastado"] += compra["cantidad"] * compra["precio"]


# Mostrar el reporte consolidado por cliente.
print("\nReporte consolidado por cliente:")
for cliente, datos in clientes.items():
    print(f"Cliente: {cliente}")
    print(f"  Total productos comprados: {datos['total_productos']}")
    print(f"  Total gastado: ${datos['total_gastado']:.2f}\n")
print("\n Diccionario de clientes con totales: ")
print(clientes)
