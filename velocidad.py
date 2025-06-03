import sys

# lista de muestra de velocidades 
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

# función de velocidad promedio
def velocidad_promedio ():
    # Iteración de lista velocidad y suma de todos los elementos
    suma = 0
    for item in velocidad:
        suma = item + suma
    #print(f"suma: {suma}")
    # Obtención de la cantidad de elementos dentro de la lista velocidad
    cantidad = len(velocidad)
    #print(f"cantidad : {cantidad}")
    # Cálculo del promedio de la lista velocidad
    promedio = suma / cantidad
    #print(f"promedio : {promedio}")

    lista_filtrada = []

    # Obtención de la posición de elementos dentro de la lista velocidad mayores al promedio
    for indice, elemento in enumerate(velocidad):
        if elemento > promedio:
            lista_filtrada.append(indice)
    print(lista_filtrada)

# verificación de entrada de argumento
if len(sys.argv) != 1:
    print("el comando necesita un argumento :  python velocidad.py")
    sys.exit(1)
else:
    velocidad_promedio()