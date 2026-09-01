# p049-sumar-consecutivos.py
# Crea un programa que sume números consecutivos
print("\033[2J\033[H", end="")
print("Sumar números consecutivos del 1 al 100")
c=0
s=0
while c <= 200 :
    c += 1
    s += c
    print(f"{c}")
    if s >= 100: break

print(f"\ la suma de los numeros consecutivos es: {s}")