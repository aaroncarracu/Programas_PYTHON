# p139-funcion-parametros.py
# Ejemplo de una funcion con varios parametros
print("\033c", end="")

def saluda(paterno: str, nombre: str) -> None:
    print(f"Hola, {paterno} {nombre}")

saluda("Perez", "David")
saluda("Perez", "Jose")