# p126-procesar-diccionario.py
# p126-procesar-diccionario.py
print("\033c", end="")
# o nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
# o sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
# Crea un diccionario nómina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).
nomina = dict(zip(nombres, sueldos))
# Muestra el diccionario nómina resultante.
print(f"\nTodos el diccionario de nomina: {nomina} - {len(nomina)} elementos")
# Itera sobre el diccionario y muestra su contenido de cuatro formas:
# o Mostrando solo las llaves (usando keys()).
print("\n Mostrando solo las llaves (usando keys())")
for nombre in nomina.keys():
    print(nombre)
# Mostrando solo los valores (usando values()).
print("\n Mostrando solo los valores (usando values())")
for sueldos in nomina.values():
    print(sueldos)
print("\nIterando por las llaves y accediendo al valor (ej. for llave in dic: ...).")
for llave in nomina:
    print(llave, nomina[llave])
print("\nMostrando la llave y el valor simultáneamente (usando items()).")
for llave, valor in nomina.items():
    print(f"({llave}, {valor})")
# ● Calcula y muestra la suma total de los sueldos.
# ● Calcula y muestra el promedio de los sueldos.
total = sum(nomina.values())
promedio = total / len(nomina)
print("Suma total de los sueldos:", total)
print("Promedio de los sueldos:", promedio)