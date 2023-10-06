# librerias
from flask import Flask
from datetime import datetime
from flask_restful import Api


# Archivos
from controllers.ingredientes import IngredientesController
from config import conexion



app = Flask(__name__)

# creamos la instacia de flask_restful.Api y le indicamos que toda la configuracion que haremos se agrege a nuestra instancia de flask
api = Api(app=app)

# aca se almacenara todas las variables de configuracion de mi proyecto flask. en ella se podran encontrar algunas variables como DEBUG y ENV , entre otras
# app.config > es un diccionario en el cual se almacenaran las variables por llave: valor
#print(app.config)

# adignamos la cadena de conexion a nuestra DB
# tipo://usuario:password@dominio:puerto/base_de_datos
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/recetario'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MY3Ezed1905@127.0.0.1:3306/recetario'

# para jalar la configuracion de mi flask y extraer su conexion a la DB
conexion.init_app(app)


# con el siguiente comando indicaremos la creacion de todos las tablas en la DB
# emitira un error si es que no hay niguna trabla a crear
# emitira un error si no le hemos instalado el conector correctamente
# tenemos que declarar en el parametro app nuestra aplicacion de flask
#conexion.create_all(app = app)
with app.app_context():
    conexion.create_all()



@app.route('/status', methods=['GET'])
def status():
  return{
    'status': True,
    'date':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
  }

@app.route('/')
def inicio():
  return 'Bienvenidos a mi API de recetas'


# Ahora definimos las rutas que van a ser utilizadas con un determinado controlador
api.add_resource(IngredientesController, '/ingredientes','/ingrediente')





























# comprobara que la instancia de la clase Flask se este ejecutando en el archivo principal del proyecto
# esto se usa para crea multiples instancias y generar un posible error de flask
if __name__ == '__main__':
  app.run(debug=True)

