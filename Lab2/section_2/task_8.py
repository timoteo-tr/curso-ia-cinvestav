"""  Función input()
    =======================
    
    La función input() lee una línea de texto desde la entrada estándar (teclado)
    y la retorna como un string.
    
    Características:
    - Siempre retorna un string
    - Puede recibir un argumento opcional (prompt) para mostrar un mensaje
    - El programa se pausa hasta que el usuario presiona Enter
    - Para otros tipos de datos, se necesita conversión explícita
"""
    
# Ejemplo 1: Input básico
print("\n1. INPUT BÁSICO:")
print("Ejemplo: nombre = input('¿Cuál es tu nombre? ')")
print("→ El programa espera entrada del usuario")
    
# Ejemplo 2: Conversión de tipos
print("\n2. CONVERSIÓN DE TIPOS:")
print("edad_str = input('¿Cuál es tu edad? ')  # Retorna string")
print("edad_int = int(edad_str)                # Conversión a entero")
print("→ Siempre se necesita conversión explícita")
    
# Ejemplo 3: Múltiples inputs
print("\n3. MÚLTIPLES INPUTS:")
print("nombre = input('Nombre: ')")
print("edad = input('Edad: ')")
print("ciudad = input('Ciudad: ')")
print("→ Se pueden capturar múltiples valores")
    
# Ejemplo 4: Input con validación
print("\n4. INPUT CON VALIDACIÓN:")
print("while True:")
print("    try:")
print("        numero = int(input('Ingresa un número: '))")
print("        break")
print("    except ValueError:")
print("        print('¡Error! Debes ingresar un número válido.')")
print("→ Manejo de errores para entradas inválidas")
    
# Demostración interactiva
print("\n" + "-"*40)
print("DEMOSTRACIÓN INTERACTIVA")
print("-"*40)
    
# Demo 1: Input simple
nombre = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola, {nombre}!")
    
# Demo 2: Input numérico con conversión
try:
    edad = input("Ingresa tu edad: ")
    edad_num = int(edad)
    print(f"En 10 años tendrás {edad_num + 10} años")
except ValueError:
        print("Edad no válida")
    
# Demo 3: Input múltiple en una línea
datos = input("Ingresa tu ciudad y país separados por coma: ")
ciudad, pais = datos.split(',') if ',' in datos else (datos, "desconocido")
print(f"Ubicación: {ciudad.strip()}, {pais.strip()}")