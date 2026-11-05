# p140-func-param-nombre.py
# Ejemplo de una funcion con parametros y nombre 
print("\033c", end="")
def saluda(paterno: str, materno: str, nombre: str) -> None:
    print(f"Hola, {paterno} {materno} {nombre} ")

saluda("Perez", "Gonzalez", "David")
saluda(nombre="Jose", paterno="Perez", materno="Gonzalez")