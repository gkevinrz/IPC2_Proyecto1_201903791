#Clase para los encabezados de la matriz

class NodoEncabezado():
    def __init__(self,id):
        self.id=id
        self.next=None
        self.prev=None
        self.primerNodo=None