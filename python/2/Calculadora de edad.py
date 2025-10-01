# Ejercicio 1: Calculadora de Edad
from datetime import datetime

# Aquí definimos todas las instrucciones.
def ejercicio_calculadora_edad():
    """
    Calcula la edad de un usuario a partir de su fecha de nacimiento en formato DD-MM-AAAA.
    """
    print("\n--- Calculadora de Edad---")
    
    hoy = datetime.now()
    fecha_nac_str = input("Ingrese su fecha de nacimiento (formato DD-MM-AAAA): ")
    
    if not fecha_nac_str:
        print("\nError: La fecha de nacimiento no puede estar en blanco.")
        return

    try:
        dia_nac, mes_nac, anio_nac = map(int, fecha_nac_str.split('-'))

        if not (1 <= dia_nac <= 31):
            print("\nError: El día debe estar entre 1 y 31.")
            return
        if not (1 <= mes_nac <= 12):
            print("\nError: El mes debe estar entre 1 y 12.")
            return
        if not (anio_nac > 1900):
            print("\nError: El año de nacimiento debe ser mayor a 1900.")
            return
            
        fecha_nacimiento = datetime(anio_nac, mes_nac, dia_nac)
        edad = hoy.year - fecha_nacimiento.year
        
        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
            cumplio_anios = "aún no ha cumplido años este año."
        else:
            cumplio_anios = "ya cumplió años este año."
            
        print(f"\n--- Resultado ---")
        print(f"Fecha de nacimiento: {dia_nac:02d}-{mes_nac:02d}-{anio_nac}")
        print(f"Edad del cliente: {edad} años.")
        print(f"El cliente {cumplio_anios}")

    except (ValueError, IndexError):
        print("\nError: Formato de fecha inválido. Use DD-MM-AAAA.")

ejercicio_calculadora_edad()
