# p048-multiplos-continue.py
# Escribe un programa que escriba los múltiplos de 10.
print("\033[2J\033[H", end="")
print("Imprimir múltiplos de 10. del 1 al 100")
i = 1
while i <= 100:
    i += 1
    if i % 10 != 0: continue 
    print(i, end=" ")
print ("\n Proceso terminado...") 