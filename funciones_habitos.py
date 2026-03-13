def registrar_habitos():
    '''
    Función que genera una lista y pide al usuario que ingrese actividades diarias.
    Las actividades diarias se guardan como string dentro de la lista "actividades".

    Returns
    -------
    actividades : lista
        Guarda las actividades diarias del usuario.

    '''
    seguir = "si"
    actividades = []
    while seguir == "si":
        actividad = input("Ingrese una actividad diara: ")
        actividades.append(actividad)
        seguir = input("Quiere seguir ingresando? (si/no) ")
    return actividades

def analizar_habitos(lista_actividades):
    '''
    En base a la función registrar_habitos, esta función cuenta la cantidad de veces que se repite una actividad en la lista y se guardan en el diccionario.

    Parameters
    ----------
    lista_actividades : lista
        Guarda las actividades diarias del usuario..

    Returns
    -------
    analisis : diccionario
        Como clave tiene el nombre de las actividades y el valor es el número de veces que se repite la palabra dentro de la lista de actividades.

    '''
    analisis = {}
    for nombre_actividad in lista_actividades:
        if nombre_actividad not in analisis:
            analisis[nombre_actividad] = 1
        else:
            analisis[nombre_actividad] += 1
    return analisis
