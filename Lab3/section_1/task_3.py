import random

numero =random.randint(1,100)

intento = 1

print("Adivina el número secreto que tengo, es un número entero entre 1 y 100")
adiv = int(input("Ingresa un número: "))
while adiv != numero: 
    intento += 1        
    if adiv > numero:
        adiv = int(input("Intenta de nuevo, el número debe ser menor: "))
    elif adiv < numero:
        adiv = int(input("Intenta de nuevo, el número debe ser mayor: ")) 
       
print("\nAcertaste, con ",intento, " intentos.")
