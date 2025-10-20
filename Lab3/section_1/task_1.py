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

# Leer matriz A
for i in range(4):
    for j in range(4):
        A[i][j] = int(input(f"a[{i+1}][{j+1}]: "))


# Leer matriz B
for i in range(4):
    for j in range(4):
        B[i][j] = int(input(f"b[{i+1}][{j+1}]: "))

# Multiplicación de Matrices
for i in range(4):
    for j in range(4):
        suma = 0
        for k in range(4):
            suma += A[i][k] * B[k][j]
        C[i][j] = suma


print("C = A * B")
print(C)
