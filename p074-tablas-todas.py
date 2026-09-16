# p074-tablas-todas.py
# Imprime las tablas de multiplicar de 1 al 10, del 1 al 10
print("\033[2J\033[H", end="")
print("Imprime las tablas de multiplicar de 1 al 10 \n ")
t= 10
n= 10
c=0
for i in range(1, t+1):
    print("="*30)
    print(f"Tabla del {i}")
    print("="*30) 
    for j in range(1,n+1):
        c=i*j
        print(f"{i} x {j} = {c}")
 
    print("="*30) 
print("\n Proceso terminado...") 