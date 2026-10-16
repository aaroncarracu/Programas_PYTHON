# p124-agregar-diccionario.py
# Crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
ventas ={"Juan": 1550,"Jose":2600,"Maria":2220}
print("\033c", end="")
# Muestra el diccionario.
print(f"\nTodos el diccionario: {ventas} - {len(ventas)} elementos")
# Agrega los siguientes vendedores y sus ventas al diccionario:
# o Rocio: 2500 (usando []).
# o Mateo: 1567 (usando []).
# o Andrea: 9567 (usando update()).
# o Miguel: 1234 (usando update()).
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567
ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})
# Muestra el diccionario actualizado
print(f"\nTodos el diccionario actualizado: {ventas} - {len(ventas)} elementos")
