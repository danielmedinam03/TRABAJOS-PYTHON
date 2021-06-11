# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:57:40 2020

@author: x1920
"""
import sys
from PyQt5 import uic, QtWidgets
#Librerias para manejo de imagenes

#otras librerias
import pandas as pd

import matplotlib.pyplot as plt
#Nombre de nuestro archivo ui
qtCreatorFile = "anomalia.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

#Clase de la ventana
class VentanaPrincipal(QtWidgets.QMainWindow,Ui_MainWindow):
 
    #Metodo constructor de la clase 
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
     
      #Declaramos el Signal -> Objeto pushButton y el Slots-> Metodo 
        self.btnGraficar.clicked.connect(self.Graficar)
        self.btnGuardar.clicked.connect(self.Guardar)
        self.btnAnomalia.clicked.connect(self.anomalia)
  
    def Graficar(self): 
        data = pd.DataFrame(map(float,(self.txtingresodatos.toPlainText().split(','))))
        plt.plot(data)
        plt.title('Grafico de Datos')
        plt.xlabel('# de datos')
        plt.ylabel('Datos')
        plt.show()
    def anomalia(self):
        plt.rcParams['figure.figsize']=(16.0, 6.0)
        #data=self.txtingresodatos.toPlainText()
        data = pd.DataFrame(map(float,(self.txtingresodatos.toPlainText().split(','))))
        wind=20
        sigma=2
        data["suelo"] = data[0].rolling(window=wind)\
            .mean() - (sigma * data[0].rolling(window=wind).std())
        data["techo"] = data[0].rolling(window=wind)\
            .mean() + (sigma * data[0].rolling(window=wind).std())
        data["anom"] = data.apply(
            lambda row: row[0] if (row[0]<=row["suelo"] or row[0]>=row["techo"]) else 0, axis=1)
        data.plot()
        plt.title('Anomalia')
        plt.xlabel('# de datos')
        plt.ylabel('Datos')
        plt.show()
   
     
         #Metodo para guardar los campos en un Archivo
    def Guardar(self): 
        nombre = self.txtnombre.toPlainText()
        datos = self.txtdatostipo.toPlainText()
       # ingresardatos = self.txtingresodatos.toPlainText()
        
        #Trabajando con Archivos
        archivo = open("anomalias.txt","a")
    
        #Formateamos la salida tabulando con \n y concatenamos
        archivo.write('Nombre: '+ nombre +'\n' 'Tipo: '+ datos )                 
        archivo.close()
             
if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())
    
    