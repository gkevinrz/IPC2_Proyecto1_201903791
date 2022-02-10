from lib2to3.pgen2.token import OP
from tkinter.tix import MAIN
import xml.etree.ElementTree as ET

class Main():
    def __ininit__(self):
        pass
    def Menu(self):
        Opcion=''
        while Opcion!='6':
            print(' ___________________________________________________')
            print('|-------------- Pisos Artesanales S.A. -------------|')
            print('|        1. Cargar archivo                          |')
            print('|        2. Elegir piso                             |')
            print('|        3. Graficar patrón inicial                 |')
            print('|        4. Seleccionar nuevo patrón y procesar     |')
            print('|        5. Graficar nuevo patrón                   |')
            print('|        6. Salir                                   |')
            print('|---------------------------------------------------|')
            Opcion=input('Seleccione una opción:\n> ')
            if Opcion=='1':
                ruta_archivo=input('Ruta del Archivo: \n > ')
                self.CargarArchivo(ruta_archivo)


    def CargarArchivo(self,ruta):
        tree=ET.parse(ruta)
        root=tree.getroot()
        print('')
        print(root)





prin=Main()
prin.Menu()