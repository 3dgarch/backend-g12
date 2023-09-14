# factory
from faker import Faker
#from faker.providers import internet, phone_number, person

fake = Faker()

# le agregamos un provier adicional a nuestro faker para que ahora pueda utilizar los tradicionales y los de internet
##fake.add_provider({internet, person})

def generar_alumnos(limite):

  for persona in range(limite):
    
    nombre = fake.first_name()
    apePat = fake.last_name()
    apeMat = fake.last_name()
    correo = fake.ascii_free_email()
    #telefono = fake.phone_number()

    #telefono = fake.random_int(min=91111111, max=99999999)
    #fake.bothfy(text='asd###??', letters='xdhola')
    telefono = fake.bothify(text='9########') 

    
    #sql = '''INSERT INTO alumnos (nombre,apellido_paterno,apellido_materno,correo,numero_emergencia) VALUES
    #                            ('%s', '%s', '%s', '%s', '%s');''' %(nombre,apePat,apeMat,correo,telefono)

    #metodo reciente
    sql = '''INSERT INTO alumnos (nombre,apellido_paterno,apellido_materno,correo,numero_emergencia) VALUES
                                ('{}', '{}', '{}', '{}', '{}');''' .format(nombre,apePat,apeMat,correo,telefono)
    
    print(sql)

#generar_alumnos(2)

def generar_niveles():
  secciones = ['A','B','C']
  ubicaciones = ['Sotano','Primer Piso','Segundo Piso','Tercer Piso']
  niveles = ['Primero','Segundo','Tercero','Cuarto','Quinto','Sexto']

  # iterar los niveles y en cada nivel colocar como minimo dos secciones y como maximo 3(random_int) y luego agregar aleatoriamente la ubicacion a ese nivel

  # Primero A Segundo Piso
  # Primero B Tercer Piso
  # Segundo A Sotano

  for nivel in niveles:
                  # entre 2 hasta <= 3 (0 | 2 | 3)
    pos_secciones = fake.random_int(min=2, max=3)
    for posicion in range(0, pos_secciones):
      pos_ubicacion=fake.random_int(min=0, max=3)

      seccion = secciones[posicion]
      ubicacion = ubicaciones[pos_ubicacion]
      nombre = nivel

      sql = '''INSERT INTO niveles(SECCION, UBICACION, NOMBRE) values
                          ('%s','%s','%s');''' %(seccion, ubicacion, nombre)
      
      # print('nivel',nivel)
      # print('seccion', secciones[posicion])
      # print('ubicacion', ubicaciones[pos_ubicacion])

      print(sql)

#generar_niveles()
  
def generar_niveles_alumnos():
  #generar un nuemro aleatorio que sera el id del alumno y el id del nivel y un anio de manera en la cual no se puede volver a genear ese mismo alumno conun nivel inferior pero con un anio superior
  #  Alumni_Id     Nivel_Id       Year
  #      1             3          2000   // 3 > Segundo A        
  #      1             1          1999   // 1 > Primero A ✔️       
  #      1             1          2002   // 1 > Primero A ❌      
  pass