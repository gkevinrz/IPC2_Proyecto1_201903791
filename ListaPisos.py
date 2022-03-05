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

    def ord(self):
        if self.size > 1:
            while True:
                actual = self.Inicio
                i = None  # anterior
                j = self.Inicio.siguiente  # siguiente
                cambio = False
                while j != None:
                    if actual.nombre > j.nombre:
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