# p081-plan-ahorro-depistos-mensuales.py
# Deberá solicitar al usuario un monto inicial, un depósito mensual fijo,
# una tasa de interés mensual (porcentaje), y el número total de meses del plan.
print("\033[2J\033[H", end="")
print("Imprimir onto inicial, un depósito mensual fijo, una tasa de interés mensual (porcentaje), y el número total de meses del plan \n")
mon=float(input("Monto inicial de ahorro: "))
d=float(input("Depósito mensual: "))
tim=float(input("Tasa de interés mensual (%): "))
meses=int(input("Número de meses a simular: "))
print("----Plan de Ahorro Detallado----")
for i in range(1,meses+1):
    ints= (mon*tim)/100
    n=mon
    mon+=ints+d
    print(f"Mes: {i} saldo incial: ${n:.2f} | interes: ${ints:.2f} | Saldo Final: ${mon:.2f}")
print(f"\nAl final de {i} meses, tendrás {mon:.2f}")
    