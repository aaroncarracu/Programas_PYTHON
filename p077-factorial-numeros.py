# p077-factorial-numeros.py
# Calcular el factorial de n numeros 
print("\033[2J\033[H", end="")
print("Calcular el factorial de n numeros\n ")
try:
    n= int(input("Hasta que numero ? "))
    f=1
    c= "x"
    print(f"{n}! =", end="")
    for i in range(1,n+1):
        f=f*i
        if i == n:
         print(f" {i} ", end="")
        else:
         print(f" {i} {c}", end="")
    print(f"= {f:,}")
except ValueError:
    print("Solo se aceptan numeros enteros")