"""
    El método .replace() aplicado a strings
    ===============================================
    
    El método .replace() crea una nueva cadena reemplazando todas las ocurrencias
    de una subcadena por otra.
    
    Sintaxis: str.replace(viejo, nuevo[, count])
    - viejo: subcadena a reemplazar
    - nuevo: subcadena de reemplazo
    - count (opcional): número máximo de reemplazos a realizar
"""

 # Ejemplo 1: Reemplazo básico
print("\n1. REEMPLAZO BÁSICO:")
texto = "Hola mundo, hola Python, hola programación"
print(f"Texto original: {texto}")
nuevo_texto = texto.replace("hola", "adiós")
print(f"Después de .replace('hola', 'adiós'): {nuevo_texto}")
    
# Ejemplo 2: Reemplazo con count limitado
print("\n2. REEMPLAZO CON COUNT LIMITADO:")
texto = "uno dos tres uno dos tres uno dos tres"
print(f"Texto original: {texto}")
nuevo_texto = texto.replace("uno", "UNO", 2)  # Solo 2 reemplazos
print(f"Después de .replace('uno', 'UNO', 2): {nuevo_texto}")
    
# Ejemplo 3: Reemplazo case-sensitive
print("\n3. REEMPLAZO CASE-SENSITIVE:")
texto = "Python es genial, python es poderoso, PYTHON es divertido"
print(f"Texto original: {texto}")
nuevo_texto = texto.replace("Python", "Java")
print(f"Después de .replace('Python', 'Java'): {nuevo_texto}")
    
# Ejemplo 4: Reemplazo múltiple (encadenado)
print("\n4. REEMPLAZOS MÚLTIPLES ENCADENADOS:")
texto = "El gato negro saltó"
print(f"Texto original: {texto}")
nuevo_texto = texto.replace("gato", "perro").replace("negro", "blanco")
print(f"Después de reemplazos encadenados: {nuevo_texto}")