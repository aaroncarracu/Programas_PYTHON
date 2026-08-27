# p036-numeros-consecutivos.py
# Escribe un programa que reciba tres números enteros y determine si son consecutivos.
print("\033[2J\033[H", end="")
print("Escribe un programa que reciba tres números enteros y determine si son consecutivos \n")
n1 = int(input("Dame el primer numero : "))
n2 = int(input("Dame el segundo numero: "))
n3 = int(input("Dame el tercer numero : "))
if (n2-n1 == 1) and (n3-n2 == 1) :
    print(f"Los numeros {n1},{n2},{n3} son consecutivos")
else :
    print(f"Los numeros {n1},{n2},{n3},  NO son consecutivos")
print("\n Proceso terminado.....")
