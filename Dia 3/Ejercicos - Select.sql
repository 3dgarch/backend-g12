-- insert Data
-- en DB y lenguajes de programacion se usa el ISO 8601 > YYYY-MM-DD
INSERT INTO vacunas(nombre,estado,fecha_vencimiento,procedencia,lote)VALUES
					('PFIZER',true,'2023-08-16','USA','123JKL'),
                    ('SINOPHARM',true,'2023-10-10','CHINA','VXCBS'),
					('SPUTNIK',false,'2022-10-04','RUSIA','GFDJS');
                    
INSERT INTO vacunatorios(nombre,latitud,longitud,direccion,horario_atencion,foto,vacuna_id)VALUES
						('Camino Real',14.121,-21.321,'AV Girasol 115','LUN-VIE 07:00 - 16:00',null,1),
                        ('Hospital Regional',17.521,-21.151,'JR Junin','LUN-VIE 07:00 - 16:00',null,2),
                        ('Lazarte',20.321,-31.126,'AV Grau 520','LUN-VIE 07:00 - 16:00',null,3);

-- mostrar vacunas diferentes a USA
-- != | NOT LIKE | <> | NOT 
SELECT * FROM vacunas WHERE procedencia <> 'USA';

SELECT * FROM vacunatorios WHERE horario_atencion LIKE '%MIE%'
						   OR horario_atencion LIKE '%LUN-VIE%'
					       OR horario_atencion LIKE '%LUN-SAB%';
                           
SELECT * FROM vacunatorios WHERE vacuna_id = 1 AND foto IS NOT NULL;               
                        


                      