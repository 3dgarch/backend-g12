# SQL > Structured Query Language
# un registro es un conjunto de datos y un dato es un valor que por si solo no dice nada

# las DB seben estar en singular
CREATE DATABASE prueba;

# para indicar que DB vas utilizar usamos el comando use
USE prueba;

# tablas
CREATE TABLE  clientes(
#columnas
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
documento VARCHAR(10) UNIQUE,
# ENUM > 
tipo_documento ENUM('C.E','DNI','RUC','PASAPORTE','OTRO'),
# BOOL > true o false
estado BOOL
);