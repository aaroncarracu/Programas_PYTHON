# p031-2da-ley-de-newton.py
# Realizar un programa que resualva la segunda ley de newton
print("\033[2J\033[H", end="")
print("Calcular los valores de la segunda ley de newton\n")
print("[F] fuerza        (f=m*a)")
print("[M] masa          (m=f/a)")
print("[A] aceleracion   (a=f/m)")
print("Elige ?")
op = input().upper()
f=a=m=0
if op == "F" :
    print("\n Estamos calculando la fuerza: ")
    m = float(input("Dame la masa :"))
    a = float(input("Dame la aceleracion : "))
    f= m*a
    print("\nla fuerza es : " +str(f))
elif op == "M" :
    print("\n Estamos calculando la masa: ")
    f = float(input("Dame la fuerza : "))
    a = float(input("Dame la aceleracion : "))
    m= f/a
    print("\nla masa es :" +str(m))
elif op == "A" :
    print("\n Estamos calculando la aceleracion: ")
    f = float(input("Dame la fuerza : "))
    m = float(input("Dame la masa : "))
    a= f/m
    print("\nla aceleracion es : " +str(a))
else :
    print ("\nOpcion incorrecta")

print ("\nProceso terminado")