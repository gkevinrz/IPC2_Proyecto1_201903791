from NodoPiso import NodoPiso

class ListaPisos():
    def __init__(self):
        self.Inicio=None
        self.size=0

    def insertarPiso(self,nombre,filas,columnas,costo_voltear,costo_cambiar):
        nuevoPiso=NodoPiso(nombre,filas,columnas,costo_voltear,costo_cambiar)
        self.size+=1
        if self.Inicio is None:
            self.Inicio=nuevoPiso
        else:
            temp=self.Inicio
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevoPiso

    def getPiso(self,nombreTerreno):
        temp=self.Inicio
        while temp is not None:
            if temp.nombre==nombreTerreno:
                return temp
            temp=temp.siguiente
        return None



    def mostrarPisos(self):

        temp=self.Inicio
        print('  Pisos Disponibles  ')
        print('|--------------------|')
        while temp is not None:
            print('Nombre: ',temp.nombre)
            temp=temp.siguiente
        print('')