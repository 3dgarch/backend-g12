# IF - ELSE
#python al no utilizar llaves para definir bloque de un comportamiento diferente tenemos que utilizar tabulaciones(TAB)
edad = int(input("ingresa tu edad"))

if(edad > 18):
  #la alineacion nunca debe variar si estamos en el mismo bloque
  print('mayor edad')
elif edad > 15:
  print('puede ingresar')

else:
  print('menor de edad')
