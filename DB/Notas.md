# APUNTES MYSQL

**CREATE**
```sql
CREATE TABLE Legajos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Edad INT NOT NULL,
    Salario DECIMAL(10, 2) NOT NULL,
    FechaNacimiento DATETIME,
    Hora TIME,
    Fecha DATE,
    Activo BOOLEAN
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes (EstudianteID)
) AUTO_INCREMENT=100;
```
- Para ingresar la fecha y hora se debe hacer en este formato: **2023-09-05 14:30:00**
- Las que no tiene NOT NULL son opcionales osea pueden ir vacios
- PRIMARY KEY nos dice no esa columna no va tener NULL o repetidos
- FOREIGN KEY relaciona una columna con otra tabla:
  - Verifica que la referencia exista al insertar o modificar
  - Falla todo la consulta, osea no agrega nada hasta no verificar la consistencia
  - Falla si se borra la referencia del padre
  - 
**Crear una tabla AUXILIAR**
```sql
CREATE TABLE AuxLegajos AS SELECT * FROM Legajos
--Crearla vacia
CREATE TABLE AuxLegajos AS SELECT * FROM Legajos WHERE 1=2
```
**ALTER**

Agregamos una nueva columna. 
En caso que necesitemos que no sea null debemos agregar un valor por default en caso que tengamos ya registros previos.
```sql
ALTER TABLE Productos ADD Color VARCHAR(10) NOT NULL DEFAULT 'Valor';
ALTER TABLE Productos MODIFY COLUMN Color VARCHAR(100) NOT NULL DEFAULT 'otro';
```
**DROP**

Eliminar el objeto tabla. Siempre y cuando no tenga realacion que lo restrinja
```sql
Drop TABLE Productos
```
----
### **SELECT**
Obtener la descripcion de la tabla
```sql
DESC Productos
```
Estructura basica
```sql
SELECT * FROM Productos
SELECT ID-Producto FROM Productos
SELECT ID-Producto FROM Productos WHERE Localidad='Capital'
```
Evitar repetidos
```sql
SELECT DISTINCT Localidad FROM Productos
```
**WHERE**
- puede combinarse con los operadores de comparacion:  =, <, >, <> o !=, IN
- puede combinarse con los operadores de comparacionAND, OR
```sql
SELECT * FROM Productos WHERE Tamaño = 'Grande' AND Precio > 5
SELECT * FROM Productos WHERE ID IN (101,104)
```
**ORDER BY**
- Ordena por una columa o varias columnas
- Si no se pone nada es por default ASC
 
```sql
SELECT * FROM Productos WHERE Tamaño = 'Grande' ORDER BY Precio ASC
SELECT * FROM Productos WHERE Tamaño = 'Grande' ORDER BY Precio DESC
SELECT * FROM Productos WHERE Tamaño = 'Grande' ORDER BY Precio, Localidad DESC
```
- Tambien puede ir un el numero 3 que referencia a la tercer columna 
```sql
SELECT * FROM Productos WHERE Tamaño = 'Grande' ORDER BY 3 ASC
```
**CONSULTA VARIAS TABLAS**
```sql
SELECT Productos.*, Proveedores.* FROM Productos, Proveedores WHERE Provedores.Localidad = Producto.Localidad

SELECT Productos.*, Proveedores.* 
FROM Productos INNER JOIN Proveedores 
ON Proveedores.Localidad = Productos.Localidad;
```
**FUNCIONES DE AGREGADO - ORDER BY & HAVING**
- COUNT: Numero de valores en la columna
- SUM: La suma de los valores de la columa
- AVG: Promedio
- MIN: El minimo
- MAX: El maximo
```sql
Select COUNT(ID) FROM Productos
Select COUNT(ID) AS Total FROM Productos
```
Combinamos con **GROUP BY** para saber el total por grupo
```sql
SELECT Color, COUNT(*) FROM Productos GROUP BY Color
--Similar
SELECT Color, COUNT(DISTINCT Color) FROM Productos
```
Agregamos HAVING a GRUOP BY: es como un where pero solo se aplica a la agrapacion.
```sql
SELECT Color, COUNT(*) FROM Legajos GROUP BY Color HAVING COUNT(Color)>3
```

