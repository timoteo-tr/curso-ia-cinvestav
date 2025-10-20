"""
    El método .sort() se utiliza para ordenar los elementos de una lista IN-PLACE,
    es decir, modifica la lista original directamente.
    
    Características principales:
    - Ordena la lista en su lugar (no retorna una nueva lista)
    - Por defecto ordena en orden ascendente
    - Puede personalizarse con el parámetro 'key'
    - Puede invertirse con el parámetro 'reverse'
    - 

Este es un algoritmo híbrido llamado Timsort, diseñado por Tim Peters (uno de los desarrolladores más reconocidos de Python).
"""


# Ejemplo 1: Ordenamiento básico
print("\n1. Ordenamiento básico (con números):")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista original: {numeros}")
numeros.sort()
print(f"Después de .sort(): {numeros}")
    
# Ejemplo 2: Ordenamiento descendente
print("\n2. Ordenamiento descendente (con letras):")
letras = ['z', 'a', 'c', 'b', 'y']
print(f"Lista original: {letras}")
letras.sort(reverse=True)
print(f"Después de .sort(reverse=True): {letras}")
    
# Ejemplo 3: Ordenamiento con key personalizado
print("\n3. Ordenamiento con key personalizado (con palabras):")
palabras = ['manzana', 'pera', 'kiwi', 'banana']
print(f"Lista original: {palabras}")
palabras.sort(key=len)  # Ordenar por longitud
print(f"Después de .sort(key=len): {palabras}")
