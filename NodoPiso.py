from stat import FILE_ATTRIBUTE_SYSTEM

from ListaPatrones import ListaPatrones
from matriz import Matriz


class NodoPiso():
    def __init__(self,nombre,filas,columnas,costo_voltear,costo_cambiar):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.costo_voltear=costo_voltear
        self.costo_cambiar=costo_cambiar
        self.ListaPatrones=ListaPatrones()
        self.Matriz=Matriz()
        self.siguiente=None