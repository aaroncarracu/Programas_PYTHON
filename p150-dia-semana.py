# p150-dia-semana.py
# Escribe un programa con una función que reciba un número entero entre 1 y 7. La función debe devolver el día
# de la semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo"). El programa principal debe pedir el
# número al usuario, llamar a la función y mostrar el nombre del día.
def dia_semana(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(numero, "Número inválido. Debe ser entre 1 y 7.")

numero = int(input("Ingrese un número entre 1 y 7: "))
print("El día de la semana es:", dia_semana(numero))