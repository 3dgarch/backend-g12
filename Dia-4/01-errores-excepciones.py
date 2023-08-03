# un error es una mala ejecucion del codigo que hara que  mi proyecto o script deje de funcionar
# en python tenemos varios errores para los diferentes sucesos:
# locals()['__builtins__'] -> me retornara del diccionario de locals() todos los errores definidos dentro de py.

# dir() -> nos permite listar estos atributos como strings para poder leerlos facilmente.
# locals() -> nos devuelve todas las variables disponibles que tenemos en python en este scope

#print(dir(locals().get('__builtins__')))

try:
  valor = int(input('Ingresar un numero: '))
  print(valor)
except ValueError:
  # error al intentar convertir de tipo de dato
  print('Error al convertir de string a number')
except Exception as error :
  # except: capturara el error causante impidiendo que el programa deje de funcionar
  print('Ops algo sali mal, intentalo denuevo')
  print(error.args) # muestra el mensaje del error

print('el programa finalizo correctamente')




try:
  resultado = 1/0

  #buscar producto en DB
  producto = None
  if(producto is None):
    raise Exception('El producto no existe')
except:
  print('hubo un error')
else:
  # el else se ejecutara si nunca ingreso  a un except
  print('la divicion se ejecuto sin problemas')
finally:
  # ingresara asi haya un except  o no
  print('Yo me ejecutare si todo fue bien o mal')


# ejemplo
while True:
  try:
    valor = int(input('ingresar un numero'))
    break
  except:
    print('Valor incorrecto, solo pueden ser numero')

print(valor)

