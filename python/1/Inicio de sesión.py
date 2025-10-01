# 1. Credenciales válidas
usuario_correcto = "admin"
clave_correcta = "1234"

intentos = 3
acceso_concedido = False

print("\n--- Sistema de Inicio de Sesión ---")

# Bucle para controlar los intentos
while intentos > 0:
    print(f"\nIntentos restantes: {intentos}")
    
    # Solicitar credenciales
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    # Validar si los campos están vacíos
    if not usuario or not clave:
        print("\nError de autentificación: Ambos campos son obligatorios.")
    # Validar si las credenciales son correctas
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("\n¡Acceso concedido! Bienvenido.")
        acceso_concedido = True
        break # Rompe el bucle si el inicio de sesión es exitoso
    # Si las credenciales son incorrectas
    else:
        print("\nError: Usuario o contraseña incorrectos.")
    
    # Restar un intento
    intentos -= 1

# Mensaje final si se agotan los intentos
if not acceso_concedido:
    print("\nHa excedido el número de intentos. Acceso bloqueado.")