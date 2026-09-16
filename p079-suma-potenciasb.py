# p079-suma-potenciasb.py
# Suma las potencias de un numero x , desde x^1 hasta x^n
print("\033[2J\033[H", end="")
print("Calculando la serie de S = x^1 +...+x^n \n")

base_x = int(input("Numero base x : "))
n_terminos = int(input("Cuantos terminos n : "))

serie_texto = ""
suma = 0

for i in range(1, n_terminos + 1):
    suma += base_x ** i
    serie_texto += f"{base_x}^{i}" if i == 1 else f" + {base_x}^{i}"

print(f"S = {serie_texto} = {suma:,}")