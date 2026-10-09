# p110-comprension-filtra-palabras.py
# Dada una lista de palabras introducidas por el usuario separadas por espacios, utilizar comprensión de listas
# para crear una nueva lista que contenga solo aquellas palabras que tengan más de 4 caracteres y convertirlas a
# mayúsculas. Imprimir la lista original y la lista filtrada.
print("\033[2J\033[H", end="")
texto = input("Introduce palabras separadas por espacios: ")

# Crear la lista original
lista_original = texto.split()

# Filtrar palabras con más de 4 caracteres y convertirlas a mayúsculas
lista_filtrada = [palabra.upper() for palabra in lista_original if len(palabra) > 4]

# Imprimir ambas listas
print("Lista original:", lista_original)
print("Lista filtrada:", lista_filtrada)