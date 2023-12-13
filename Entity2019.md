### MODELOS
``` c#
public partial class Pais
{
    public Pais()
    {
        Ciudad = new HashSet<Ciudad>();
    }
    public int IdPais { get; set; }
    public string Nombre { get; set; }
    public virtual ICollection<Ciudad> Ciudad { get; set; }     //Es referenciado
}
public partial class Capital
{
    public Capital()
    {
        Ciudad = new HashSet<Ciudad>();
    }
    public int IdCapital { get; set; }
    public string Nombre { get; set; }
    public virtual ICollection<Ciudad> Ciudad { get; set; }     //Es referenciado
}
public partial class Ciudad
{
    public int IdCiudad { get; set; }
    public string Nombre { get; set; }                          //Admiten automaticamete null en .net5
    public int IdPais { get; set; }
    public int? IdCapital { get; set; }                         //Admite null
    public virtual Capital IdCapitalNavigation { get; set; }    //referencia a idCapital
    public virtual Pais IdPaisNavigation { get; set; }          //referencia a idPais
}
```
### ENTITIES
``` c#
modelBuilder.Entity<Ciudad>(entity =>
{
    entity.HasKey(e => e.IdCiudad).HasName("PK__Ciudad__D4D3CCB01ED1CDF2");

    entity.ToTable("Ciudad");

    entity.Property(e => e.Nombre)
        .IsRequired()                               //--NOT NULL en DB--
        .HasMaxLength(250)
        .IsUnicode(false);

    entity.HasOne(d => d.IdCapitalNavigation)       //Variable referecial   Ciudad.IdCapitalNavigation
        .WithMany(p => p.Ciudad)                    //ICollection           Capital.Ciudad
        .HasForeignKey(d => d.IdCapital)            //Variable              Ciudad.IdCapital
        .HasConstraintName("FK_Ciudad_Capital");

    entity.HasOne(d => d.IdPaisNavigation)          //Variable referecial   Ciudad.IdPaisNavigation
        .WithMany(p => p.Ciudad)                    //ICollection           Pais.Ciudad
        .HasForeignKey(d => d.IdPais)               //Variable              Ciudad.IdPais
        .OnDelete(DeleteBehavior.ClientSetNull)     //----NOT NULL------
        .HasConstraintName("FK_Ciudad_Pais");       //CONSTRAINT
});
```

<hr>

# DobleReferencia UsuarioALta UsuarioModificacion

### MODELOS
``` c#
public partial class Usuario
{
    public Usuario()
    {
        FeriadoUsuarioAlta = new HashSet<Feriado>();
        FeriadoUsuarioModificacion = new HashSet<Feriado>();
    }
    public int IdUsuario { get; set; }
    public string Nombre { get; set; }

    public virtual ICollection<Feriado> FeriadoUsuarioAlta { get; set; }
    public virtual ICollection<Feriado> FeriadoUsuarioModificacion { get; set; }
}
public partial class Feriado
    {
        public int IdFeriado { get; set; }
        public string Motivo { get; set; }
        public int IdUsuarioAlta { get; set; }
        public int? IdUsuarioModificacion { get; set; }

        public virtual Usuario IdUsuarioAltaNavigation { get; set; }
        public virtual Usuario IdUsuarioModificacionNavigation { get; set; }
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
        .IsRequired()                                       //--NOT null en db
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
