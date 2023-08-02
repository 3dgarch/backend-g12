# variable global
nombre = 'Eduardo'

#si definimos una variable de manera global pero la queremos modificar dentro de una funcion, no sera posible ya que al momento de querer modificarla nos pedira que esa variable exista de manera aislada dentro de esa funcion, no sera posible ya que al momento de querer
def saludar():
    #global: palabra reservada para poder utilizar la variable global
    global nombre
    nombre = nombre * 2
    print(nombre)

saludar()

#ahora definimos una variable local
# si definimos variables dentro de la funcion solamente estas podran ser usadas dentro de las mismas mas no fuera de ellas aun asi mandemos a llamar a la funcion, por que la variable se crea cuando se llama y se destruye cuando se termina de ejecutar esa funcion(ese sub bloque de codigo)
def ejemplo():
    ganancia = 0.15
ejemplo()