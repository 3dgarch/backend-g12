# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento,nacionalidad, dni , ademas tambien una clase Alumno y una clase Docente en la cual el alumno,  a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. en base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo ometodo que deba ser privado

# clase persona
class Persona:
    def __init__(self,nombre,fec_nac,dni,nacionalidad):
        self.nombre = nombre
        self.fec_nac = fec_nac
        self.dni = dni
        self.nacionalidad = nacionalidad
    def saludar(self):
        print("Hello my name is: {}".format(self.nombre))


# clase alumno
class Alumno(Persona):
    def __init__(self,nombre,fec_nac,dni,nacionalidad,cursos):
        super().__init__(nombre,fec_nac,dni,nacionalidad)

        #atributo privado
        self.__cursos = cursos
    
# clase docente
class Docente(Persona):
    def __init__(self,nombre,fec_nac,dni,nacionalidad,cts,seguro_social):
        super().__init__(nombre,fec_nac,dni,nacionalidad)
        self.cts = cts
        #atributo privado
        self.__seguro_social = seguro_social

