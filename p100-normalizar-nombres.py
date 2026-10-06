# p100-normalizar-nombres.py
# De una lista de nombres con espacios y mayusculas, se normalizan los nombres a minusculas y sin espacios al fin o inicio
print("\033[2J\033[H", end="")
print("\033[1;34m"+"Normalizar nombres" + "\033[0m")
nombres = ["  Juan  ", "  MARIA  ", "  Pedro  ", "  Ana  "]

# Normalizar los nombres a minusculas y sin espacios al inicio o fin
nombres_normalizados = [nombre.strip().lower() for nombre in nombres]
print("Nombres originales:", nombres)
print("Nombres normalizados:", nombres_normalizados)
