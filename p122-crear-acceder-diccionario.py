# p122-crear-acceder-diccionario.py
# Crea un diccionario llamado dias usando llaves numéricas para los días de la semana
Diccionario_dias = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}
print("\033c", end="")

# Muestra el diccionario completo.
print(f"\nTodos el diccionario: {Diccionario_dias} - {len(Diccionario_dias)} elementos")
# Accede y muestra los siguientes valores específicos:
# o El valor de la llave 1 (usando []).
# o El valor de la llave 7 (usando []).
#o El valor de la llave 5 (usando get()).
#o El valor de la llave 7 (usando get()).
print(Diccionario_dias[1])
print(Diccionario_dias[7])
print(Diccionario_dias.get(5))
print(Diccionario_dias.get(7))
# Vuelve a mostrar el diccionario completo.
print(f"\nTodos el diccionario: {Diccionario_dias} - {len(Diccionario_dias)} elementos")