import sys

# Diccionario
precios = {'Notebook': 700000,
          'Teclado': 25000,
          'Mouse': 12000,
          'Monitor': 250000,
          'Escritorio': 135000,
          'Tarjeta de Video': 1500000}

if len(sys.argv) > 2:
    argumento1 = int(sys.argv[1])
    argumento2 = str(sys.argv[2])
else:
    argumento1 = int(sys.argv[1])
    argumento2 = ""

# definición de función
def filtrar(diccionario, umbral, modo):
  
  if modo == "mayor" or modo == "":
    filtro = {k for k,v in diccionario.items() if v > umbral}
    print("Los productos mayores al umbral son: ",", ".join(filtro))

  elif modo == "menor":
    filtro = {k for k,v in diccionario.items() if v < umbral}
    print("Los productos menores al umbral son: ",", ".join(filtro))

  else: print("Lo sentimos, no es una operación válida")
  sys.exit()

filtrar(precios, argumento1, argumento2)