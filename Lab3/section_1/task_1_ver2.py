A = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(0)
    A.append(fila)

B = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(0)
    B.append(fila)

C = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(0)
    C.append(fila)

print("Multiplicación de matrices de tamaño 4 × 4, con elementos enteros\n")

# Leer matriz A
for i in range(4):
    fila = input(f"Introduce fila {i+1} de A (4 números separados por espacio): ").split()
    for j in range(4):
        A[i][j] = int(fila[j])

print()

# Leer matriz B
for i in range(4):
    fila = input(f"Introduce fila {i+1} de B (4 números separados por espacio): ").split()
    for j in range(4):
        B[i][j] = int(fila[j])


# Multiplicación de Matrices
for i in range(4):
    for j in range(4):
        suma = 0
        for k in range(4):
            suma += A[i][k] * B[k][j]
        C[i][j] = suma


print("\nResultado: C = A × B\n")
for fila in C:
    for elemento in fila:
        print(f"{elemento:6}", end="")  # ancho fijo para alineación
    print()  # salto de línea al terminar la fila
