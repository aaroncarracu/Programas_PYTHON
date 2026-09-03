# p056-contador-vocales.py
# Dada una frase, cuenta cuantas vocanes , cuantas consonantes 
print("\033[2J\033[H", end="")
print("Dada una frase, cuenta cuantas vocanes , cuantas consonantes \n")
frase = input("ingresa una frase: ").lower()
print(f"\n La frase a nalizar es : {frase} y tiene {len(frase)} caracteres")

i=v=con=otro=0
while i < len(frase):
    c = frase[i]
    print (c, end= " ")
    if "a" <= c <= "z":
        print("si")
        if c in "aeiou" :
            v+= 1
        else:
            con += 1
    else:
        print("no")
        otro += 1

    i += 1
print(f"\n Vocales : {v} \n consonantes : {con} \n otros : {otro} ")