# DFU
# Funciones Defenidas por el Usuario

def sumar(numero1, numero2):
    '''Funcion que recibe parametros'''
    print('se realizara la sumatoria...')
    print(numero1 + numero2)

sumar(5,5)

#imprimir documentacion de funcion
print(sumar.__doc__)



# funcion con retorno(diccionario)
usuario=[]
def registrar(nombre,email,telefono):
    '''funcion que registra un usuario y lo guarda en una lista'''
    usuario.append({
        'nombre':nombre,
        'email':email,
        'telefono':telefono
    })
    #retorna una tupla
    return({
        'message': 'Usuario registrado',
        'usuario': usuario[0]
    },1,True)

#  1pos      2pos   3pos
resultado, numero, booleano = registrar('edgar','edgar@gmail.com','56321478')
print(resultado)
print(numero)
print(booleano)


#registrar productos
productos=[]

def registrar_productos(nombre,precio,estado=True,almacen='Almacen del cercado'):
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'estado': estado,
        'almacen': almacen
    })
    return 'producto agregado exitosamente'

#siempre tenemos que pasar primero los parametros que no tienen valores por defecto
registrar_productos('tomate',4.50)
registrar_productos('Apio',1.50,False)
registrar_productos('Cebolla',2.80)

#otra manera de pasar productos
registrar_productos(almacen='Almacen del Lima',nombre='pescado',precio=2.50)



#ingresar n parametros
def alumnos(*args):
    print(args)

alumnos('Eduardo','Nahia','Pedro')
alumnos('Martha',30,False)


# Kwargs = keyward argument
# si en la funcion querenn¿mos recibir un numero ilimitado de argumentos pero estos deben de tener su nombre de parametro con su valor entonces usaremos los kwargs
def ingresarProductos(**kwargs):
    print(kwargs)

ingresarProductos(nombre='Manzana',precio=2.00,stock=20)


# Recursividad
def saludar_n_veces(limite):
    if(limite ==0):
        return 'llege al limite'
    print('Hola')
    return saludar_n_veces(limite-1)

resultado = saludar_n_veces(10)

print(resultado)


# 5!  = 5 * 4 * 3 * 2 *1 = 120

def factorial(limite):
    if(limite == 0):
        return 1
    return limite * factorial(limite-1)

resultado = factorial(5)
print(resultado)


def duda(nombre_per, origen_per):
    if nombre_per == 'andrea' and origen_per == 'arequipa':
        return 'me caso'
    else:
        return 'Next'



# OPERADORE TERNARIO

nombre_per = 'andrea'
origen_per = 'arequipa'


resultado = 'Me caso' if nombre_per == 'Andrea' and origen_per == 'lima' else 'Next'

# LAMBDA FUNCTION
# son funciones que puede tener un numero indeterminado de argumentos pero solamente una expresion(una sola linea de ejecucion de codigo)ademas esta sera retornada
cuadrado = lambda numero: numero **2

rpta = cuadrado(4)
print(rpta)


igv = lambda precio: precio * 0.18 # 1.18
rpta_igv = igv(100)
