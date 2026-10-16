# p125-eliminar-diccionario.py
# Crea un diccionario municipios con los datos: Apozol: 1863, Calera: 1868, Fresnillo: 1554, Guadalupe:
# 1821, Jalpa: 1824, Jerez: 1824, Loreto: 1931, Mazapil: 1824, Momax: 1857.
muni = {"Apozol": 1863, "Calera": 1868, "Fresnillo": 1554, "Guadalupe":
 1821, "Jalpa": 1824, "Jerez": 1824, "Loreto": 1931, "Mazapil": 1824, "Momax": 1857}
print("\033c", end="")
# Muestra el diccionario.
print(f"\nTodos el diccionario: {muni} - {len(muni)} elementos")
#Realiza las siguientes eliminaciones, mostrando el estado del diccionario después de cada operación:
# o Elimina Apozol (usando del).
del muni["Apozol"]
print(f"\nTodos el diccionario borrando Apozol: {muni} - {len(muni)} elementos")
# Elimina Fresnillo (usando pop()).
muni.pop("Fresnillo")
print(f"\nTodos el diccionario borrando Fresnillo: {muni} - {len(muni)} elementos")
# Elimina el último elemento insertado (Momax) (usando popitem()).
muni.popitem()
print(f"\nTodos el diccionario borrando el ultimo elemento: {muni} - {len(muni)} elementos")
# ● Vacía el diccionario (usando clear()).
# ● Muestra el diccionario final (vacío).
muni.clear()
print(f"\nBorrar todo el diccionario: {muni} - {len(muni)} elementos")