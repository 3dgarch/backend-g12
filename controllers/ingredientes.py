from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente


# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase
class IngredientesController(Resource):

  def get(self):
    #vamos a crear una sesion en la cual ejecutaremos una query
    resultado = conexion.session.query(Ingrediente).all
    print(resultado)
    return{
      'message': 'Yo soy el get de los ingredientes'
    }
  def post(self):
    print(request.get_json())

    # registramos un nuevo ingrediente
    try:
      nuevoIngrediente = Ingrediente()
      nuevoIngrediente.nombre = 'Leche evaporada'

      # ahora guardo la informacion en la DB. 
      # add() > estamos creando una nueva transaccion 
      conexion.session.add(nuevoIngrediente)

      # commit > sirve para guardar las cambios de manera permanente en la DB
      conexion.session.commit()

      return{
        'message':'Ingrediente regsitrado exitosamente'
      }
    except Exception as e:
      print(e.args[0])

      # si hubo un error al momento de hacer alguna modificacion e la DB entonces 'retrocederemos' todas las modificaciones y no realizaremos ningun cambio n
      conexion.session.rollback()
      return{
        'message':'Hubo un error en el registro',
        'content': e.args[0]
      }