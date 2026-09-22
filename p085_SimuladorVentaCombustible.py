# p085_SimuladorVentaCombustible.py
# El programa debe permitir a los operadores
# realizar cálculos de ventas, proyecciones de rendimiento y categorización de
# clientes mediante un flujo lógico robusto.
print("\033[2J\033[H", end="")
# Variables iniciales y precios base por litro
precio_magna = 24.50
precio_premium = 26.80
precio_diesel = 25.90

# Ciclo infinito
while True:
    # Despliegue del menú principal
    print("==========================================")
    print("         SISTEMA INTERACTIVO GASOLINERA   ")
    print("==========================================")
    print("1. Venta de Combustible")
    print("2. Simulación de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")
    print("------------------------------------------")
    try:
        opcion = int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("\nError: Debe ingresar un número entero válido.\n")
        continue  # Reinicia el ciclo para volver a pedir la opción

    # Validar opción fuera de rango
    if opcion < 1 or opcion > 4:
        print("\nError: Opción inválida. Intente de nuevo.\n")
        continue

    # --------------------------------------------------
    # OPCIÓN 1: VENTA DE COMBUSTIBLE
    # --------------------------------------------------
    if opcion == 1:
        print("\n==========================================")
        print("           VENTA DE COMBUSTIBLE           ")
        print("==========================================")
        print("1. Magna   ($24.50/L)")
        print("2. Premium ($26.80/L)")
        print("3. Diésel  ($25.90/L)")
        print("------------------------------------------")
        
        tipo = int(input("Seleccione el tipo de combustible (1-3): "))
        
        if tipo < 1 or tipo > 3:
            print("Error: Tipo de combustible no válido.\n")
            continue

        litros = float(input("Ingrese la cantidad de litros a cargar: "))
        
        if litros <= 0:
            print("Error: La cantidad de litros debe ser mayor a 0.\n")
            continue

        nombre_combustible = ""
        precio_unitario = 0.0

        if tipo == 1:
            nombre_combustible = "Magna"
            precio_unitario = precio_magna
        elif tipo == 2:
            nombre_combustible = "Premium"
            precio_unitario = precio_premium
        elif tipo == 3:
            nombre_combustible = "Diésel"
            precio_unitario = precio_diesel

        total = litros * precio_unitario

        # Tabla alineada de recibo de venta
        print("\n+--------------------+-----------+---------------+")
        print(f"| {'COMBUSTIBLE':<18} | {'LITROS':<9} | {'TOTAL ($)':<13} |")
        print("+--------------------+-----------+---------------+")
        print(f"| {nombre_combustible:<18} | {litros:<9.2f} | ${total:<12.2f} |")
        print("+--------------------+-----------+---------------+")

        # Pago y cálculo con operadores // y %
        pago = float(input("\nIngrese el monto con el que paga ($): "))
        if pago >= total:
            cambio_entero = int(pago - total)
            billetes_100 = cambio_entero // 100       # Operador de división entera //
            sobrante = cambio_entero % 100 
            print("-"*40)           
            print(f"Litros totales: ${litros:.2f}")
            print(f"Cantidad a Pagar: ${total:.2f}")
            print(f"Cambio total: ${pago - total:.2f}")
            print("-"*40)   
        else:
            print("Monto insuficiente para completar la venta.")

    # --------------------------------------------------
    # OPCIÓN 2: SIMULACIÓN DE RENDIMIENTO
    # --------------------------------------------------
    elif opcion == 2:
        print("\n==========================================")
        print("        SIMULACIÓN DE RENDIMIENTO         ")
        print("==========================================")
        rendimiento = float(input("Ingrese el rendimiento base de su auto (km/L): "))
        
        if rendimiento <= 0:
            print("Error: El rendimiento debe ser mayor a 0.\n")
            continue

        print("\n+--------------------+------------------+------------------+")
        print(f"| {'DISTANCIA (KM)':<18} | {'LITROS NEC.':<16} | {'COSTO EST. ($)':<16} |")
        print("+--------------------+------------------+------------------+")

        # Ciclo for con range() y operador de potencia **
        for distancia in range(100, 501, 100):
            # Factor de resistencia progresivo aplicado con exponente **
            factor_resistencia = 1 + (distancia / 1000) ** 2
            rendimiento_ajustado = rendimiento / factor_resistencia
            
            litros_necesarios = distancia / rendimiento_ajustado
            costo_estimado = litros_necesarios * precio_magna
            print(f"| {distancia:<18} | {litros_necesarios:<16.2f} | ${costo_estimado:<15.2f} |")

        print("+--------------------+------------------+------------------+")
        print("* Incluye factor de resistencia (potencia **) y tarifa Magna ($22.50/L)")

    # --------------------------------------------------
    # OPCIÓN 3: CLASIFICADOR DE CLIENTE
    # --------------------------------------------------
    elif opcion == 3:
        print("\n==========================================")
        print("         CLASIFICADOR DE CLIENTE          ")
        print("==========================================")
        monto_compra = float(input("Ingrese el monto gastado en la compra ($): "))
        
        if monto_compra <= 0:
            print("Error: El monto ingresado debe ser mayor a 0.\n")
            continue

        if monto_compra < 100:
            categoria = "Regular"
        elif monto_compra > 500:
            categoria = "Flotilla"
        else:
            categoria = "Premium"
        
        print("\n+------------------+-------------------+")
        print(f"| {'MONTO TOTAL ($)':<16} | {'CATEGORÍA':<17} |")
        print("+------------------+-------------------+")
        print(f"| ${monto_compra:<15.2f} | {categoria:<17} |")
        print("+------------------+-------------------+")

    # --------------------------------------------------
    # OPCIÓN 4: SALIR
    # --------------------------------------------------
    elif opcion == 4:
        print("\nGracias por utilizar el sistema. ¡Hasta luego!")
        break

    print()