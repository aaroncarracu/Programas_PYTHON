# p091-lista-de-gastos_b.py
# esarrolla una aplicación que almacene gastos en una lista y permita al usuario
# manipularla a través de un menú que se mostrará continuamente hasta que decida salir.

gastos = []
salir = False

while not salir:
	print('\n--- Aplicación de gastos ---')
	print('1. Ver gastos')
	print('2. Agregar gasto')
	print('3. Modificar gasto')
	print('4. Eliminar gasto')
	print('5. Ver total')
	print('6. Salir')

	opcion = input('Elige una opción: ').strip()

	if opcion == '1':
		if len(gastos) == 0:
			print('No hay gastos registrados.')
		else:
			print('\nGastos actuales:')
			for indice in range(len(gastos)):
				print(f'{indice + 1}. ${gastos[indice]:.2f}')
	elif opcion == '2':
		try:
			monto = float(input('Ingresa el monto del gasto: '))
			if monto < 0:
				print('Error: el monto no puede ser negativo.')
			else:
				gastos.append(monto)
				print('Gasto agregado correctamente.')
		except ValueError:
			print('Error: debes ingresar un monto numérico.')
	elif opcion == '3':
		if len(gastos) == 0:
			print('No hay gastos para modificar.')
		else:
			try:
				indice = int(input('Número del gasto que deseas modificar: ')) - 1
				if indice < 0 or indice >= len(gastos):
					print('Error: gasto no encontrado.')
				else:
					nuevo_monto = float(input('Ingresa el nuevo monto: '))
					if nuevo_monto < 0:
						print('Error: el monto no puede ser negativo.')
					else:
						gastos[indice] = nuevo_monto
						print('Gasto modificado correctamente.')
			except ValueError:
				print('Error: ingresa un índice y un monto numéricos.')
	elif opcion == '4':
		if len(gastos) == 0:
			print('No hay gastos para eliminar.')
		else:
			try:
				indice = int(input('Número del gasto que deseas eliminar: ')) - 1
				if indice < 0 or indice >= len(gastos):
					print('Error: gasto no encontrado.')
				else:
					gasto_eliminado = gastos.pop(indice)
					print(f'Gasto de ${gasto_eliminado:.2f} eliminado correctamente.')
			except ValueError:
				print('Error: ingresa un índice numérico.')
	elif opcion == '5':
		total = 0
		for gasto in gastos:
			total = total + gasto
		print(f'Total de gastos: ${total:.2f}')
	elif opcion == '6':
		print('Programa terminado.')
		salir = True
	else:
		print('Opción no válida. Elige un número del 1 al 6.')
