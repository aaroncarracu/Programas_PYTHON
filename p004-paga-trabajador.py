# p004-paga-trabajador.py
# calcular el pago de un trabajador
print("\033[2J\033[H", end="")
print ("calculando el pago de un trabajador \n")

# Entrada
nombre = input("ingresa el nombre del trabajador ")
horas = int(input("las horas trabajadas "))
paga = float(input("la paga por hora "))
# proceso
tasa =0.03
pagabruta = horas * paga 
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
# Salida
print ("Resumen de pagos \n")
print (f"El trabajador: {nombre}, trabajo {horas} horas, a una paga de {paga} pesos")
print (f"Paga bruta: {pagabruta:>10,.2f} pesos")
print (f"impuesto: {impuesto:>10.2f} pesos")
print (f"Paga neta: {paganeta:>10,.2f} pesos")


