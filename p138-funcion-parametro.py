# p138-funcion-parametro.py
# Ejemplo de una funcion con parametros
print("\033c", end="")
def saluda(nombre: str) -> None:
    print(f"Hola, {nombre} bienvenido a python, tu nombre tiene {len(nombre)} letras")

saluda("Aaron ca")
saluda("david perez")
saluda("jose jose")