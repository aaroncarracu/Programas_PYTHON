# p142-func-mas-param.py
# funcion que resive n parametros
print("\033c", end="")

def saluda(*nombres: str) -> None:
    print(nombres)

    for nombre in nombres:
        print(f'Hola {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres')


def edades(*edades: int) -> None:
    print(edades)

    for edad in edades:
        print(f'Tu edad es: {edad} años')


saluda('Carlos Castaneda', 'Juan', 'Pedro')
edades(25, 30, 35)