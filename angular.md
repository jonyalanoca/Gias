## Angular

Crear un nuevo proyecto de angular

```
ng new NombreProyecto
ng new NombreProyecto --skip-tests

<!-- En caso que no aparezca el app.module -->
ng new NombreProyecto --standalone=false
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
**Verificar que se agrego en app.module.ts en NgModule -> declaratios**
<br>
o
<br>
Podemos ver que es lo que va a modificar o crear antes de que lo haga en la consola
```
ng g  c pages/contact --dry-run
```

## Bindeos

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
## Directivas

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

## Redireccionamientos
Para redireccionar desde el html sin recargar la paguina
``` html
<a routerLink="/home">Home</a>
```
DESDE EL CODIGO
- Importa el módulo Router de @angular/router en tu componente ComponenteOrigen.
```typescript
import { Router } from '@angular/router';
```
- Inyecta el servicio Router en el constructor de tu componente. Y creacion del la función
```typescript
constructor(private router: Router) { }

redireccionarAComponenteDestino() {
  this.router.navigate(['/home']);
}
```
## Enrutamiento
Queremos usar los componentes como paguinas necesitamso un archivo de enrutamiento `app-routing.module.ts` este sera el principal 
- A la altura de nuestro app.module.ts crear este archivo
```
ng g m app-routing --flat 
```
- Inicialmente tendremos algo asi
```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { ContactComponent } from './pages/contact/contact.component';

//RUTAS
const routes: Routes = [
{path:'home', component:HomeComponent},
{path:'about',component:AboutComponent},
{path:'contact',component:ContactComponent},

// Inidicamos un DEFAULT por si se ingresa mal alguna ruta
{path:'**',redirectTo:'home'}

];

//INPORTANTE 
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule] //TAMBIEN HAY QUE INCLUIR EN EL app-module
})

export class AppRoutingModule { }
```
- Incluir en el `app-module.ts`
``` typescript
import { AppRoutingModule } from './app-routing.module';
...
imports: [
  BrowserModule,
  AppRoutingModule //Se inlcuye aca
],
```
- En el `app.component.html` se debe incluir
```html
<router-outlet></router-outlet>
```

## Division de Modulos
- Para mantener limpio nuestro `app.module.ts` se hace la division de modulo
  - ponemos nuestros componentes en una carpeta que caracteriza a estos componentes Ej: reportes
  - creamos en modulo dentro de esta carpeta
  ``` cmd
    ng g m Reportes
    <!-- Se crea un modulo dentro de la carpeta reportes con nombre reportes.module.ts -->

    <!-- Evitar que se  cree una carpeta nueva, se crea el modulo en la ruta que indica -->
    ng g m app-routing --flat 
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
  
## LazyLoad
Todo este modulo sera cargado en carga peresoza y cuando sea necesario

- Creamos un nuevo modulo y routing (Hijo)
```
 ng g m pages/posts --routing
```
- Creamos un nuevo componente para hacerlo LazyLoading
```
 ng g c pages/posts
```
