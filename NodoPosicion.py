#0 blanco 
#1 negro
class NodoPosicion():
    def __init__(self,fila,columna,estado):
        self.Fila=fila
        self.Columna=columna
        self.Estado=estado
        self.derecha=None
        self.izquierda=None
        self.arriba=None
        self.abajo=None
