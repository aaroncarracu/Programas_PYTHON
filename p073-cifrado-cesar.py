# p073-cifrado-cesar.py
# Cifra un mensaje con desplazamiento (Cifrado de Cesar)
print("\033[2J\033[H", end="")
print("Cifrado Cesar ")
mo = input("Mensaje ? ")
d = int(input("Desplazamiento ? "))
ms = cn =""
for c in mo:
    if c.isalpha(): # solo letras
        ca =ord(c)
        if c.islower() :
            bd= ord("a")
        else:
            bd= ord("A")
        cn = bd +(ca - bd + d) % 26
        ms = ms + chr(cn)
    else:
        ms = ms + c

print("Mensaje cifrado: " +ms)

