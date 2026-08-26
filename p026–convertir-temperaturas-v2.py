# p026–convertir-temperaturas-v2.py
# Convierte temperaturas de grados celsuis a grados fahrenheit y viceversa.
print("\033[2J\033[H", end="")
print("Convertir temperaturas grados celsuis a grados fahrenheit y viceversa \n")
print("[1] Convertir de Celsius a Fahrenheit")
print("[2] Convertir de Fahrenheit a Celsius")
op = int(input("elije una opcion: "))
if op == 1:
    print("Convirtiendo de Fahrenheit a Celsius")
    f = float(input("Dame la temperatura en grados Fahrenheit "))
    c = (f-32)*5/9
    print(f"✅ {f} grados Fahrenheit, equivalen a {c} grados centigrados ")
else :
    if op == 2:
        print("Convirtiendo de Celsius a Fahrenheit")
        c = float(input("Dame la temperatura en grados Celsius "))
        f = (c* 9/5)+ 32
        print(f"✅ {f} grados Celsius, equivalen a {c} grados Fahrenheit ")
    else :
        print("\n Opcion invalida ")

print("\n Programa Finalizada... ")