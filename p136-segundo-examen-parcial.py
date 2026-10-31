# p136-segundo-examen-parcial.py
# Se desea procesar el registro de vuelos de una aerolínea ("AeroRegistro").
# Crear una lista vacía para almacenar los vuelos
print("\033[H\033[J")
vuelos = []
vuelos_conjunto = set()
registro_historico = []
# Variable de control
continuar = "s"

# Ciclo while para capturar los vuelos
while continuar.lower() == "s":
    # Al terminar la captura (ej. cuando el usuario ingrese un número de vuelo vacío o "*"), el programa deberá
    # procesar las colecciones e imprimir:
    numero = input("Numero de vuelo (* para terminar): ")

    if numero == "" or numero == "*":
        break
    # Crear un diccionario para cada vuelo
    vuelo = {}

    # Solicitar los datos del vuelo
    vuelo["numero_vuelo"] = numero
    vuelo["origen"] = input("Ciudad de origen: ")
    vuelo["destino"] = input("Ciudad de destino: ")
    vuelo["aerolinea"] = input("Nombre de la aerolínea: ")
    vuelo["pasajeros"] = int(input("Número de pasajeros: "))
    vuelo["tarifa"] = float(input("Precio del boleto: $"))

    # Agregar el diccionario a la lista
    vuelos.append(vuelo)
    # conjuntos

    # Preguntar si desea registrar otro vuelo
    continuar = input("\n¿Deseas registrar otro vuelo? (s/n): ")
# Los datos se deben almacenar en una lista, donde cada elemento de la lista sea un diccionario con los
# datos de un vuelo.

# Mostrar todos los vuelos registrados
print("\n===== LISTA DE VUELOS REGISTRADOS =====")

for vuelo in vuelos:
    print(vuelo)
    # Obtener el destino de cada vuelo
    vuelos_conjunto.add(vuelo["destino"])
    # Crear una tupla con los tres datos solicitados
    registro = (
        vuelo["numero_vuelo"],
        vuelo["aerolinea"],
        vuelo["destino"]
    )

    # Agregar la tupla a la lista
    registro_historico.append(registro)
    

# Mostrar los destinos únicos
print("\n Destinos únicos:", vuelos_conjunto)

# Mostrar el registro histórico
print("\n Registro histórico:", registro_historico)

print("\n Tabla de datos:")
print("No. Vuelo  | Origen           | Destino        | Aerolínea   | Pasajeros   | Tarifa |")
print("-" * 95)
# Contar vuelos por aerolinea
conteo_aerolineas = {}
# Contar vuelos por ciudad de destino
conteo_destinos = {}
total_vuelos = len(vuelos)
# Recorrer la lista de diccionarios
for vuelo in vuelos:
    aerolinea = vuelo["aerolinea"]
    conteo_aerolineas[aerolinea] = conteo_aerolineas.get(aerolinea, 0) + 1
    destino = vuelo["destino"]
    conteo_destinos[destino] = conteo_destinos.get(destino, 0) + 1
    print(f"{vuelo['numero_vuelo']:<10} | "
          f"{vuelo['origen']:<18} | "
          f"{vuelo['destino']:<15} | "
          f"{vuelo['aerolinea']:<12} | "
          f"{vuelo['pasajeros']:<10} | "
          f"${vuelo['tarifa']:,.2f}")


print("\nDatos relevantes ")
print("Total de vuelos:", total_vuelos)
print("\nVuelos por aerolinea:")

for aerolinea, cantidad in conteo_aerolineas.items():
    print(aerolinea, ":", cantidad)
print("\nVuelos por destino:")

for destino, cantidad in conteo_destinos.items():
    print(destino, ":", cantidad)
# Suma y promedio de pasajeros
suma_pasajeros = sum(vuelo["pasajeros"] for vuelo in vuelos)

if total_vuelos > 0:
    promedio_pasajeros = suma_pasajeros / total_vuelos
else:
    promedio_pasajeros = 0

print("\nPasajeros:")
print("Suma:", suma_pasajeros)
print("Promedio:", round(promedio_pasajeros, 2))


# Suma y promedio de tarifas
suma_tarifas = sum(vuelo["tarifa"] for vuelo in vuelos)

if total_vuelos > 0:
    promedio_tarifas = suma_tarifas / total_vuelos
else:
    promedio_tarifas = 0

print("\nTarifas:")
print("Suma: $", round(suma_tarifas, 2))
print("Promedio: $", round(promedio_tarifas, 2))


# Vuelo mas caro y mas barato
if total_vuelos > 0:

    vuelo_caro = max(vuelos, key=lambda vuelo: vuelo["tarifa"])

    vuelo_barato = min(vuelos, key=lambda vuelo: vuelo["tarifa"])

    print("\nVuelo mas caro:")
    print(vuelo_caro["numero_vuelo"], "- $", vuelo_caro["tarifa"])

    print("\nVuelo mas barato:")
    print(vuelo_barato["numero_vuelo"], "- $", vuelo_barato["tarifa"])

else:
    print("\nNo hay vuelos registrados para calcular tarifas.")