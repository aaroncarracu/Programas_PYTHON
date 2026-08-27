# p032-aceptar-estudiante.py
# Aceptar estudiantes en base a edad y calificaciones (usando AND)
# Condiciones edad >= 18 y c1 y c2 >= 8
print("\033[2J\033[H", end="")
print("Aceptar estudiantes en base a edad y calificaciones (usando AND)\n")
nombre = input("dame tu nombre:  ")
edad = int(input("Dame tu edad:  "))
if edad >=18 :
    print ("\n Continuamos con el proceso:")
    c1= float(input("Dame tu primera calificacion:  "))
    c2= float(input("Dame tu segunda calificacion:  "))
    if c1 >= 8 and c2 >= 8 :
        print (f"{nombre}, Bienvenido a la universidad... ")
    else :
       print (f"\n {nombre} , No aceptamos calificaciones menores a 8... ") 

else :
    print (f"\n {nombre} , No aceptamos menores de edad... ")

print ("\nProceso terminado :")