Combinamos con **WHERE** 
```sql
SELECT COUNT(*) FROM Productos WHERE Stock = 2
```
Combinamos WHERE con LIKE
Lo usamos para buscar paralbras o parte de ellas
```sql
--buscara nombres que comienzan el L
SELECT * FROM Productos WHERE Nombre LIKE 'L%'
--Buscara nombres que finalize con a
SELECT * FROM Productos WHERE Nombre LIKE '%a'
--Buscara fechas de febrero de 1992
SELECT * FROM Productos WHERE Fecha LIKE '__/02/1992'
```

**NOT LIKE**
```sql
--buscara nombres que no contenga e
SELECT * FROM Productos WHERE Nombre NOt LIKE '%e%'
```
CONSULTA DENTRO DE CONSULTA
```sql
SELECT * FROM Proveedores WHERE ID_Producto IN (SELECT ID FROM Productos)
--con inner join
SELECT Proveedores.* 
FROM Proveedores INNER JOIN Productos 
ON Proveedores.ID_Producto = Productos.ID;
```
**UNION**

Sirve para unir dos o mas tablas
- Las tablas deben tener la misma cantidad de **columnas**, **tipo** y **orden**

```sql
--La tabla2 se pondra abajo de la tabla1 ELIMINNANDO LAS REPETIDAS
SELECT * FROM Tabla1 UNION SELECT * FROM Tabla2
--Sin eliminacion de repetidas
SELECT * FROM Tabla1 UNION ALL SELECT * FROM Tabla2
```

**INNER JOIN**
```sql
SELECT Proveedores.*, Productos.*
FROM Proveedores INNER JOIN Productos 
ON Proveedores.ID_Producto = Productos.ID;
```
**LEFT JOIN**
```sql
SELECT Proveedores.*, Productos.*
FROM Proveedores INNER JOIN Productos 
ON Proveedores.ID_Producto = Productos.ID;
--Con WHERE
SELECT Proveedores.*, Productos.* FROM Proveedores, Productos WHERE Proveedores.ID_Producto(+) = Productos.ID;
```
**RIGTH JOIN**
```sql
SELECT Proveedores.*, Productos.*
FROM Proveedores INNER JOIN Productos 
ON Proveedores.ID_Producto = Productos.ID;
--Con WHERE
SELECT Proveedores.*, Productos.* FROM Proveedores, Productos WHERE Proveedores.ID_Producto = Productos.ID(+);
```
---
### UPDATE
```sql
Update Productos SET Tamaño = 'Chico' WHERE ID=12
Update Productos SET Tamaño = 'Chico', Precio = 0, Localidad = NULL WHERE ID=12
```
---
### DELETE
```sql
DELETE FROM Productos
DELETE FROM Productos WHERE ID= 1
```
**TRUNCATE**

- A diferencia del delete vacia la tabla pero reincia los ids
- Es **DLL** no se puede recuperar
```sql
TRUNCATE TABLE Productos
```
---
### INSERT

```sql
INSERT INTO Productos VALUES (NULL, 'Taza', 120,NULL)
INSERT INTO Productos(Nombre, Precio, Seccion) VALUES ('Taza', 120,NULL)
```
Inserciones masivas
- Se copiara todo el contenido de la tabla AuxProductos siempre y cuando respete la estructura de la tabla Productos

```sql
INSERT INTO Productos SELECT * FROM AuxProductos
```
---

**TRANSACTIONS COMMIT ROLLBACK**
  - **Transaction** es un area de prueba donde tiramos querys 
    - **Commit** hace que los cambios gerenerados sean permanenetes
        - Las sentencias de **DLL** hace un commit automatico
    - **Rollback** deshace todas las actualizaciones al ultimo estado previo commiteado o inicio de seccion.

