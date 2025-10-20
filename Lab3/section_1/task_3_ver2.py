import random

# Generar número secreto
numero = random.randint(1, 100)
intentos = 0

print("Adivina el número secreto que tengo (entre 1 y 100)\n")

while True:
    try:
        adiv = int(input("Ingresa un número: "))
        intentos += 1

        if adiv > numero:
            print("Demasiado alto, intenta con un número menor.\n")
        elif adiv < numero:
            print("Demasiado bajo, intenta con un número mayor.\n")
        else:
            print(f"\n¡Acertaste! Lo lograste en {intentos} intentos.")
            break

    except ValueError:
        print("Por favor, ingresa solo números enteros.\n")
