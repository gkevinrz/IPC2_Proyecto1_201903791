from urllib.parse import _NetlocResultMixinBytes
from NodoPatron import NodoPatron
from matriz import Matriz

class ListaPatrones():
    def __init__(self):
        self.Inicio=None
        self.size=0
    def insertarPatron(self,codigo_patron,string_patron):
        nuevoPatron=NodoPatron(codigo_patron,string_patron)
        self.size+=1
        if self.Inicio is None:
            self.Inicio=nuevoPatron
            self.Inicio.Estado=True
        else:
            temp=self.Inicio
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevoPatron
            nuevoPatron.anterior=temp
    def getPatron(self,codigoPatron):
        temp=self.Inicio
        while temp is not None:
            if temp.codigo_patron==codigoPatron:
                return temp
            temp=temp.siguiente
        return None
    def mostrarPatrones(self):
        temp=self.Inicio
        print('  Patrones Disponibles ')
        print('|----------------------|')
        while temp is not None:
            if temp.Estado==False:
                print('Codigo: '+temp.codigo_patron +' Patron: '+temp.string_patron)
            else:
                print('Patron actual:', temp.string_patron)
            temp=temp.siguiente
