# p147-estacion-año.py
# Funcion que regresas la estacion del año segun el mes
print("\033c", end="")

def estacion_año(mes: int) -> str:
    meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
    if mes in [12, 1, 2]:
        return "Invierno"
    elif mes in [3, 4, 5]:
        return meses[mes] + " - y es Primavera"
    elif mes in [6, 7, 8]:
        return meses[mes] + " - y es Verano"
    else:
        return meses[mes] + " - y es Otoño"

# Ejemplo de uso
mes = int(input('Dame el numero del mes del 1 al 12: '))
print(f'Corresponde a: {estacion_año(mes)}')