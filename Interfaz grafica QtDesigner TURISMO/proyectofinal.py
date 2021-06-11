# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:43:02 2020

@author: USUARIO
"""

from math import*
import numpy as np
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "TurismoTolima.ui"

Ui_MainWindow, QtBaseClass= uic.loadUiType(qtCreatorFile)

#Definir variables
val1=0
val2=0
precio=0

pniñ=120000  #Precio niños viaje a represa de prado
padul=160000  #Precio aultos viaje a represa de prado
nniñ=110000  #Precio niños viaje a parque nacional de los nevados
nadul=150000  #Precio aultos viaje a parque nacional de los nevados
cniñ=150000  #Precio niños viaje a cafam
cadul=180000  #Precio aultos viaje a cafam

#Clase de la ventana
class VentanaPrincipal(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #Declaramos el sigma, objeto pushButton
        self.btnCalcular.clicked.connect(self.Calcular)
        self.btnGuardar.clicked.connect(self.Guardar)
        
        
    def Calcular(self):
        opcioncombo= self.lugares.currentText()
        if opcioncombo=='REPRESA PRADO':
            dias=self.textEditDias.toPlainText()
            niños=self.textEditNinos.toPlainText()
            adultos=self.textEditAdultos.toPlainText()
                
            niños=int(niños)
            dias=int(dias)
            adultos=int(adultos)
            val1=(niños*pniñ)*dias
            val2=((adultos+1)*padul)*dias
            valor= (val1+val2)
                
            self.precio.setText( str(valor) )
        if opcioncombo=='PARQUE NACIONAL NATURAL DE LOS NEVADOS':
            dias=self.textEditDias.toPlainText()
            niños=self.textEditNinos.toPlainText()
            adultos=self.textEditAdultos.toPlainText()
                
            niños=int(niños)
            dias=int(dias)
            adultos=int(adultos)
            
            val1=(niños*nniñ)*dias
            val2=((adultos+1)*nadul)*dias
            valor= (val1+val2)
            self.precio.setText( str(valor) )
                
            
        if opcioncombo=='CAFAM':
            dias=self.textEditDias.toPlainText()
            niños=self.textEditNinos.toPlainText()
            adultos=self.textEditAdultos.toPlainText()
            
            niños=int(niños)
            dias=int(dias)
            adultos=int(adultos)
            
            val1=(niños*cniñ)*dias
            val2=((adultos+1)*cadul)*dias
            valor= (val1+val2)
            self.precio.setText( str(valor) )
                
                
                
                #MEtodo para guardar los campos en un Archivo
        
    def Guardar(self):
        nombre=self.textEditNombre.toPlainText()
        cedula=self.textEditIdent.toPlainText()
        diasalquiler=self.textEditDias.toPlainText()
        #valor=self.precio.setText.toPlainText()
            
            
            
        #Trabajando con Archivos
        archivo=open('Turismo_Tolima.txt','a')
        opcioncombo=self.lugares.currentText()
            
            
        #Formateamos la salida tabulando con \n
        archivo.write('NOMBRE: '+' '+ nombre + ' - ' + 'CEDULA :' + cedula + 'DESTINO : ' + str (opcioncombo)+' ' + 'DIAS DE HOSPEDAJE' + diasalquiler + ' TOTAL :' + '\n')
        
        archivo.close()
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())

        
