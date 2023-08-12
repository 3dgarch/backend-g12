 # EJERCICIO 1:
# Escriba un funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo diguje usando *, ejemplo:

# altura: 5
# ancho: 4
# resultado
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()

def dibujar_rectangulo():
    altura = int(input("Ingrese la altura: "))
    ancho = int(input("Ingrese el ancho: "))

    for numero in range(altura):
        for numero2 in range(ancho):
            print("*", end="")
        print("")
            
dibujar_rectangulo()

# EJERCICO 2:
# Escriba una funcion que nosotros le ingresemos el grosor de un octagono y que lo diguje, ejemplo:
# grosor: 5
#      *****
#     *******
#    *********
#   ***********
#  *************
#  *************
#  *************
#  *************
#  *************
#   ***********
#    *********
#     *******
#      *****
#dibujar_octagono()
def dibujar_octagono():
    grosor = int(input("Ingresar el grosor del octagono: "))

    if(grosor == 1):
        return print("No puede tener como grosor el valor de 1")
    
    #formulara para obtener el tope
    tope = (2*(grosor-1))+grosor

    espacio = grosor

    for numero in range(grosor, tope+1, 2):
        espacio -= 1
        espacios = " "*espacio
        simbolo = "*"*numero

        if(numero == tope):
            limite = 0
            while(limite < grosor):
                print(simbolo)
                limite += 1
            break
        print(espacios+simbolo)
    espacio += 1

    for numero in range(tope-2, grosor-1, -2):
        espacios = " "*espacio
        espacio += 1
        simbolo = "*"*numero
        print(espacios+simbolo)

        



# EJERCICIO 3:
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre 2
# si el numero es inpar, se multiplica  por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12
# serie_Collatz()

def serie_collatz():
    numero = int(input("Ingresa un numero: "))
    while(numero != 1):
        if(numero % 2 == 0):
            numero /= 2
        else:
            numero = (numero*3)+1
        print(numero)
