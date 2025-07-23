# calculadora_promedios.py

def ingresar_calificaciones():
    nombres = []
    calificaciones = []
    
    while True:
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue
        
        try:
            nota = float(input(f"Ingrese la calificación para {materia} (0 - 10): "))
            if nota < 0 or nota > 10:
                print("La calificación debe estar entre 0 y 10.")
                continue
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        nombres.append(materia)
        calificaciones.append(nota)

        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break

    return nombres, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []
    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    return indice_max, indice_min

def main():
    print("=== Calculadora de Promedios ===")
    nombres, calificaciones = ingresar_calificaciones()

    if not nombres:
        print("No se ingresaron materias. Finalizando el programa.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    idx_max, idx_min = encontrar_extremos(calificaciones)

    print("\n--- Resumen Final ---")
    for i, (nombre, nota) in enumerate(zip(nombres, calificaciones)):
        print(f"{i+1}. {nombre}: {nota}")

    print(f"\nPromedio general: {promedio:.2f}")

    if aprobadas:
        print("Materias aprobadas:")
        for i in aprobadas:
            print(f"  - {nombres[i]} ({calificaciones[i]})")
    else:
        print("No se aprobaron materias.")

    if reprobadas:
        print("Materias reprobadas:")
        for i in reprobadas:
            print(f"  - {nombres[i]} ({calificaciones[i]})")
    else:
        print("No se reprobaron materias.")

    if idx_max is not None:
        print(f"\nMejor calificación: {nombres[idx_max]} ({calificaciones[idx_max]})")
    if idx_min is not None:
        print(f"Peor calificación: {nombres[idx_min]} ({calificaciones[idx_min]})")

    print("\nGracias por usar la calculadora de promedios. ¡Hasta luego!")

if __name__ == "__main__":
    main()
