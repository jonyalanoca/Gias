
### Activar estadisticas
```sql
set statistics time, io on
```
### Obligar a sql que trabaje en un solo Core sin paralelismo

```sql
...
option(maxdop 1)
```
### Obligar excluir el cache almacenado

```sql
...
OPTION (RECOMPILE); 
```
