# p130-conjunto-personas.py
# las siguientes dos listas de nombres:
lista1 = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
lista2 = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}
print("\033[H\033[J")
# Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
# Crear los conjuntos A y B
A = set(lista1)
B = set(lista2)

# Mostrar los conjuntos
print("Conjunto A:", A)
print("Conjunto B:", B)
# Unión (A | B)
print("\nUnion de conjuntos")
print(f"A U B: {A.union(B)}")
# Intersección (A & B)
print("\nInterseccion de conjuntos")
print(f"A ∩ B: {A.intersection(B)}")
# Diferencia (A - B)
print("\nDiferencia de conjuntos")
print(f"A - B: {A.difference(B)}")
# Diferencia Simétrica (A ^ B)
print("\nDiferencia simétrica de conjuntos")
print(f"A Δ B: {A.symmetric_difference(B)}")
# Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes afirmaciones:
# ¿Es {Pablo, Mateo} un subconjunto de B?
C = {"Pablo", "Mateo"}
print("\nSubconjuntos y superconjuntos")
print(f"Es PABLO, MATEO  es subconjunto de B? {C.issubset(B)}")
# ¿Es A un superconjunto de {Reynaldo, Angelica}?
D = {"Reynaldo", "Angelica"}
print("\nSuperconjuntos")
print(f"A es superconjunto de D? {A.issuperset(D)}")
# ¿Está "Pedro" en el conjunto A?
print("\nPertenencia y no pertenencia")
print(f"Pedro pertenece a A? {"Pedro" in A}")
# ¿No está "Lilia" en el conjunto B?
print(f"Lilia pertenece a B? {"Lilia" in B}")