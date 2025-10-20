# Operaciones con enteros (int)
a = 3 # Si el número va sin punto, es de tipo entero
b = 5
print("Operaciones básicas con los números tipo int,",a,"y",b)
print(a,"+",b,"=",a+b,"Tipo:", type(a+b))
print(a,"-",b,"=",a-b,"Tipo:", type(a-b))
print(a,"*",b,"=",a*b,"Tipo:", type(a*b))
print(a,"/",b,"=",a/b,"Tipo:", type(a/b))

print()
print("-----------------------")
a = float(a) # Conversión a tipo float
b = float(b)
print("Operaciones básicas con los números tipo float,",a,"y",b)
print(a,"+",b,"=",a+b,"Tipo:", type(a+b))
print(a,"-",b,"=",a-b,"Tipo:", type(a-b))
print(a,"*",b,"=",a*b,"Tipo:", type(a*b))
print(a,"/",b,"=",a/b,"Tipo:", type(a/b))

print()
print("-----------------------")
a = int(a) # Conversión a tipo int
print("Operaciones básicas con los números",a,"de tipo int y",b, "de tipo float")
print(a,"+",b,"=",a+b,"Tipo:", type(a+b))
print(a,"-",b,"=",a-b,"Tipo:", type(a-b))
print(a,"*",b,"=",a*b,"Tipo:", type(a*b))
print(a,"/",b,"=",a/b,"Tipo:", type(a/b))