CREATE TABLE vacunas(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre varchar(20) UNIQUE NOT NULL,
estado BOOL DEFAULT true,
fecha_vencimiento DATE,
procedencia ENUM('USA','CHINA','RUSIA','UK'),
lote VARCHAR(10)
);

CREATE TABLE vacunatorios(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) NOT null,
latitud FLOAT,
longitud FLOAT,
direccion VARCHAR(200),
horario_atencion VARCHAR(200),
-- la llave foranea(FK Foreign Key) es la representacion de la relacion entre la otra tabla e indicara todo su contenido representado solo por su  id
-- La FK siempre va de lado de muchos
vacuna_id INT,
FOREIGN KEY(vacuna_id) REFERENCES vacunas(id)
);

-- Un vacunatorio podra tener una sola vacuna, pero una vacuna puede estar presente en varios vacunatorios 
-- Vacunas < Vacunatorios

