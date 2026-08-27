# p035-tipo-triangulo.py
# Clasificar un triangulo segun la longitud de sus lados
print("\033[2J\033[H", end="")
print("Clasificar un triangulo segun la longitud de sus lados: \n")
ladoa = float(input("Dame la longuitud de lado a: "))
ladob = float(input("Dame la longuitud de lado b: "))
ladoc = float(input("Dame la longuitud de lado c: "))
if ladoa == ladob and ladob == ladoc:
    print('\n Es un triangulo EQUILATERO , todos sus lados son iguales')
elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print('\n Es un triangulo ISOCELES , al menos dos lados iguales')
else:
    print('\n Es un triangulo ESCALENO , todos sus lados son diferentes ')

print('\nProceso terminado')