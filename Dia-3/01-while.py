# mientras que (while)
numero = 0
while numero < 10:
    #pass #pass: no hace nada, solo es para que no bote error hasta poner una logica
    print(numero)
    numero+=1
else:
    print("El while termino!")



# ejercicio
par, impar = 0,0
numeros = [1,2,3,4,5,6,7,8]

for numero in numeros:
    if numero % 2 == 0:
        par +=1
    else:
        impar +=1
print('Hay {} numeros pares'.format(par))
print('Hay {} numeros impares'.format(impar))


#while
pos = 0

while pos <len(numeros):
    if numeros[pos] % 2 == 0:
        par +=1
    else:
        impar+=1
    pos +=1