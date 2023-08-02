notas = [10,20,16,8]

# for(let i=0; i<10; i++){....}
# en cada iteracion de la lista notas tendremos su valor y lo almacenaremos en una variable llamadda nota

for nota in notas:
    print(nota)

# creamos un bucle manual para una iteracion hasta el limite definido en el range
for numero in range(10):
    print(numero)

# si colocamos dos parametros, el primero significara el numero inicial y el segundo el tope
for numero in range(5,20):
    print(numero)

# si colocamos dos parametros, el primero significara el numero inicial, el segundo el tope y el tercero el numero de incremento
for numero in range(5,10,2):
    print(numero)


# ejercicio
#imprimir los 3 valores iniciales de notas
notas = [10,20,15,16,18]

for nota in notas[:3]: # : -> hasta la posicion 3
  print(nota)

for posicion in range(3):
    print(notas[posicion])





productos = ['Manzanas','Peras','Naranja','Lima']

busqueda = input('Buscar producto: ')

for producto in productos:
    if producto == busqueda:
        print("El producto existe")
        break
else:
    print("No hay stock")