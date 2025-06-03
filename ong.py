import sys
fact_ = []
prod_ = []

def factorial ():
    # Factorial:
    # n! = n * n -1 * n -2 * ... *2 *1
    # Ejemplo factorial:  5! = 5 * 4 * 3 * 2 * 1 = 120

    n = int(input("ingrese un número entero positivo: "))
    factorial = 1
    i=0
    while i < n:
        print(i)
        print (f"mostrará {n} veces")
        factorial = factorial * (i + 1)
        print("fact: ", factorial)
        i+=1
        print("fin")

def productoria ():
    # Productoria:
    #  Ejemplo: 𝐴 = [3,6,4,2,8]
    #  ∏𝐴𝑖 =  3 * 6 * 4 * 2 * 8

    a = [4,6,7,4,3]
    productoria = 1
    for elemento in a:
        productoria = productoria * elemento
        print(productoria)

if len(sys.argv) != 1:
    print("el comando necesita un argumento :  python ong.py")
    sys.exit(1)

n = len(sys.argv)
for i in range (n):
    if fact_(i) in sys.argv[i]:
        factorial()
    elif prod_(i) in sys.argv[i]:
        productoria()

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)