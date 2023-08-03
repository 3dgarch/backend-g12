# Programacion Orientada a Objetos -> POO | OOP
# La programacion debe estar creada en base  a clases
# Toda parte del codigo debe de ser tratada como si fuese una plantilla
# clases -> son plantillas para que puedan ser utilizadas varias veces sin la necesidad de modificar su forma en relacion al objeto sino que al revez

class Persona:
    # las variables creadas dentrop de la clase pasan a llamarse atributos
    nombre = 'Juan'
    fecNac = '2000-01-12'

    # metodos
    def saludar(self):
        # self = this
        self.decir_nombre()
        self.nombre
        print('Hola como estan')
    def decir_nombre(self):
        print('Digo el nombre')

# cuando una variable se crea a raiz de una clase, esta variable pasa a llamar instancia(instancia -> copia en su totalidad de la clase)
persona1 = Persona()

print(persona1)