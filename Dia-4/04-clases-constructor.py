class Animal:
    # nombre = ''
    # sexo = ''
    # patas = 0

    # metodo constructor: este metodo se llamara cuando vayamos a crear una nueva instancia
    def __init__(self,nombre,sexo,patas):
        self.nombre = nombre
        self.sexo = sexo
        self.patas = patas
    def descripcion(self):
        return 'yo soy un {}, soy {}, y tengo {} patas'.format(self.nombre,self.sexo,self.patas)
        
foca = Animal('foca','m',2)
caballo = Animal('cabello','m',4)
gato = Animal('gato','f',4)

print(foca.descripcion())