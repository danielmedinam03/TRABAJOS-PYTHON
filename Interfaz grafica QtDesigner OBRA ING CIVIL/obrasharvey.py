# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:42:12 2020

@author: PC
"""
from math import*
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Obradeconstruccion.ui"

Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
#definir variables
acupre=0
deci_mano=0
deci_mats=0
deci_extra=0
pre_mano=0
pre_extra=0
pre_mats=0
totalsueldos=0
valortotal=0
sobrante=0
can_trab=0

class VentanaPrincipal(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #DECLARAMOS EL SIGMA
        self.pushButtonCalcular.clicked.connect(self.Calcular)
        self.pushButtonGuardar.clicked.connect(self.Guardar)
        
    def Calcular(self):
        
        #CALCULOS DE LOS PRESUPUESTOS
        presupuesto=self.Presupuesto.toPlainText()
        presupuesto=float(presupuesto)
        
        por_mano=self.PorcentajeMano.toPlainText()
        por_mats=self.PorcentajeMateriales.toPlainText()
        por_extra=self.PorcentajeExtra.toPlainText()
        
        por_mano=float(por_mano)
        por_mats=float(por_mats)
        por_extra=float(por_extra)
        #PASO DE PORCENTAJES A DECIMAL
        deci_mano=(por_mano/100)
        deci_mats=(por_mats/100)
        deci_extra=(por_extra/100)
        #PRESUPUESTO DE MANO DE OBRA, MATS, DINERO EXTRA
        pre_mano=(presupuesto*deci_mano)
        pre_extra=(presupuesto*deci_extra)
        pre_mats=(presupuesto*deci_mats)
        self.labelMano.setText(str(pre_mano))
        self.labelExtra.setText(str(pre_extra))
        self.labelMats.setText(str(pre_mats))
        
        totalpresupuestos=(pre_mano+pre_extra+pre_mats)
        self.labelPresupuesto.setText(str(totalpresupuestos))
        
        #CALCULOS DE SUELDOS DE TRABAJADORES
        can_trab=self.Numero.toPlainText()
        sueldo=self.Sueldo.toPlainText()
        can_trab=int(can_trab)
        sueldo=int(sueldo)
        
        totalsueldos=can_trab*sueldo
        
        #CALCULOS DINERO EXTRA GASTADO
        val_extra=self.DineroGastado.toPlainText()
        val_extra=int(val_extra)
        
        #PRECIO MATS
        val_mats=self.PrecioMats.toPlainText()
        val_mats=float(val_mats)
        
        #PRECIO DINEROS EXTRAS
        val_extra=self.DineroGastado.toPlainText()
        val_extra=float(val_extra)
        
        #CALCULOS VALOR TOTAL
        valortotal=totalsueldos+val_mats+val_extra
        self.labelTotal.setText(str(valortotal))
        
        if presupuesto>=valortotal:
            sobrante=presupuesto-valortotal
            result= 'Sobrante'
        elif presupuesto<valortotal:
            sobrante=presupuesto-valortotal
            sobrante=(sobrante*-1)
            result= 'Faltante'
    
        self.labelFalSob.setText(str(sobrante) + ' '+ result)
        
    def Guardar (self):
        presupuesto=self.Presupuesto.toPlainText()
        presupuesto=float(presupuesto)
        nombre=self.Nombre.toPlainText()
        
        #ARCHIVO
        archivo=open('Calculos_Obras.txt','a')
        #FORMATEA LA SALIDA
        archivo.write('NOMBRE: ' + ' ' + nombre + '--' + 'DINERO PRESUPUESTADO:  ' + str(presupuesto) + '--' + 'PRECIO DE LA CONSTRUCCION:    ' + str(valortotal) + '\n' )
        
        archivo.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())