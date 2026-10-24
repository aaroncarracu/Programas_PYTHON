# p131-conjunt-numeros.py
# Dadas las siguientes tres listas de números:
Lista1 = {50, 60, 70, 80, 90, 100, 200}
Lista2 = {60, 90, 100, 300, 400, 500}
Lista3 = {10, 20, 60, 90, 70, 100, 600, 700}
# Crear y mostrar los conjuntos A, B y C a partir de las listas.
A = set(Lista1)
B = set(Lista2)
C = set(Lista3)
# Mostrar los conjuntos
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)
#o Unión (A | B)
#o Unión (B | C)


print("\nUnion de conjuntos")
print(f"A | B: {A.union(B)}")
print(f"B | C: {B.union(C)}")
# Diferencia (A - C)
print("\nDiferencia de conjuntos")
print(f"A - C: {A.difference(C)}")
# Diferencia Simétrica (B ^ C)
print("\nDiferencia simétrica de conjuntos")
print(f"B Δ C: {B.symmetric_difference(C)}")
# Intersección (B & C)
print("\nInterseccion de conjuntos")
print(f"B ∩ C: {B.intersection(C)}")
# Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes preguntas:
# o ¿Es A subconjunto de B?
print("\nSubconjuntos y superconjuntos")
print(f"Es A, MATEO  es subconjunto de B? {A.issubset(B)}")
# o ¿Es C subconjunto de A?
print(f"Es C, MATEO  es subconjunto de A? {C.issubset(A)}")
# o ¿Está el número 100 en A?
print("\nPertenencia y no pertenencia")
print(f"Esta el num 100 en A? {100 in A}")
# o ¿Está el número 60 en A, B y C?
print(f"Esta el num 60 en A? {60 in A}")
print(f"Esta el num 60 en B? {60 in B}")
print(f"Esta el num 60 en C? {60 in C}")
# o ¿No está el número 900 en C?
print(f"Esta el num 900 en C? {900 in C}")