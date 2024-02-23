
```c#
//Left Join con empresarioLocalidad
join empresarioLocalidad in tEmpresarioLocalidad on localidad.IdLocalidad equals empresarioLocalidad.IdLocalidadCanalizadora
     into _empresarioLoc
from empresarioLocalidad in _empresarioLoc.DefaultIfEmpty()
```
