def maximo(sucesion):
    """ Calcula el término máximo de una sucesión dada """
    max = sucesion[0]
    for term in sucesion:
        if term > max:
            max = term
    return max

def minimo(sucesion):
    """ Calcula el término máximo de una sucesión dada """
    min = sucesion[0] 
    for term in sucesion:
        if term < min:
            min = term
    return min

def long(sucesion):
    """ Calcula el número de términos de una sucesión dada """
    suma = 0
    for k in sucesion:
        suma += 1
    return suma

List = [-4,5,0,12,6,-9]
Tupla = (-5,5,0,1,36,-12,4)

print("Lista =", List)
print("El número máximo de la lista es:", maximo(List))
print("El número mínimo de la lista es:", minimo(List))
print("El número de elementos de la lista es:",long(List))
print()

print("--------------------------------------------")
print("Tupla =", Tupla)
print("El número máximo de la tupla es:", maximo(Tupla))
print("El número mínimo de la tupla es:", minimo(Tupla))
print("El número de elementos de la tupla es:",long(Tupla))

