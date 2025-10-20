"""
Se crea un diccionario anidado donde, para cada estudiante, se le asigna
una calificación por cada materia que lleva y con base a los datos de la lista
generada, generar otro diccionario, simple, donde se considere el nombre y 
el promedio
"""

List1 = {  # Diccionario anidado
    "Ana": {"Matemáticas": 90, "Física": 85, "Química": 88},
    "Luis": {"Matemáticas": 75, "Física": 80, "Química": 70},
    "María": {"Matemáticas": 95, "Física": 100, "Química": 98},
    "Francisco": {"Matemáticas": 73, "Física": 82, "Química": 100}
}

List2 = {} # Diccionario simple, vacío

for nombre in List1.keys():    
    contador = 0 
    suma = 0
    for materia, calif in List1[nombre].items():
        suma += calif
        contador += 1
    promedio = suma/contador    
    List2[nombre]=(round(promedio,2))

print(List1)
print()
print(List2)

print()
print("Nombre      Promedio")
print("----------------------")
for nombre, promedio in sorted(List2.items()):
    print(f"{nombre:<10}  {promedio:>6.2f}")
    


