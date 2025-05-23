import sys
from string import ascii_lowercase

def fuerza_bruta(password):
    password = password.lower()  
    intentos = 0
    
    for i, char_password in enumerate(password):
        for char_alphabet in ascii_lowercase:
            intentos += 1  
            if char_alphabet == char_password:
                break 
    return intentos

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python fuerza_bruta.py <contraseña>")
        sys.exit(1)
    
    contrasena_oculta = sys.argv[1]
    
    # Validar que la contraseña solo contenga letras (sin la ñ)
    for char in contrasena_oculta.lower():
        if char not in ascii_lowercase:
            print("La contraseña solo debe contener letras del abecedario en minúsculas (sin la ñ).")
            sys.exit(1)

    num_intentos = fuerza_bruta(contrasena_oculta)
    print(f"La contraseña fue forzada en {num_intentos} intentos")