# Encapsulamiento -> se declara tipos de accesibilidad a los atributos y metodos de una clase

class Producto:
    def __init__(self, nombre, precio):
        # Existen 3 tipos de accesibilidad a los atributos y metodos de una clase:
        # public
        self.nombre = nombre
        self.precio = precio
        
        # private(__ejemplo)
        self.__ganancia = self.precio * 0.30

    def mostrar_info(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'ganancia': self.__ganancia,
            'igv':'{:.2f}'.format(self.__calcular_igv())
        }
    def __calcular_igv(self):
        resultado = self.precio * 0.18
        return resultado


