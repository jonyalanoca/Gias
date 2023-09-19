Relaciones

~~~c#
public int Id { get; set; }
public string Nombre { get; set; }
public string Descripcion { get; set; }
public string FechaCreacion { get; set; }
public string UrlImagen { get; set; }
// Entity automaticamente buscara el Modelo Categoria luego Id
public int CategoriaId { get; set; }
// Esto es obligatorio para una relacion 1 a 1
public Categoria Categoria { get; set; }
~~~

Si el Modelo tiene esto
~~~c#
public int IdEstudiante { get; set; }

public string? Nombre { get; set; }

public int? Legajo { get; set; }
// Significa que este modelo tiene esta relacionada en otro Modelo 
public virtual ICollection<Relacion2> Relacion2s { get; set; } = new List<Relacion2>();
~~~