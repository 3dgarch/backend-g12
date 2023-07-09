nombre = 'Edgar'
estado_civil = 'viudo'

print(nombre)

# concatenar (juntar) varios valores
print('el nombre es: ',nombre, 'del usuario')

# para usar el metodo format(). debemos coincidir las mismas veces de variables con las llaves
print('La persona {} es {}'.format(nombre, estado_civil))

# ademas podemos agregar la posicion de la variable que queremos imprimir dentro de las llaves
print('{1} es una persona {0}'.format(estado_civil, nombre))