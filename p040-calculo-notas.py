# p040-calculo-notas.py
# Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en
# el promedio, el programa deberá mostrar uno de los siguientes mensajes:
print("\033[2J\033[H", end="")
print("Escribe un programa que realice el promedio de 5 calificaciones")
c1 = float (input("Dame la primera calificacion : "))
c2 = float (input("Dame la segunda calificacion : "))
c3 = float (input("Dame la tercer calificacion  : "))
c4 = float (input("Dame la cuarta calificacion  : "))
c5 = float (input("Dame la quinta calificacion  : "))
prom = (c1+c2+c3+c4+c5)/5
print(f"\nTu promedio de calificacion es: {prom}")
if prom < 6 :
    print("Quedas reprobado")
elif prom >= 6 and prom < 7 :
    print("Pasas de panzazo")
elif prom >= 7 and prom < 8 :
    print("Muy bien, puedes mejorar")
elif prom >= 8 and prom < 9 :
    print("Excelente, sigue así")
elif prom >= 9 and prom <= 10 :
    print("Perfecto, tu esfuerzo valió la pena")

print("Proceso terminado.... ")