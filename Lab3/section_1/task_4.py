def crear_contraseña():
    print("=== CREADOR DE CONTRASEÑAS ===")
    print("Requisitos:")
    print("- Mínimo 8 caracteres")
    print("- No puede contener espacios")
    print("- No puede contener los caracteres: &, #, %, @")
    print()
    
    while True:
        contraseña = input("Ingresa tu nueva contraseña: ")
        
        # Verificar longitud mínima
        if len(contraseña) < 8:
            print("Error: La contraseña debe tener al menos 8 caracteres")
            continue
        
        # Verificar espacios
        if ' ' in contraseña:
            print("Error: La contraseña no puede contener espacios")
            continue
        
        # Verificar caracteres prohibidos
        caracteres_prohibidos = ['&', '#', '%', '@']
        for caracter in caracteres_prohibidos:
            if caracter in contraseña:
                print(f"Error: La contraseña no puede contener el carácter '{caracter}'")
                break
        else:
            # Si no se rompió el ciclo, la contraseña es válida
            print("¡Contraseña creada exitosamente!")
            print(f"Tu contraseña es: {contraseña}")
            break

# Ejecutar el programa
crear_contraseña()