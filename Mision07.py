#   Carlos Badillo García
#   Programa que muestra un menu para que el usuario escoga la función que sera realizada


def dividir(dividendo, divisor): #Función que sirve para realizar una division sin hacer uso de "/, // o %"
    div = dividendo
    cociente = 0

    while divisor <= dividendo:
        dividendo = dividendo - divisor
        cociente = cociente + 1

    print(div, "/", divisor, "=", cociente, ", sobra", dividendo)


def encontrarMayor(): #Función que muestra el número mayor entre un conjunto de números

    mayor = -1
    numero = int(input("Teclea un número [-1 para salir]: "))

    while numero != -1:
        if numero > mayor:
            mayor = numero
        numero = int(input("Teclea un número [-1 para salir]: "))

    if mayor == -1:
        print("No hay valor mayor")
    else:
        print("El mayor es: ", mayor)

def leerOpciones(): #Función para mostrar las opciones a escoger
    print("Misión 07. Ciclos while")
    print("Autor: Carlos Badillo García")
    print("Matrícula: A01377618")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion


def main(): #Función que ejecuta la función para leer las opciones y consecuentemente, todas las demas funciones

    opcion = leerOpciones()

    while opcion != 3:
        if opcion == 1:
            print()
            print("Calculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)
            print()

        elif opcion == 2:
            print()
            print("Teclea una serie de números para encontrar el mayor.")
            encontrarMayor()
            print()

        else:
            print("ERROR, teclea 1, 2 o 3")
            print()

        opcion = leerOpciones()
    print()
    print("Gracias por usar este programa, regresa pronto.")


main()