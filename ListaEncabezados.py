
class ListaEncabezado():
    def __init__(self,primero=None):
        self.Primero=primero
    
    def insertarEncabezado(self,nuevo):
        if self.Primero==None:
            self.Primero=nuevo
        elif nuevo.id <self.Primero.id:
            nuevo.next=self.Primero
            self.Primero.prev=nuevo
            self.Primero=nuevo
        else:
            actual=self.Primero
            while actual.next!=None:
                if nuevo.id<actual.next.id:
                    nuevo.next=actual.next
                    actual.next.prev=nuevo
                    nuevo.prev=actual
                    actual.next=nuevo
                    break
                actual=actual.next
            if actual.next==None:
                actual.next=nuevo
                nuevo.prev=actual

    

    def getEncabezado(self,id):
        actual=self.Primero
        while actual!=None:
            if actual.id==id:
                return actual
            actual=actual.next
        return None
