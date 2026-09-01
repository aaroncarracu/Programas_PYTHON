# p050-conteo-numeros.py
# Escribe un programa que le pida al usuario que introduzca números uno por uno y realice un conteo, parar con 999.
print("\033[2J\033[H", end="")
print("Usuario introduce n numeros conteo, paro con 999")
c = suma = cp = cn = cz = 0
while True:
    n = int(input("Numero: (999 para terminar) "))
    if n == 999: break
    c+= 1
    suma += n
    if n> 0: 
        cp += 1  # contador
    elif n < 0: 
        cn += 1 # contador
    else: 
        cz += 1 # contador
print("\n Los calculos son:")
print(f"\n cuantos?   {c}")
print(f"\n suma?      {suma}")
print(f"\n positivos? {cp}")
print(f"\n negativos? {cn}")
print(f"\n cero?      {cz}")
print ("\n Proceso terminado...")