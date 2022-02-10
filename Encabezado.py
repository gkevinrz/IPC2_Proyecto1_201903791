#Clase para los encabezados de la matriz

class NodoEncabezado():
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        self.primerNodo=None