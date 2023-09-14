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

-- DDL > Data Definition Language > se usara para la definicion de donde se almacenaran los datos en mi DB

-- Para renombrar una tabla con un nuevo nombre
RENAME TABLE nombre_antiguo TO nombre_nuevo;

-- DROP > elimina la tabla y su contenido a diferencia del DELETE aquq solo elimina el contenido
DROP TABLE vacunatorios;

-- eliminar columna de una tabla
ALTER TABLE vacunatorios DROP COLUMN latitud;

-- agregar una columna a  una tabla indicando el tipo y posicion 
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;

-- Rename column > renombra la columna
ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;

-- modificar el tipo de dato de una columna. NO se podra modificar si esa columna tiene datos
ALTER TABLE vacunatorios MODIFY COLUMN foto CHAR(100) UNIQUE NOT NULL;

-- descripcion de tabla
DESC clientes;

-- desactivar safe _mode
set sql_safe_updates=1