---
---
### INDICES
Son estructuras de acceso que facilitan la agilizar la respuesta de una consulta en determinada columna que se repitan muchas veces
- Las columnas PRIMARY KEY tiene por defecto indice
```sql
CREATE INDEX I_Loc_Prov ON Proveedores(Localidad)
-- Compuesta 
CREATE INDEX I_PrecLoc_Prov ON Proveedores(Precio, Localidad)

-- Borrar index
DROP INDEX I_Loc_Prov 
```

### Vistas
Encapsula la visibilidad  para darle permisa a un usuario y tiene los datos acotados
```sql
CREATE VIEW V_Capital_Proveedores AS SELECT * FROM Proveedores WHERE Localidad='Capital'

-- Borrar index
DROP VIEW V_Capital_Proveedores

-- Alterar explicito
 CREATE OR REPLACE VIEW V_Capital_Proveedores AS SELECT * FROM Proveedores WHERE Localidad='Capital' AND Localidad='Matanza'
```

### CATALOGO
```sql
-- Dentro de information_schema
SELECT * FROM TABLES
SELECT * FROM COLUMS
SELECT * FROM INDEXS
```
```sql
SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA = 'comanda_db';
```
Cada usuario puede acceder a lo que le coresponda en cambio el dba tiene acceso a todo.<br>
Como nace el objeto de catalogo de System: Cuando instalo en motor, un script sql contiene el create view de cada uno de los objetos principales (systable, syscolum etc.)

### REGLAS DE INTEGRIDAD RELACIONAL
Protegen a las base de datos contra los daños accedentales
Son las **CONSTRAINS** 
- De PRIMARY KEY : Que sea unica y no sea nula
- FOREING KEY: Cuando la foreing key no existe en el padre
<br><br>


- NOT NULL
- PRIMARY KEY
- FOREING KEY
- UNIQUE: el valor es unica en la columna pero puede ir null
- CHECK

tambien pueden ser consultadas en el SYSTEM
<BR>
EL MOTOR LE PONE NOMBRE AUTOMATICAMENTE A ESTAS CONSTRINS 

- No se le puede colocar nombre a NULL

```sql
create TABLE CLIENTE(
	ID_CLIENTE INT NOT NULL,
    NOMBRE VARCHAR(30),
    TIPO_DOC VARCHAR(10),
    NRO_DOC INT,
    CUIT VARCHAR(25),
    -- valida que no se repita la combinacion entre tipo_doc y nro_doc
    CONSTRAINT uk_tipo_num_doc UNIQUE (TIPO_DOC, NRO_DOC),
    CONSTRAINT uk_cuit UNIQUE(CUIT)
)
```
Check constrain
```sql
create TABLE CLIENTE(
	Edad INT CONSTRAINT ck_edad CHECK(Edad>17 AND Edad<65),
  
  CONSTRAINT ck_est_civil CHECK
  (
    (est_civil in (‘CASADO’, ‘PAREJA’) AND dni_conyuge IS NOT NULL) 
    OR
    (est_civil in (‘SOLTERO’, ‘SEPARADO’, ‘VIUDO’) AND dni_conyuge IS NULL)
  );
)
```
Primary key
```sql
create TABLE CLIENTE(
	Id_Empleado INT,
  Id_Gerente INT,
  CONSTRAINT pk_id_empleado_id_gerente PRIMARY KEY(Id_Empleado, Id_Gerente)
)
```
forening key
```sql
create TABLE CLIENTE(
	Id_Empleado INT,
  Id_Gerente INT,
  CONSTRAINT gerente_fk_id_gerente FOREIGN KEY (Id_Gerente) REFERENCES GERENTES(Id)
) 
```
Alter
```sql
ALTER TABLE s_emp
ADD (CONSTRAINT s_emp_pk_id PRIMARY KEY (id),
CONSTRAINT s_emp_ck_salario CHECK (salario > 500));

ALTER TABLE tabla ENABLE CONSTRAINT nombre_constraint;
ALTER TABLE tabla DISABLE CONSTRAINT nombre_constraint;
```
Esta columna tiene que cumplir la conidicion para poder habilitar la constrain

26