
´´´c#
var consulta =
    from rg in dbContext.RendicionGuia
    join r in dbContext.Rendicion on new { rg.IdRendicion, IsNotEmpresarioNull = r.IdEmpresario != null } equals new { r.IdRendicion, IsNotEmpresarioNull = true }
    join g in dbContext.Guia on rg.IdGuia equals g.IdGuia
    join sc in dbContext.SubCuenta on g.IdSubCuenta equals sc.IdSubCuenta
    join c in dbContext.Cuenta on sc.IdCuenta equals c.IdCuenta
    join cl in dbContext.Cliente on c.IdCliente equals cl.IdCliente
    join e in dbContext.Empresario on r.IdEmpresario equals e.IdEmpresario
    join rt in dbContext.RendicionTipo on r.IdRendicionTipo equals rt.IdRendicionTipo
    join gr in dbContext.GuiaReclamo on new { g.IdGuia, Observaciones = "%SIN CONFORMAR RENDICION DE OPERADOR%" } equals new { gr.IdGuia, gr.Observaciones }
        into grGroup
        from gr in grGroup.DefaultIfEmpty()
    where (idEmpresario == null || r.IdEmpresario == idEmpresario)
        && !(
            from e in dbContext.Evento
            join ec in dbContext.EventoCodigo on e.IdEventoCodigo equals ec.IdEventoCodigo
            where e.IdGuia == g.IdGuia && new[] { 15, 37, 70, 52 }.Contains(ec.Codigo)
            select 1
        ).Any()
        && g.Anulada == 0
        && rt.Codigo == 100
    select new
    {
        FechaEmision = g.FechaEmision,
        FechaRendicion = r.Fecha,
        NumeroGuia = g.Numero,
        NumeroRendicion = r.Numero,
        cl.RazonSocial,
        FechaInicioReclamo = gr.Fecha,
        r.IdEmpresario,
        Empresario = e.RazonSocial
    };

// Ejecutar la consulta y obtener los resultados
var resultados = consulta.ToList();
´´´









pdf en c#
https://products.fileformat.com/es/pdf/net/itext/
