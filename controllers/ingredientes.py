from flask_restful import Resource


# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase
class IngredientesController(Resource):
  def get(self):
    return{
      'message': 'Yo soy el metodo ingredientes'
    }
  def post(self):
    return{
      'message':'Yo soy el post'
    }