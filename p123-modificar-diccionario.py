# p123-modificar-diccionario.py
# Crea un diccionario llamado paises con los siguientes pares (llave: valor): Argentina: 100, Brasil: 200,
# Colombia: 300, Chile: 400, Ecuador: 500, Bolivia: 600, Jamaica: 700.
paises = {'Argentina': 100, 'Brasil': 200, 'Colombia': 300, 'Chile': 400, 'Ecuador': 500, 'Bolivia':
600, 'Jamaica': 700}
print("\033c", end="")
# Muestra el diccionario inicial.
print(f"\nTodos el diccionario: {paises} - {len(paises)} elementos")
# Modifica los valores de las siguientes llaves:
#o Cambia el valor de Brasil a 250 (usando []).
# o Cambia el valor de Chile a 450 (usando []).
# o Cambia el valor de Bolivia a 650 (usando update()).
# o Cambia el valor de Jamaica a 750 (usando update()).
paises["Brasil"]= 250
paises["Chile"]= 450
paises["Bolivia"]= 650
paises["Jamaica"]= 750
# Muestra el diccionario modificado.
print(f"\nEl diccionario modificado es: {paises} - {len(paises)} elementos")