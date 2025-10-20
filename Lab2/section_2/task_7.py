"""
    Expresión s *= n para secuencias mutables
    =================================================
    
    La expresión s *= n (donde s es una secuencia mutable y n es un número entre 0 y 255)
    repite la secuencia 's' 'n' veces y asigna el resultado de nuevo a 's'.
    
    Características:
    - s debe ser una secuencia MUTABLE (lista, bytearray)
    - n debe ser un entero entre 0 y 255 (para operaciones in-place eficientes)
    - Modifica la secuencia original IN-PLACE
    - No aplica para secuencias INMUTABLES (tuplas, strings)
"""

# Ejemplo 1: Con listas (mutable)
print("\n1. CON LISTAS (MUTABLE):")
lista = [1, 2, 3]
print(f"Lista original: {lista} (id: {id(lista)})")
lista *= 3
print(f"Después de lista *= 3: {lista} (id: {id(lista)})")
print("→ Mismo objeto, contenido modificado")
    
# Ejemplo 2: Con bytearray (mutable)
print("\n2. CON BYTEARRAY (MUTABLE):")
bytes_mutables = bytearray(b'abc')
print(f"Bytearray original: {bytes_mutables}")
bytes_mutables *= 2
print(f"Después de bytearray *= 2: {bytes_mutables}")
    
# Ejemplo 3: Comparación con strings (inmutable)
print("\n3. COMPARACIÓN CON STRINGS (INMUTABLE):")
cadena = "abc"
print(f"String original: {cadena} (id: {id(cadena)})")
cadena *= 3
print(f"Después de string *= 3: {cadena} (id: {id(cadena)})")
print("→ Nuevo objeto creado (inmutable)")
    
# Ejemplo 4: Límites de n (0-255)
print("\n4. LÍMITES DE n (0-255):")
lista = ['x']
print(f"n = 0: {lista * 0}")  # Lista vacía
lista = ['x']
print(f"n = 1: {lista * 1}")  # Lista sin cambios
lista = ['x']
print(f"n = 255: longitud = {len(lista * 255)}")  # Máximo para operación in-place
