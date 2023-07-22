# una colecciones es una variable que  puede almacenar varios valores

# LIST (listas)

nombre = ['cesar','pedro','magaly']

combinada = ['eduardo', 20, False, 15.5, [1,2,3]]

# las listas siempre empiezan en la posicion 0
print(nombre[0])

# cuando hacemos el uso de valores negativos en una lista  internamente python le dara vuelta
print(nombre[-1])


# METODOS

# pop(): remueve el ultimo elemento d ela lista y se puede almacenar en otra lista
resulta = nombre.pop() 

# append(): ingresa un nuevo elemento a la ultima posicion de la lista
nombre.append('juana')

# del: elimina el contenido de una posicion de la lista pero no lo podemos almacenar en otra variable
del nombre[0]

# clear(): limpiara toda la lista
nombre.clear()

# para indicar una sub seleccion de una lista
print(combinada[1:2])

x = combinada[:] # .copy()

print(combinada[:])
#desde el inicio  hasta <2
print(combinada[:2])

#desde la posicion 2 hasta el final
print(combinada[2:])


meses_dscto = ['enero', 'marzo', 'julio']
mes = 'septiembre'
mes2 = 'enero'

print(mes not in meses_dscto)
print(mes2 in meses_dscto)


# si Hacemos una sumatoria en las listar estas se combinaran en cual la segunda lista ira despues de la primera
seccion_a = ['Martha','Jorge']
seccion_b = ['Jose','Marcos']
print(seccion_a + seccion_b)

# input: sirve para esperar un dato ingresado por el usuario
dato = input('ingresa tu nombre: ')
print(dato)



# TUPLAS: No se pueden modificar su valor una vez creada

cursos = ('backend', 'frontend')
print(cursos[1])

# en la tupla solamente no podemos alterar los valores pertenecientes a ella. pero si dentro de esta hay una lista u otr coleccion de datos, si se podra modificar
variada = (1,2,3,[4,5,6])
variada[3][0]='hola'

print(variada)
print(2 in variada) # true

# para ver la cantidad de elementos que conforman una tupla o una lista
print(len(variada)) #NOTA: posicion siempre empieza desde cero


# CONJUNTOS
#coleccion de datos DESORDENADA, una  vez que se crea ya no se puede acceder a las posiciones de sus elementos
estaciones = {'vernano','otonio','primavera','invierno'}

print(estaciones)

#se agrega de forma aleatoria
estaciones.add('otro')

#quita el ultimo elemento aleatoriamente
estacion = estaciones.pop()



# DICCIONARIOS
#una coleccion de datos desordenada pero cada elemento obedece a una llave definida
persona = {
  'nombre': 'edgar',
  'apellido': 'chavez',

}

print(persona['apellido'])

#hacemos busqueda de una determinada llave y si no lo encuentra mandamos un sms
print(persona.get('apellido','No existe'))

#devuelve todas las llaves de mi diccionarios
print(persona.keys())

#devuelve una tupla con la llave y valor
print(persona.items())

#devuelve todos los contenidos de mi diccionario
print(persona.values())

# eliminar una llave de un diccionario
persona.pop('apellido')


