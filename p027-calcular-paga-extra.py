# p027-calcular-paga-extra.py
# Calculando la paga de un trabajador calculando la paga de horas extras
 
print("\033[2J\033[H", end="")
print("Calcular la paga de un trabajador considerando horas extras ")
print ("Dame los datos")
nombre = input ("Nombre: ")
horas = int(input("Horas: "))
paga_pxhora = float(input("Pago x hora: "))

horas_extra = paga_extra = 0
if horas > 40 :
    paga_normal = 40 * paga_pxhora
    horas_extra= horas - 40
    paga_extra = horas_extra * (paga_pxhora*2)
else :
    paga_normal = horas * paga_pxhora

total = paga_normal + paga_extra
print("Calculos de pagos")
print(f"El trabajador {nombre} trabajo {horas} horas a una paga de {paga_pxhora}")
print(f"Paga Normal: {paga_normal}")
print(f"Horas extra: {horas_extra}")
print(f"Paga Extra: {paga_extra}")
print(f"Total pagado: {total}")
print("\n Proceso terminado...")