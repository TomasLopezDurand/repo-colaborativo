def registrar_habitos():
    seguir = "si"
    actividades = []
    while seguir == "si":
        actividad = input("Ingrese una actividad diara: ")
        actividades.append(actividad)
        seguir = input("Quiere seguir ingresando? (si/no) ")

def analizar_habitos(actividades):
    analisis = {}
    for nombre_actividad in actividades:
        if nombre_actividad not in analisis:
            analisis[nombre_actividad] = 1
        else:
            analisis[nombre_actividad] += 1
    return analisis
