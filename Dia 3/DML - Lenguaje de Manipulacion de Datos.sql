USE prueba;
-- DML  > Data Manipulation Language (Lenguaje de Manipulacion de Datos)
-- INSERT, SELECT, UPDATE, DELETE
 
 -- insert
INSERT INTO clientes(nombre,documento,tipo_documento,estado)VALUES
					('Eduardo','47859856','DNI',true);
INSERT INTO clientes(nombre,documento,tipo_documento,estado)VALUES
					('Estefani','47956552','DNI',true),
                    ('Fabian','1495562565','RUC',false);

-- select
SELECT nombre,documento FROM clientes;
SELECT * FROM clientes;          

SELECT * FROM clientes WHERE documento = '47859553' AND (nombre ='Rosa' OR nombre = 'Eduardo');
SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = 'true';
SELECT * FROM clientes WHERE nombre LIKE 'Edu%o';

-- update
UPDATE clientes SET nombre ='Ramiro', documento = '47859856'
				WHERE id = 1 AND nombre = 'Eduardo';
                
-- Modo seguro > es el modo que nos impide hacer actualizaciones (UPDATE) y eliminaciones (DELETE) sin usar
-- una columna que sea indice (PK)
-- Para desactivar el modo seguro
SET SQL_SAFE_UPDATES = false;


-- delete
DELETE FROM clientes WHERE id = 1;       
                    