#esto es un comentario
#TODO: logica para este controlador

# variables
nombre = "edgar"
edad = 30

# variables de texto 
apellido = "Chavez"

# texto que pueda contener salto de lineas
descripcion = """hola, como estan
amigos"""

#imprime por consola
print('hola mundo')

#type() => mostrara el tipo de variable
print(type(edad))

#python: no se crear una variable sin contenido
#python: None = null | undefined
especialidad = None

#en python no hace validacion de tipo de dato primario (si la variable 'nace' siendo string) normal se puede cambiar su tipo a otro (Boolean, int, float, array, etc)
#en python no existen las constantes
dni = [1,2,3]
dni = 'peruano'
dni = False

#id() => dara la ubicacion de esa variable en relacion a la memoria des dispositivo
print(id(dni))

# declarar variables en una misma linea
mes, dia = "febrero", 12

#del: elimina la variable de la memoria
del mes