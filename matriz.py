from re import A
from Encabezado import NodoEncabezado
from NodoPosicion import NodoPosicion
from ListaEncabezados import ListaEncabezado


class Matriz():
    def __init__(self):
        self.EncabezadoFilas=ListaEncabezado()
        self.EncabezadoColumnas=ListaEncabezado()


    def insertarAzulejo(self,fila,columna,estado):
        nuevo=NodoPosicion(fila,columna,estado)
    #-------------------------------------------
        nuevaFila=self.EncabezadoFilas.getEncabezado(fila)
        if nuevaFila ==None:
            nuevaFila=NodoEncabezado(fila)
            nuevaFila.primerNodo=nuevo
            self.EncabezadoFilas.insertarEncabezado(nuevaFila)
        else:
            if nuevo.Columna<nuevaFila.primerNodo.Columna:
                nuevo.derecha=nuevaFila.primerNodo
                nuevaFila.primerNodo.izquierda=nuevo
                nuevaFila.primeroNodo=nuevo
            else:
                actual=nuevaFila.primerNodo
                while actual.derecha!=None:
                    if nuevo.Columna<actual.derecha.Columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha
                if actual.derecha==None:
                    actual.derecha=nuevo
                    nuevo.izquierda=actual

    #.-----------------para columnas (manejo vertical)
        nuevaColumna=self.EncabezadoColumnas.getEncabezado(columna)
        if nuevaColumna==None:
            nuevaColumna=NodoEncabezado(columna)
            nuevaColumna.primerNodo=nuevo
            self.EncabezadoColumnas.insertarEncabezado(nuevaColumna)
        else:
            if nuevo.Fila<nuevaColumna.primerNodo.Fila:
                nuevo.abajo=nuevaColumna.primerNodo
                nuevaColumna.primerNodo.arriba=nuevo
                nuevaColumna.primerNodo=nuevo
            else:
                actual=nuevaColumna.primerNodo
                while actual.abajo!=None:
                    if nuevo.Fila<actual.abajo.Fila:
                        nuevo.abajo=actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba=actual
                        actual.abajo=nuevo
                        break
                    actual=actual.abajo
                if actual.abajo==None:
                    actual.abajo=nuevo
                    nuevo.arriba=actual

    def imprimirColumnas(self):
        tmp=self.EncabezadoColumnas.Primero
        while tmp!=None:
            nodoacceso=tmp.primerNodo
            while(nodoacceso is not None):
                print('[(',nodoacceso.Fila,',',nodoacceso.Columna,')]',nodoacceso.Estado)    
                nodoacceso=nodoacceso.abajo
            tmp=tmp.next   
    def imprimirFilas(self):
        tmp=self.EncabezadoFilas.Primero
        while tmp is not None:
            nodoAcceso=tmp.primerNodo
            while(nodoAcceso is not None):
                print('[(',nodoAcceso.Fila,',',nodoAcceso.Columna,')]',nodoAcceso.Estado)
                nodoAcceso=nodoAcceso.derecha
            tmp=tmp.next    
    def getNodo(self,fila,columna):
        tmp=self.EncabezadoFilas.Primero
        while tmp is not None:
            nodoTmp=tmp.primerNodo
            while nodoTmp is not None:
                if(nodoTmp.Fila==fila and nodoTmp.Columna ==columna):
                    return nodoTmp
                nodoTmp=nodoTmp.derecha
            tmp=tmp.next
        return None





