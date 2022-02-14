class Ventas:
    def __init__(self, _id,clien, fech, subtotal2,IVA, total, listaven):
        self._id= int(_id)
        self.clien = int(clien)
        self.fech = str(fech)
        self.IVA = float(IVA)
        self.total = float(total)
        self.subtotal2 = float(subtotal2)
        self.listaven = list(listaven) 
        

