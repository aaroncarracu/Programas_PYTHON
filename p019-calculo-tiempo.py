# p019-calculo-tiempo.py
# Diseña un programa que tome una cantidad de horas como un número entero
print("\033[2J\033[H", end="")
print("Calcular el tiempo en diferentes unidades \n")
horas = int(input("dame la cantidad de horas: "))
dias = horas / 24
minutos = horas * 60
segundos = minutos * 60
print(f"Las horas son     : {horas} h")
print(f"Los días son      : {dias:.2f} días")
print(f"Los minutos son   : {minutos} min")
print(f"Los segundos son  : {segundos} s")