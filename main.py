from cgitb import text
from lib2to3.pgen2.token import OP
from os import stat
from pickletools import OpcodeInfo
from tkinter.tix import MAIN
import xml.etree.ElementTree as ET
from NodoPiso import NodoPiso
from ListaPisos import ListaPisos
from os import system,startfile
#from ListaPatrones import ListaPatrones
class Main():
    def __init__(self):
        self.ListaPisos=ListaPisos()
        #self.ListaPatrones=ListaPatrones()
        
    def Menu(self):
        Opcion=''
        OpcionPiso=''
        OpcionPatron=''
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
            elif Opcion=='2':
                self.ListaPisos.ord()
                self.ListaPisos.mostrarPisos()
                OpcionPiso=input('Escriba el nombre del piso: \n > ')
                print('\nPiso '+OpcionPiso+' seleccionado')
            elif Opcion=='3':
                pisoelegidograf=self.ListaPisos.getPiso(OpcionPiso)
                self.graficar_inicial(pisoelegidograf)
            elif Opcion=='4':
                pisoelegido=self.ListaPisos.getPiso(OpcionPiso)
                #pisoelegido.Matriz.imprimirColumnas()
                #print('--------------------------------')
                #pisoelegido.Matriz.imprimirFilas()
                #pisoelegido.ListaPatrones.mostrarPatrones()
                pisoelegido.ListaPatrones.ordenar()
                pisoelegido.ListaPatrones.mostrarPatrones()
                OpcionPatron=input('Escriba el código del patrón nuevo:\n> ')
                patronelegido=pisoelegido.ListaPatrones.getPatron(OpcionPatron)
                self.Procesar(pisoelegido,patronelegido)
            elif Opcion=='5':
                pisoelegidograf=self.ListaPisos.getPiso(OpcionPiso)
                self.graficar_final(pisoelegidograf,patronelegido)
                


    def CargarArchivo(self,ruta):
        tree = ET.parse(ruta)
        root=tree.getroot()
        print('')
        #nombre_piso=''
        filas=0
        columnas=0
        precio_voltear=0
        precio_deslizar=0
        #print(root)
        for elemento in root:
            for f in elemento.iter('R'):
                    filas=int(f.text)
            for c in elemento.iter('C'):
                    columnas=int(c.text)
            for s in elemento.iter('S'):
                    precio_deslizar=int(s.text)
            for fq in elemento.iter('F'):
                    precio_voltear=int(fq.text)
            self.ListaPisos.insertarPiso(elemento.attrib['nombre'],filas,columnas,precio_voltear,precio_deslizar)
            #self.ListaPisos.insertarPiso(elemento.attrib['nombre'],filas,columnas,precio_voltear,precio_deslizar)
            pisotemp=self.ListaPisos.getPiso(elemento.attrib['nombre'])
            for patrones in elemento.iter('patrones'):
                for patron in patrones.iter('patron'):
                    pisotemp.ListaPatrones.insertarPatron(patron.attrib['codigo'],patron.text)
            patronIn=pisotemp.ListaPatrones.Inicio
            #print(patronIn.string_patron)
            s=str(patronIn.string_patron)
            #print(s)
            a=1
            #print(s[0])
            for i in range(filas):
                for j in range(columnas):
                    if s[a]=='B':
                        #print(patronIn.string_patron[a])
                        pisotemp.Matriz.insertarAzulejo(i,j,1)
                    else:
                        #print(patronIn.string_patron[a])
                        pisotemp.Matriz.insertarAzulejo(i,j,0)
                    a=a+1
        
        print('Pisos agregados correctamente')
    


    def Procesar(self,pisoelegido,patronnuevo):
        pisoElegido=pisoelegido
        pisoElegido.ListaPatrones.Inicio.Estado=False
        nuevoPatron=patronnuevo
        x=1
        log=''
        costo=0
        ac=0
        for i in range(pisoElegido.filas):
            for j in range(pisoElegido.columnas):
                if pisoElegido.Matriz.getNodo(i,j).Estado==0 and nuevoPatron.string_patron[x]=='W':
                    #print(pisoElegido.Matriz.getNodo(i,j).Estado)
                   #print(nuevoPatron.string_patron[x])
                    log+="""No hay movimiento en la casilla actual\n"""
                    
                elif pisoElegido.Matriz.getNodo(i,j).Estado==1 and nuevoPatron.string_patron[x]=='B': 
                    #print(nuevoPatron.string_patron[x])           
                    log+="""No hay movimiento en la casilla actual\n"""
                elif pisoElegido.Matriz.getNodo(i,j).Estado==0 and nuevoPatron.string_patron[x]=='B':
                    if pisoElegido.costo_voltear<pisoelegido.costo_cambiar:
                        costo=costo+pisoElegido.costo_voltear
                        log+=f"""Se volteó la casilla actual ({i,j})\n"""
                        pisoElegido.Matriz.getNodo(i,j).Estado=1
                    elif pisoElegido.costo_cambiar<pisoElegido.costo_voltear:
                        
                        if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j) is not None:
                            if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la derecha ({i,j+1})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0 and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                             
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            
                        else:
                            if pisoElegido.Matriz.getNodo(i+1,j) is None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                print('estoy aqui2')
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de la derecha ({i,j+1})\n"""
                         
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and  pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i+1,).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i+1,j) is None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""    
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is None:
                                costo=costo+pisoElegido.costo_voltear
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                #print('s')
                    elif pisoElegido.costo_voltear==pisoelegido.costo_cambiar:
                        if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j) is not None:
                            if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la derecha ({i,j+1})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0 and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                             
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                        else:
                            if pisoElegido.Matriz.getNodo(i+1,j) is None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                print('estoy aqui2')
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de la derecha ({i,j+1})\n"""
                         
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and  pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=0
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i+1,j) is None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=1
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""    
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is None:
                                costo=costo+pisoElegido.costo_voltear
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                                pisoElegido.Matriz.getNodo(i,j).Estado=1



                elif pisoElegido.Matriz.getNodo(i,j).Estado==1 and nuevoPatron.string_patron[x]=='W':
                    if pisoElegido.costo_voltear<pisoElegido.costo_cambiar:
                        costo=costo+pisoElegido.costo_voltear
                        log+=f"""Se volteó la casilla actual ({i,j})\n"""
                        pisoElegido.Matriz.getNodo(i,j).Estado=0
                    elif pisoElegido.costo_cambiar<pisoElegido.costo_voltear:
                        if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j) is not None:
                            if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la derecha ({i,j+1})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1 and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                        else:
                            if pisoElegido.Matriz.getNodo(i+1,j) is None  and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de la derecha ({i,j+1})\n"""
                         
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""


                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i+1,j) is None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is None:
                                costo=costo+pisoElegido.costo_voltear
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                    elif pisoElegido.costo_voltear==pisoelegido.costo_cambiar:
                        if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j) is not None:
                            if pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la derecha ({i,j+1})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""
                                x=x+1
                                continue
                            elif pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1 and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""

                        else:
                            if pisoElegido.Matriz.getNodo(i+1,j) is None  and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i,j+1).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de la derecha ({i,j+1})\n"""
                         
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==0:
                                costo=costo+pisoElegido.costo_cambiar
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                pisoElegido.Matriz.getNodo(i+1,j).Estado=1
                                log+=f"""Se cambió la casilla actual ({i,j}) a la casilla de abajo ({i+1,j})\n"""


                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is not None and pisoElegido.Matriz.getNodo(i+1,j).Estado==1:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i+1,j) is None and pisoElegido.Matriz.getNodo(i,j+1) is not None and pisoElegido.Matriz.getNodo(i,j+1).Estado==1:
                                costo=costo+pisoElegido.costo_voltear
                                pisoElegido.Matriz.getNodo(i,j).Estado=0
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                            elif pisoElegido.Matriz.getNodo(i,j+1) is None and pisoElegido.Matriz.getNodo(i+1,j) is None:
                                costo=costo+pisoElegido.costo_voltear
                                log+=f"""Se volteó la casilla actual ({i,j})\n"""
                                pisoElegido.Matriz.getNodo(i,j).Estado=0     

                x=x+1
                #pisoElegido.Matriz.getNodo(i,j)
        nuevoPatron.Estado=True
        
        log+=f"""\nCosto Mínimo: {costo}"""
        f = open (f'Log_{pisoElegido.nombre}.txt','w',encoding='utf-8')
        f.write(log)
        f.close()
       


    def graficar_inicial(self,piso):
        pisograf=piso
        texto="""
        digraph {"""
        texto+=f"""
        label="Nombre: {piso.nombre}"
        fontname="Arial"
        bgcolor="#f7f9f9"
        tbl [
        shape=plaintext
        label=<"""

        texto+="""
        <table color='black' border='0' cellborder='1' cellpadding='13' cellspacing='2'>
        """
        for i in range(pisograf.filas):
            texto+="""<tr>"""
            for j in range(pisograf.columnas):
                if pisograf.Matriz.getNodo(i,j).Estado==1:
                    texto+=f"""
                    <td bgcolor='black'></td>
                    """
                else:
                    texto+="""<td bgcolor='white'></td>"""
            texto+="""</tr>"""
    
        texto+="""
        </table>
        >];
        }
        """
        txt=texto
        miarchivo=open('PatronInicial.dot','w')
        miarchivo.write(txt)
        miarchivo.close()
        system('dot -Tpng PatronInicial.dot -o PatronInicial.png')
        system('cd ./PatronInicial.png')
        startfile('PatronInicial.png')
    
    def graficar_final(self,piso,s):
        pisograf=piso
        texto="""
        digraph {"""
        texto+=f"""
        label="Nombre: {piso.nombre}\n\n Patron: {s.string_patron}"
        fontname="Arial"
        bgcolor="#f7f9f9"
        tbl [
        shape=plaintext
        label=<"""

        texto+="""
        <table color='black' border='0' cellborder='1' cellpadding='13' cellspacing='2'>
        """
        for i in range(pisograf.filas):
            texto+="""<tr>"""
            for j in range(pisograf.columnas):
                if pisograf.Matriz.getNodo(i,j).Estado==1:
                    texto+=f"""
                    <td bgcolor='black'></td>
                    """
                else:
                    texto+="""<td bgcolor='white'></td>"""
            texto+="""</tr>"""
    
        texto+="""
        </table>
        >];
        }
        """
        txt=texto
        miarchivo=open('PatronFinal.dot','w')
        miarchivo.write(txt)
        miarchivo.close()
        system('dot -Tpng PatronFinal.dot -o PatronFinal.png')
        system('cd ./PatronFinal.png')
        startfile('PatronFinal.png')
    


    

    




            










prin=Main()
prin.Menu()