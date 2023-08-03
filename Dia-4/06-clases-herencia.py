# Herencia -> extraer informacion de una clase padre

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    def saludar(self):
        return 'Hola soy {}'.format(self.nombre)

class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo,padres):
        
        #super() -> sirve para mandar a llamar a la clase  de la cual estamos heredandoo la herencia, ademas solo sirve para acceder a los metodos mas no a los atributos
        super().__init__(nombre, apellido, correo)
        self.padres = padres

    def info(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'padres': self.padres,
            'saludar': super().saludar()
        }
        

