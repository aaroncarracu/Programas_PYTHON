# p091-lista-de-gastos.py
# Desarrolla una aplicación que almacene gastos en una lista y permita al usuario
# manipularla a través de un menú que se mostrará continuamente hasta que decida salir.

def mostrar_menu():
	print('\nAplicación de gastos')
	print('1. Agregar gasto')
	print('2. Mostrar gastos')
	print('3. Eliminar gasto')
	print('4. Modificar gasto')
	print('5. Ver total')
	print('6. Salir')
	opcion = input('Elige una opción: ').strip()
	return opcion

def main():
	gastos = []

	while True:
		opcion = mostrar_menu()

		if opcion == '1':
			try:
				gasto = float(input('Ingresa el monto del gasto: '))
				if gasto < 0:
					print('El monto no puede ser negativo.')
				else:
					gastos.append(gasto)
					print('Gasto agregado.')
			except ValueError:
				print('Ingresa un monto numérico válido.')
		elif opcion == '2':
			if not gastos:
				print('No hay gastos registrados.')
			else:
				print('\nGastos actuales:')
				for indice, gasto in enumerate(gastos, start=1):
					print(f'{indice}. ${gasto:.2f}')
		elif opcion == '3':
			if not gastos:
				print('No hay gastos para eliminar.')
			else:
				try:
					indice = int(input('Número del gasto que deseas eliminar: ')) - 1
					if indice < 0 or indice >= len(gastos):
						print('El número de gasto no existe.')
					else:
						gasto_eliminado = gastos.pop(indice)
						print(f'Gasto de ${gasto_eliminado:.2f} eliminado.')
				except ValueError:
					print('Ingresa un índice numérico válido.')
		elif opcion == '4':
			if not gastos:
				print('No hay gastos para modificar.')
			else:
				try:
					indice = int(input('Número del gasto que deseas modificar: ')) - 1
					if indice < 0 or indice >= len(gastos):
						print('El número de gasto no existe.')
					else:
						nuevo_gasto = float(input('Ingresa el nuevo monto: '))
						if nuevo_gasto < 0:
							print('El monto no puede ser negativo.')
						else:
							gastos[indice] = nuevo_gasto
							print('Gasto actualizado.')
				except ValueError:
					print('Ingresa un índice y un monto numéricos válidos.')
		elif opcion == '5':
			print(f'Total de gastos: ${sum(gastos):.2f}')
		elif opcion == '6':
			print('Hasta luego.')
			break
		else:
			print('Opción no válida. Elige un número del 1 al 6.')

if __name__ == '__main__':
	main()
