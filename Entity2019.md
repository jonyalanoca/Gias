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
                .HasMaxLength(250)
                .IsUnicode(false);

            entity.HasOne(d => d.IdCapitalNavigation)       //Variable referecial   Ciudad.IdCapitalNavigation
                .WithMany(p => p.Ciudad)                    //ICollection           Capital.Ciudad
                .HasForeignKey(d => d.IdCapital)            //Variable              Ciudad.IdCapital
                .HasConstraintName("FK_Ciudad_Capital");

            entity.HasOne(d => d.IdPaisNavigation)          //Variable referecial   Ciudad.IdPaisNavigation
                .WithMany(p => p.Ciudad)                    //ICollection           Pais.Ciudad
                .HasForeignKey(d => d.IdPais)               //Variable              Ciudad.IdPais
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_Ciudad_Pais");       //CONSTRAINT
        });


        modelBuilder.Entity<Ciudad>(entity =>
        {
            entity.HasKey(e => e.IdCiudad)
                .HasName("PK__Ciudad__D4D3CCB01ED1CDF2");

            entity.ToTable("Ciudad");

            entity.Property(e => e.Nombre)
                .IsRequired()
                .HasMaxLength(250)
                .IsUnicode(false);

            entity.HasOne(d => d.IdCapitalNavigation)
                .WithMany(p => p.Ciudad)
                .HasForeignKey(d => d.IdCapital)
                .HasConstraintName("FK_Ciudad_Capital");

            entity.HasOne(d => d.IdPaisNavigation)
                .WithMany(p => p.Ciudad)
                .HasForeignKey(d => d.IdPais)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_Ciudad_Pais");
        });

```