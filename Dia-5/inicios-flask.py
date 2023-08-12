# no se puede crear un archivo con el mismo nombre de la libreria que se va utilizar

# importacion de libreria
from flask import Flask

#import datetime de python
from datetime import datetime



# instancia de la libreria Flask()
# __name__   ->muestra si el archivo es el archivo raiz o principal(__main__) del proyecto
app = Flask(__name__)

# los decoradores es un patron de software que se utilizan para modificar el funcionamiento de un metodo o una clase en particular sin la necesidad de emplear otros metodos como la herencia 
@app.route('/')

# voy a modificar el comportamiento del metodo route para cuando su ruta sea '/' y su nuevo comportamiento sera el siguiente definido en la funcion inicial
def inicial():
    print("Me llamaron!")
    # siempre en los controladores tenemos que devolver una respuesta
    return 'Bienvenidos a mi primer Api 🔌' # windows + .


@app.route('/api/info')
def info_app():
    return {
        #para dar formato a la fecha se utiliza: strftime() > string from time
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S') #devuelve la fecha actual del servidor
    }










# run(): para inicializar servidor de Flask
# debugging >significa que estamos en modo de prueba y que con ello cada vez que guardamos se reinicia el servidor automaticamente
app.run(debug=True)

# !!!!!!
# todo lo que declaramos luego de la llamada am metodo run() nunca se ejecutara ya que el metodo run() hace que el programa se quede 'colgado' esperando una peticion del usuario