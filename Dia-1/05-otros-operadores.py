# Operadores de comparacion

numero1 , numero2 = 10, 20

# NOTA: En python no tenemos el triple igual(===)



# Igual que
print(numero1 == numero2)

# Mayor que | Mayor igual que
print(numero1 > numero2)
print(numero1 >= numero2)

# Menor que | Menor igual que
print(numero1 < numero2)
print(numero1 <= numero2)

# Diferente de
print(numero1 != numero2)


# Operadores Logicos
# en js se utiliza && en python se utliza and
print((10>5) and (10<20))

# en js se utiliza || en python se utliza or
print((10>5) or (30<20))


# Operadores de Identidad(sirven para ver si estan apuntando a la misma direccion de memoria)
# is
# is not

verduras  = ['apio', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['apio', 'lechuga', 'zapallo']

# Nota: las colleciones de datos son variables mutables(cuando cambio su contenido se veran reflejadas en todas las copias)

verduras2[0] = 'peregil'
verduras[1] = 'manzana'

verduras4 = verduras.copy() # copy(): hace una copia pero se guardara en nuva posicion de memoria
verduras4[0] = 'pepino'

print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)

print('la posicion de la variable verduras es: ',id(verduras))
print('la posicion de la variable verduras2 es: ',id(verduras2))
print('la posicion de la variable verduras4 es: ',id(verduras4))


# si hablamos  de variables primitivas(str,int,float,boolean,date) al hacer una copia compartira su mismo espacio de memoria, PERO al hacer una modificacion este cambiara su espacio de memoria
nombre = 'Juan'

nombre2 = nombre
print(nombre2 is nombre)
print(id(nombre))
print(id(nombre2))

nombre2 = 'Edgar'
print(nombre)
