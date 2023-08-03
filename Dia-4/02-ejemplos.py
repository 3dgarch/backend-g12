productoId = input('ingresar el id de un producto')

#buscar en DB un producto
# 1 2 3 4 5 6 7 8 9

try:
    if(productoId == '10'):
        # raise: emitira un error manualmente
        # se utiliza para no continuar con el flujo
        raise Exception('El producto no existe en la DB')
except:
    # ingresa si hubo un error
    print('Ups, algo salio mal')
else:
    # ingresa si no hubo un error
    print('El producto encontrado es: ')

finally:
    # ingresa si hubo o no un error
    print('message','Resultado final')

print('El programa finalizo')