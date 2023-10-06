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
- Importante: hay que importar el **FormsModule** en el module
- por lo general se usa en inputs
``` html
<input type="text"  [(ngModel)]="apellido" placeholder="Ingrese apellido">
<h1>{{apellido}}</h1>
```
### Directivas

Asegurarse que se importa **CommonModule**

**NGIF**
Muestra u oculta un elemento si recibe un true o false

``` html
<button *ngIf="nombre=='Juan'" (click)="accion()">Borrar ultimo heroe</button>
<button *ngIf="isEmpty()" (click)="accion()">Borrar ultimo heroe</button>
<button *ngIf="1+1==2" (click)="accion()">Borrar ultimo heroe</button>
```
Tambien existe el **ngif-else** con la particularidad que los **ng-Templates** no se crean en el html hasta no recibir un **else**
``` html
<p *ngIf="nombre=='Juan'; else tagName">Text</p>
<ng-template #tagName>
    <p>Text Else</p>
</ng-template>
```

**NGFOR** repite un elemento segun la condicion
``` html
<p *ngFor="let item of listaHeroe"> {{item}}</p>
<p *ngFor="let item of listaHeroe"> {{item.Nombre}}</p>
```

### Division de Modulos
  - ponemos nuestros componentes en una carpeta que caracteriza a estos componentes Ej: reportes
  - creamos en modulo dentro de esta carpeta
  ``` cmd
    ng g m Reportes
    <!-- Se crea un modulo dentro de la carpeta reportes con nombre reportes.module.ts -->
  ```
  -Nuestro nuevo Module de verse de esta forma
  ``` typescript
    @NgModule({
    declarations: [
        HeroeComponent,
        ListComponent,
    ],
    imports: [
        CCommonModule,
        FormsModule
    ],
    exports:[
        HeroeComponent,
        ListComponent,
    ]
    })
    export class HeroesModule { }
  ```
  - nos aseguramos que tiene las importaciones y exportaciones correctas
  - En el modulo padre borramos los imports que ya no usamos y declarations 
  - En el modulo padre agregamos nuestro nuevo Modulo en imports
  - IMPORTANTE: este modulo encapsula a los componentes y se limita el su alcance
    
