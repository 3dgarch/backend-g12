from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS, cross_origin


app = Flask(__name__)

# si solamente llamamos a la clasey le pasamos la instancia de la clase flsk creara los permisos para que todos puedan acceder(Allowed-Origin), para que cualquier metodo pueda ser consultado(Allowed-Method) y para cualquier header(Allowed-Headers)
# resources='http://127.0.0.1:5000'
CORS(app=app,origins=['http://127.0.0.1:5000','http://127.0.0.1:5500'],methods='GET',allow_headers=['Content-Type'])


# variables
clientes = [
    {
        "nombre":"edgar",
        "apellidos":"chavez garcia",
        "id":1
    }
    
]

# funciones globales
def buscar_usuario(id):
    # iterar la lista y buscar el cliente por ese id, y si no existe imprimir un mensaje
    # v1
    #  for cliente in clientes:
    #     if cliente.get('id') == id:
    #         return cliente
            
    # v2
    for posicion in range(0,len(clientes)):
        if clientes[posicion].get('id') == id:
            return(clientes[posicion], posicion)
    



# definicion ruta inicial
@app.route('/')
def estado():
    hora_del_servidor = datetime.now()
    return{
        'status': True,
        'hour': hora_del_servidor.strftime('%H:%M:%S'),
    }

# ruta clientes
@app.route('/clientes', methods=['POST', 'GET'])
def obtener_clientes():
    # request: solo puede ser llamado en cada controlador(funcion que se ejecutara cuando se realice una peticion desde el frontend)
    print(request.method)      # mostrara el tipo de metodo al cual esta haciendo la consulta el front
    print(request.get_json())  # mostrara los datos enviados desde el front en un diccionario

    
    if request.method == 'POST':
        # ingresara cuando el metodo sea post
        data = request.get_json()
        
        data['id'] = len(clientes) + 1
        clientes.append(data)
        return {
            'message': 'Cliente agregado exitosamente',
            'client': data
        }
    elif request.method == 'GET':
        # ingresara cuando el metodo sea get
        return {
            'message': 'Lista de clientes',
            'clients': clientes
        }

@app.route('/cliente/<int:id>', methods=['GET','PUT','DELETE'])
def gestion_usuario(id):
    #pass #para que no de error mientras no se define contenido
    print(id)
    if request.method == 'GET':
            usuario = buscar_usuario(id)
            if usuario:
                return usuario[0]
            else:        
                return({
                    'message':'El usuario no se encontro'
                },404) # 404 > status
            
    elif request.method == 'PUT':
        resultado = buscar_usuario(id)
        if resultado:
            #modificar el usuario

            #resultado[0] > usuario
            #resultado[1] > posicion

            # extraemos la informacion del body y lo almacenamos en una variable
            data = request.get_json()

            # en ese diccionario agregamos una llave 'id' y almacenaremos el id del usuario que esta en la posicion 0 de la tupla del usuario encontrado
            data['id'] = resultado[0].get('id')

            # extraeremos la posicion del usuario devuelta en la posicion 1 de la tupla de buscar_usuario()
            posicion = resultado[1]

            # modificar ese usuario con el nuevo valor
            clientes[posicion] = data

            return data
            
        else:
            return{
                'message':'El usuaruio a modificar no se encontro'
            }, 404

    elif request.method == 'DELETE':
        resultado = buscar_usuario(id)
        if resultado:
            [usuario ,posicion] = resultado

            cliente_eliminado = clientes.pop(posicion)

            return{
                'message':'Cliente eliminado exitosamente',
                'cliente': cliente_eliminado
            }
        else:
            return{
                'message':'El cliente a eliminar no se encontro'
            },404


# ejemplo cross_origin
@app.route('/ejemplo_ruta',methods=['GET'])
@cross_origin(origins=['http://inkafarma.com','http://inkaframa.pe'])
def obtenir_clientes():
    pass

    







# debug > si esta habilitaro(true) se reiniciara automaticamnete el servidor cada vez que guardemos cambis en cualquier archivo

# port > indicara que puerto queremos utilizar, por defecto es el 5000(port=8080)
app.run(debug=True)