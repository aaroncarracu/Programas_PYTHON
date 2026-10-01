# p093-consolidar-ventas.py
# una empresa tiene 2 sucursales y desea consolidar las ventas de cada una de ellas
# se ingresan n ventas para cada sucursal el usuario lo define

ventass1 = []
ventass2 = []
ventas_conso = []
print('\033[H\033[J')
n = int(input("Ingrese el número de ventas para cada sucursal: "))
# Ingresar ventas para la sucursal 1
for i in range(n):
   
        venta = float(input(f"Ingrese la venta {i + 1} para la sucursal 1: "))
        ventass1.append(venta)
# Ingresar ventas para la sucursal 2      
print("\n Ventas para la sucursal 2")
for i in range(n):
        venta = float(input(f"Ingrese la venta {i + 1} para la sucursal 2: "))
        ventass2.append(venta)
# ventas consolidadas
ventas_conso = ventass1 + ventass2
print(f"Ventas consolidadas")
for i, venta in enumerate(ventas_conso, start=1):
    print(f"Venta {i}: {venta}")
# suma de ventas consolidadas
suma_ventas = sum(ventas_conso)
print(f"Suma de ventas consolidadas: {suma_ventas}")