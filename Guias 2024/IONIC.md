- Insalación de Ionic
```
npm i -g @ionic/cli

ionic -v
```
- Crear un nuevo proyecto 

``` cmd
ionic start NombreArchivo blank     //vacio
ionic start NombreArchivo sidemenu  //Menu lateral
ionic start NombreArchivo tabs      //tambs en abajo

->Angular
->NgModule

```
- Iniciar el proyecto -> **Se debe estar posicionado el la carpeta del proyecto**

``` cmd
ionic serve

<!-- Ver IOS y Andriod en simultaneo-->
ionic serve --lab

<!-- DETENER -->
Ctrl+C
```
## Creación de una pagina
- Por lo general se agregan automaticamente en el app-routing-module
- Para crear una paguina usamos el comando:
```
ionic g page home

-->Definir la carpeta donde se crea la paguina
ionic g page pages/home 

--> Ver los archivos que se crea antes de ejecutar
ionic g page home --dry-run

-->Excluir los archivos de test 
ionic g page home --dry-run  --spect=false

```