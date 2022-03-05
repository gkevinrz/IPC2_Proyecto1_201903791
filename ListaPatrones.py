from argparse import Action
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
                print('Codigo: '+temp.codigo_patron +' Patron actual: '+temp.string_patron)
            temp=temp.siguiente

        #self.ordenar()
    def ordenar(self):
        if self.size > 1:
            while True:
                actual = self.Inicio
                i = None  # anterior
                j = self.Inicio.siguiente  # siguiente
                cambio = False
                while j != None:
                    if actual.codigo_patron > j.codigo_patron:
                        cambio = True
                        if i != None:
                            tmp = j.siguiente
                            i.siguiente = j
                            j.siguiente = actual
                            actual.siguiente = tmp
                        else:
                            tmp2 = j.siguiente
                            self.Inicio = j
                            j.siguiente = actual
                            actual.siguiente = tmp2
                        i = j
                        j = actual.siguiente
                    else:
                        i = actual
                        actual = j
                        j = j.siguiente
                if not cambio:
                    break
