-- JOINS
-- es la manera de ingresar desde una tabla hacia otra mediante una col en comun
use prueba;

SELECT * FROM vacunatorios INNER JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 1;


-- LEFT JOIN
-- traera todo el contenido de la tabla izquierda y adicionalmente el contenido de interseccion con la tabla de la derecha
SELECT * FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id; 

-- RIGHT JOIN
-- traera todo el contenido de la tabla de la derecha y adicionalmente el contenido de interseccion con la tabla de la izquierda
SELECT * FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

-- FUL OUTER JOIN 
-- traera toda la informacion tanto de la tabla de la izquierda como de la derecha y opcionalmente si hay ulguna interseccion lo hara sino no importa
SELECT *
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id UNION
SELECT *
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;



-- si se usa una clausula WHERE o en el SELECT una clumnaambigua(que se repite el mismo nombre) hay que especificar de que tabla estamos hablando
SELECT vacunas.nombre,vacunatorios.nombre FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'pfizer';


-- EJERCICIOS
-- 1. devolver los vacunatorios en los cuales la vacuna sea sinpharm y su horario de atencion dea de LUN-VIE
SELECT *
FROM  vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'SINOPHARM' AND horario_atencion LIKE '%LUN-VIE%';

-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00 IN()
SELECT vaunas.nombre
FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE latitud IN(-5,10);

-- 3. Devolver todos las vacunas que no tengan vacunatorio y solamente su procedencia y nombre
SELECT procedencia, vacunas.nombre
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;
