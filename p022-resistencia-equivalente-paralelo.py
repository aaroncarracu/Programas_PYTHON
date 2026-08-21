# p022-resistencia-equivalente-paralelo.py
# Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.
print("\033[2J\033[H", end="")
print("Calcular la resistencia equivalente de un circuito con cuatro resistencias en paralelo \n")
r1 = float(input("dame el valor de la 1 resistencia: \n"))
r2 = float(input("dame el valor de la 2 resistencia: \n"))
r3 = float(input("dame el valor de la 3 resistencia: \n"))
r4 = float(input("dame el valor de la 4 resistencia: \n"))
req = 1 / (1/r1 + 1/r2 + 1/r3 + 1/r4)
print("Las resistencias son:")
print(f"{r1} Ω , {r2} Ω , {r3} Ω y {r4} Ω")
print(f"La resistencia total es: {req:.3f} Ω")