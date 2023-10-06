# las tablas que queremos crear en python se representaran en forma de clases y cada columna sera su atributo

# create table ingredientes (id in primary key ...)
from config import conexion
from sqlalchemy import Column, types

class Ingrediente(conexion.Model):
  # ahora esta clase tendra un comportamiento en forma de un model (tabla en la DB)
  # id seria considera como una columna de mi modelo (table)
  #id = Column(type_=int)
  id = Column(type_=types.Integer, primary_key=True, autoincrement=True,)
  nombre = Column(type_=types.String(length=45), nullable=False, unique=True)

 
  # renombrar tabla
  __tablename__ = 'ingredientes'