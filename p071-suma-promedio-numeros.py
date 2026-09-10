# p071-suma-promedio-numeros.py
# Calcula la suma y el promedio de las calificaciones 
while True:
    print("\033[2J\033[H", end="")
    print("Calcula la suma y el promedio de las calificaciones ")
    n = int (input("cuantas calificaciones: "))
    prom=0
    sum=0
    strcals = ""
    for i in range(0,n,1):
        print("calificacion" +str(i))
        cal = int(input())
        sum=sum+cal
        prom= sum/n 
        strcals=strcals + str(cal) + " "
    print(f"\n Los numeros fueron : {strcals}")
    print(f"\n La suma es igual a: {sum}")
    print(f"\n El promedio de las calificaciones es igual a: {prom}")
    if input("\n s para Continuar (S/N) ").upper() == "N" : break


