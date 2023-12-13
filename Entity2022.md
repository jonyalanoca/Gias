### MODELOS
``` c#
public partial class Pais
{
    public Pais()
    {
        Ciudad= new List<Ciudad>();
    }
    public int IdPais { get; set; }

    public string Nombre { get; set; } = null!;

    public virtual ICollection<Ciudad> Ciudad { get; set; }     //PAIS ES REFERENCIADO
}
public partial class Capital
{
    public Capital()
    {
        Ciudad = new List<Ciudad>();
    }
    public int IdCapital { get; set; }

    public string? Nombre { get; set; }                         //STRING QUE APCETA NULL

    public virtual ICollection<Ciudad> Ciudad { get; set; }     //CAPITAL ES REFERENCIADO
}
public partial class Ciudad
{
    public int IdCiudad { get; set; }

    public string Nombre { get; set; } = null!;                 //STRING QUE NO APCETA NULL

    public int IdPais { get; set; }

    public int? IdCapital { get; set; }

    public virtual Capital? IdCapitalNavigation { get; set; }    //REFERENCIA QUE ACEPTA NULL

    public virtual Pais IdPaisNavigation { get; set; } = null!; //REFERENICIA QUE NO ACEPTA NULL
}
```
### ENTITIES
``` c#
modelBuilder.Entity<Ciudad>(entity =>
{
    entity.HasKey(e => e.IdCiudad).HasName("PK__Ciudad__D4D3CCB01ED1CDF2");

    entity.ToTable("Ciudad");

    entity.Property(e => e.Nombre)
        .HasMaxLength(250)
        .IsUnicode(false);

    entity.HasOne(d => d.IdCapitalNavigation)       //Variable referecial   Ciudad.IdCapitalNavigation
        .WithMany(p => p.Ciudad)                    //ICollection           Capital.Ciudad
        .HasForeignKey(d => d.IdCapital)            //Variable              Ciudad.IdCapital
        .HasConstraintName("FK_Ciudad_Capital");

    entity.HasOne(d => d.IdPaisNavigation)          //Variable referecial   Ciudad.IdPaisNavigation
        .WithMany(p => p.Ciudad)                    //ICollection           Pais.Ciudad
        .HasForeignKey(d => d.IdPais)               //Variable              Ciudad.IdPais
        .OnDelete(DeleteBehavior.ClientSetNull)     //OBLIGATORIO SI ES  NOT NULL
        .HasConstraintName("FK_Ciudad_Pais");       //CONSTRAINT
});
```
<hr>

# DobleReferencia UsuarioALta UsuarioModificacion

### MODELOS
``` c#
public partial class Usuario
{
    public int IdUsuario { get; set; }

    public string Nombre { get; set; } = null!;

    public virtual ICollection<Feriado> FeriadoIdUsuarioAltaNavigations { get; set; } = new List<Feriado>();

    public virtual ICollection<Feriado> FeriadoIdUsuarioModificacionNavigations { get; set; } = new List<Feriado>();
}
public partial class Feriado
{
    public int IdFeriado { get; set; }

    public string Motivo { get; set; } = null!;

    public int IdUsuarioAlta { get; set; }

    public int? IdUsuarioModificacion { get; set; }

    public virtual Usuario IdUsuarioAltaNavigation { get; set; } = null!;

    public virtual Usuario? IdUsuarioModificacionNavigation { get; set; }
}
```
### ENTITIES

``` c#
modelBuilder.Entity<Feriado>(entity =>
{
    entity.HasKey(e => e.IdFeriado)
        .HasName("PK_Feriado_IdFeriado");

    entity.ToTable("Feriado");

    entity.Property(e => e.Motivo)
        .HasMaxLength(250)
        .IsUnicode(false);

    entity.HasOne(d => d.IdUsuarioAltaNavigation)           //Var           Feriado.IdUsuarioAltaNavigation
        .WithMany(p => p.FeriadoUsuarioAlta)                //ICollection   Usuario.FeriadoUsuarioAlta
        .HasForeignKey(d => d.IdUsuarioAlta)                //Var           Feriado.IdUsuarioAlta
        .OnDelete(DeleteBehavior.ClientSetNull)             //---NOT NULL---
        .HasConstraintName("FK_Feriado_UsuarioAlta");       //Constraint

    entity.HasOne(d => d.IdUsuarioModificacionNavigation)   //Var           Feriado.IdUsuarioAltaNavigation
        .WithMany(p => p.FeriadoUsuarioModificacion)        //ICollection   Usuario.FeriadoUsuarioAlta
        .HasForeignKey(d => d.IdUsuarioModificacion)        //Var           Feriado.IdUsuarioAlta
        .HasConstraintName("FK_Feriado_Modificacion");      //Constraint
});
```
