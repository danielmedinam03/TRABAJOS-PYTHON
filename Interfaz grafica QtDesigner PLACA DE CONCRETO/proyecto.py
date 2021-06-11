# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:21:10 2020

@author: PC
"""

from math import*
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "concreplacas.ui"

Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

e=0.12
r=0.20
w_varilla=0.994
A=0
L=0

class VentanaPrincipal(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #DECLARAMOS EL SIGMA
        self.pushButtonCalcular.clicked.connect(self.Calcular)
        self.pushButtonGuardar.clicked.connect(self.Guardar)
        
    def Calcular(self):
        
        e=0.12
        r=0.20
        A=0
        L=0
        L=self.textEditLongitud.toPlainText()
        A=self.textEditAncho.toPlainText()
        L=int(L)
        A=int(A)
        
        V=(L*A*e)
        self.labelVolumen.setText(str(V))
        
        
        cemento= (V*7)*1.05
        arena= (V*0.56)
        grava= (V*0.84)
        agua= (V*180)
        precio_cemento=(cemento*25000)
        precio_arena=(arena*45000)
        precio_grava=(grava*68000)
        precio_agua=(agua*1000)
        
        acero_ancho=(A/r)
        acero_long=(L/r)
        t_varillas_ancho=acero_ancho
        t_varillas_long=acero_long
        
        if A<=6:
            t_met_ancho=(t_varillas_long*6)
            total_pesos_a=t_varillas_long*12500
        else:
            t_met_ancho=(t_varillas_long*12)
            total_pesos_a=t_varillas_long*25000
        if L<=6:
            t_met_long=(t_varillas_ancho*6)
            total_pesos_l=t_varillas_ancho*12500
        else:
            t_met_long=(t_varillas_ancho*12)
            total_pesos_l=t_varillas_ancho*25000
        total_acero_lineal=(t_met_ancho+t_met_long)
        
        #PESO TOTAL DEL ACERO
        #t_w_acero=total_acero_lineal*w_varilla
        
        total_pesosvarilla=total_pesos_a+total_pesos_l
        
        #Mano de obra
        mo=350000
        m_o= V*mo
        
        #Maquinaria
        mezcla_dora=35000
        mezcladora=mezcla_dora
        
        #ACPM
        acpm=3900
        a_c_p_m= V*acpm
        
        #TOTAL A PAGAR
        TOTAL=precio_cemento+precio_arena+precio_grava+precio_agua+total_acero_lineal+total_pesosvarilla+m_o+mezcladora+a_c_p_m

        self.textEditTotal.setText(str(TOTAL))
        
    def Guardar(self):
        nombre=self.textEditNombre.toPlainText()
        Id=self.textEditId.toPlainText()
        L=self.textEditLongitud.toPlainText()
        A=self.textEditAncho.toPlainText()
        TOTAL=self.textEditTotal.toPlainText()
        
        
        
        #SE TRABAJA  CON EL ARCHIVO
        archivo=open('DatosConcreplacas.txt','a')
        archivo.write('NOMBRE:' + '' + nombre + 'IDENTIFICACION: ' + '' + Id + '' + 'LONGITUD: ' + '' +L+ 'ANCHO: ' + '' + A + 'TOTAL A PAGAR: ' + TOTAL + '' + '\n' )
              
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())