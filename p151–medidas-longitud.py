# p151–medidas-longitud.py
# Un conversor de unidades de longitud. El programa debe mostrar un
# menú y utilizar dos funciones separadas:
def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54
def metros_a_pies(metros):
    return metros * 3.28084
while True:
    print("Conversor de unidades de longitud")
    print("1. Pulgadas a centímetros")
    print("2. Metros a pies")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        pulgadas = float(input("Ingrese la cantidad en pulgadas: "))
        centimetros = pulgadas_a_centimetros(pulgadas)
        print(f"\n {pulgadas} pulgadas son {centimetros:.2f} centímetros. \n")
    elif opcion == "2":
        metros = float(input("Ingrese la cantidad en metros: "))
        pies = metros_a_pies(metros)
        print(f"\n {metros} metros son {pies:.2f} pies. \n")
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

