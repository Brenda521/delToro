class Detalle_de_Venta:
    def __init__ (self,id_art,cant,total,id_venta, arcant,iva, subtotal):
        self.id_art=int(id_art)
        self.cant=int(cant)
        self.total=float(total)
        self.id_venta=int(id_venta)
        self.arcant=float(arcant)
        self.iva = float(iva)
        self.subtotal = float(subtotal)
        

