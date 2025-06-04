def calcular(**kwargs):
  s = 0
  for key, value in kwargs.items():

    # Condicional "if in"
    if "fact_" in key:

      # Factorial:
      # n! = n * n -1 * n -2 * ... *2 *1
      # Ejemplo factorial:  5! = 5 * 4 * 3 * 2 * 1 = 120

      #n = int(input("ingrese un número entero positivo: "))
      factorial = 1
      i=0
      while i < value:
        factorial = factorial * (i + 1)
        i+=1
      print(f"El factorial de {value} es", factorial)

    # condicional "elif in"
    elif "prod_" in key:
      
      # Productoria:
      #  𝐴 = [3,6,4,2,8]
      #  ∏𝐴𝑖 =  3 * 6 * 4 * 2 * 8

      productoria = 1
      for elemento in value:
        productoria = productoria * elemento
      print(f"La productoria de {value} es", productoria)

calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)