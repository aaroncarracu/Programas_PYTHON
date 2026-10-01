# p097-producto-punto.py
# calcular el producto punto de dos vectores
# Se tienen dos vectores de la misma longitud, y se desea calcular su producto punto.
vector1 = [1, 3, -5]
vector2 = [4, -2, -1]

print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Validar que ambos vectores tengan la misma longitud antes de calcular el producto punto.
if len(vector1) != len(vector2):
    print("Error: los vectores deben tener la misma longitud.")
else:
    # Calcular el producto punto de los dos vectores y mostrar el resultado.
    producto_punto = 0

    for i in range(len(vector1)):
        producto_punto += vector1[i] * vector2[i]

    print("Producto punto:", producto_punto) 