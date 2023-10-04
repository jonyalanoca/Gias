## Angular

Crear un nuevo proyecto de angular

```
ng new NombreProyecto
```
Inicializar proyecto (desde la raiz del proyecto)
```
ng serve
ng serve -o
```
Agregar un nuevo componente(desde la raiz del proyecto)
```
ng generate component NuevoComponente
ng g n components/nuevoComponente
```
Verificar que se agrego en app.module.ts en NgModule -> declaratios

### Bindeos

**Interpolacion**: Permite poner cualquier expresion js, podemos poner **Variables** y **Metodos**
``` html
<p>{{ name }}</p>
<p>{{ descripcion() }}</p>
```
**Bindeo de la propiedad**: Le damos valor a las etiquetas desde un atributo
``` html
<img [src]="imagenUrl">
<input type="button" [value]="nameButton">
```
**Bindeo de evento**: Cada vez que haga click llamara a al metodo ej: Onclick
``` html
<input type="button" [value]="nameButton" (click)="Onclick()">
<button (click)="Onclick()">{{nameButton}}</button>
```

**Bindeo bidireccional**: el imput y la variable estan sincronizado
- Importante: hay que añadir el FormsModule en app.module
- por lo general se usa en inputs
``` html
<input type="text"  [(ngModel)]="apellido" placeholder="Ingrese apellido">
<h1>{{apellido}}</h1>
```
### Directivas

