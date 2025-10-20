'''
Este programa transforma una variable de tipo str a int, float, bool,
list y tupla.
'''


var1 = "123"
print("Variable original:",var1, "Tipo:",type(var1))
print()

#Conversión a int
var2 = int(var1)
print("Convertido a int:",var2, "Tipo:",type(var2), "\n")

#Conversión a float      
var3=float(var1)
print("Convertido a float:",var3, "Tipo:",type(var3))
print()

#Conversión a bool
var4 = bool(var1)
print("Convertido a bool:",var4, "Tipo:",type(var4))
print()

# Conversión a lista
var5 = list(var1)
print("Convertido a lista:", var5, "Tipo:", type(var5))
print()

# Conversión a tupla
var6 = tuple(var1)
print("Convertido a tupla:", var6, "Tipo:", type(var6))
print()

# SEGUNDA PARTE: Cambiar valor a "hello"
print("=== CON 'hello' ===")
var1 = "hello"
print("Nueva variable:", var1)

# Intentar las mismas conversiones
# int
try:
    var2 = int(var1)
    print("Convertido a int:", var2, "Tipo:", type(var2))    
except ValueError as e:
    print("Error al convertir a int:", e)
print()

# float
try:
    var3 = float(var1)
    print("Convertido a float:", var3, "Tipo:", type(var3))    
except ValueError as e:
    print("Error al convertir a float:", e)
print()

# bool
try:
    var4 = bool(var1)
    print("Convertido a bool:", var4, "Tipo:", type(var4))    
except ValueError as e:
    print("Error al convertir a bool:", e)
print()

# lista
var5 = list(var1)
print("Convertido a lista:", var5, "Tipo:", type(var5))
print()

# tupla
var6 = tuple(var1)
print("Convertido a tupla:", var6, "Tipo:", type(var6))
print()
