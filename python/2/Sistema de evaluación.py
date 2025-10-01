# Ejercicio 2: Sistema de Evaluación

def ejercicio_sistema_evaluacion():
    """
    Registra calificaciones de N alumnos en M materias y determina su estado.
    """
    print("\n--- Sistema de Evaluación de Alumnos ---")
    
    try:
        # Pedir el número de alumnos y materias
        num_alumnos = int(input("Ingrese el número de alumnos a evaluar: "))
        num_materias = int(input("Ingrese el número de materias por alumno: "))
        if num_alumnos <= 0 or num_materias <= 0:
            print("Error: El número de alumnos y materias debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: Ingrese un número válido.")
        return

    print("\n" + "="*40 + "\n")
    
    # Bucle exterior: para cada alumno
    for i in range(num_alumnos):
        print(f"--- Capturando datos del Alumno {i + 1} de {num_alumnos} ---")
        
        # Validar que no se dejen campos vacíos
        while True:
            nombre = input("Nombre del alumno: ")
            matricula = input("Matrícula del alumno: ")
            if nombre and matricula:
                break
            else:
                print("Error: El nombre y la matrícula no pueden estar vacíos. Intente de nuevo.")
        
        aprobadas = 0
        reprobadas = 0
        
        # Bucle interior: para cada materia
        for j in range(num_materias):
            while True:
                try:
                    calificacion = float(input(f"  Ingrese calificación de la Materia {j + 1}: "))
                    if 0 <= calificacion <= 10:
                        break
                    else:
                        print("  Error: La calificación debe estar entre 0 y 10.")
                except ValueError:
                    print("  Error: Ingrese un valor numérico para la calificación.")
            
            # Condición de evaluación
            if calificacion > 6:
                aprobadas += 1
            else:
                reprobadas += 1
        
        # Mostrar resumen del alumno
        print("\n--- Resumen Académico ---")
        print(f"Alumno: {nombre} (Matrícula: {matricula})")
        print(f"Materias Aprobadas: {aprobadas}")
        print(f"Materias Reprobadas: {reprobadas}")
        print("\n" + "="*40 + "\n")

    print("--- Fin del Proceso de Evaluación ---")