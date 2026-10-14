# p121-area-figuras.py
# Calculadora dinámica de áreas usando un diccionario de diccionarios

import math

figuras = {
    "1": {
        "nombre": "Círculo",
        "parametros": ["radio"],
        "formula": "pi * radio ** 2"
    },
    "2": {
        "nombre": "Triángulo",
        "parametros": ["base", "altura"],
        "formula": "base * altura / 2"
    },
    "3": {
        "nombre": "Rectángulo",
        "parametros": ["base", "altura"],
        "formula": "base * altura"
    }
}
while True:
    print("\nCalculadora de áreas")
    for opcion, figura in figuras.items():
        print(f"{opcion}. {figura['nombre']}")
    print("0. Salir")

    opcion = input("Elija una figura: ")

    if opcion == "0":
        print("Hasta luego.")
        break
    if opcion not in figuras:
       print("Opción no válida. Intente de nuevo.")
       continue

    figura = figuras[opcion]
    valores = {}
    for parametro in figura["parametros"]:
        while True:
                try:
                    valor = float(input(f"Ingrese {parametro}: "))
                    if not math.isfinite(valor) or valor <= 0:
                        print("El valor debe ser un número mayor que cero.")
                        continue
                    valores[parametro] = valor
                    break
                except ValueError:
                    print("Ingrese un número válido.")
       


contexto = {"pi": math.pi, **valores}
area = eval(figura["formula"], {"__builtins__": {}}, contexto)
print(f"Fórmula: {figura['formula']}")
print(f"Área del {figura['nombre'].lower()}: {area:.2f}")