# p028-retira-cuenta.py
# Simula el retiro de dinero de una cuenta con validacion 
saldo_cuenta= 1500
print("\033[2J\033[H", end="")
print("Simula el retiro de dinero de una cuenta con validacion \n")

cantidad_retiro = float(input(f"cantidad a retirar de la cuenta saldo : {saldo_cuenta}?"))
if cantidad_retiro > 0:
     print ("\n Procedemos al retiro")
     if cantidad_retiro <= saldo_cuenta :
        nuevo_saldo= saldo_cuenta - cantidad_retiro
        print (f"\n Retiro exitoso, Tu nuevo saldo es {nuevo_saldo} ")
     else : 
       print (f" \n Quieres retirar {cantidad_retiro} Pero tienes {saldo_cuenta} No te alcanza")
else :
 print ("\n La cantidad a retirar debe ser un numero positivo")



 print ("\n Gracias por utilizar el servicio ")

