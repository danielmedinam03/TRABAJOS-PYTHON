# -*- coding: utf-8 -*-
"""
Created on Tue May 11 06:53:12 2021

@author: PC
"""
import serial
import sqlite3
import datetime
import time
import matplotlib.pyplot as plt
import pandas as pd
#import Seaborn as sb
#import numpy as np

conexion=sqlite3.connect("PRUEBABD.db")

dt=datetime.datetime.now()
COM ="COM10"
arduino=serial.Serial(COM, 9600)
cursor=conexion.cursor()
'''
cursor.execute("""CREATE TABLE DATAFINAL
               (NUM INTEGER PRIMARY KEY AUTOINCREMENT,
               FECHA VARCHAR (50),
               HORA VARCHAR (20),
               TEMPERATURA INTEGER,
               HUMEDAD FLOAT,
               CO2 FLOAT,
               UV FLOAT)""")
'''

lista=[]


try:
    while True:
        data=arduino.readline().decode('ascii')
        if data!="":
            dt=datetime.datetime.now()
            fecha='{}/{}/{}'.format(dt.year,dt.month,dt.day)
            hora='{}:{}:{}'.format(dt.hour,dt.minute,dt.second)
            
            line=data.split(sep=',')
            lista=[str(fecha),str(hora),int(line[0]),float(line[1]),float(line[2]),float(line[3])]
            time.sleep(5)
            print(lista)
            
            cursor=conexion.cursor()
            
            cursor.execute("INSERT INTO DATAFINAL VALUES (NULL,?,?,?,?,?,?)",lista)
            
            conexion.commit()

except KeyboardInterrupt:
      
#cursor.execute("SELECT * FROM DATA_PRE")
#datos=cursor.fetchall()
    surveys_df = pd.read_sql_query("SELECT * FROM DATAFINAL", conexion)
    print(surveys_df)
    #dt=np.array(dt_string)
    #temp = surveys_df[surveys_df.TEMPERATURA]
    #num=surveys_df.iloc[:,[0]]
    #hora=surveys_df.iloc[:,[2]]
    temp=surveys_df.iloc[:,[3]]
    hum=surveys_df.iloc[:,[4]]
    co=surveys_df.iloc[:,[5]]
    uv=surveys_df.iloc[:,[6]]
    plt.rcParams['figure.figsize']=(10, 4.8)

    #Grafica de Datos de la temperatura
    plt.title("Datos de la temperatura (C°)")
    plt.xlabel("Datos")
    plt.ylabel("Temperatura")
    plt.plot(temp, color='green')
    plt.show()
    #Histograma temperatura
    plt.hist(surveys_df['TEMPERATURA'], 15, color='green',ec='black')
    plt.title("Histograma de la Temperatura (C°)")
    plt.xlabel("Temperatura")
    plt.ylabel("Datos")
    plt.show()
    #Grafica de Datos de la Humedad
    plt.title("Datos de la Humedad (%)")
    plt.xlabel("Datos")
    plt.ylabel("Humedad")
    plt.plot(hum, color='yellow')
    plt.show()
    #Histograma Humedad
    plt.hist(surveys_df['HUMEDAD'], 15, color='yellow',ec='black')
    plt.title("Histograma de la Humedad (%)")
    plt.xlabel("Humedad")
    plt.ylabel("Datos")
    plt.show()
    #Grafica de Datos del CO2
    plt.title("Datos de la calidad del Aire (CO2)")
    plt.xlabel("Datos")
    plt.ylabel("CO2")
    plt.plot(co,color='blue')
    plt.show()
    #Histograma CO2
    plt.hist(surveys_df['CO2'], 15, color='blue',ec='black')
    plt.title("Histograma del CO2")
    plt.xlabel("CO2")
    plt.ylabel("Datos")
    plt.show()
    #Grafica de Datos de los Rayos UV
    plt.title("Datos de los Rayos UV")
    plt.xlabel("Datos")
    plt.ylabel("Rayos UV")
    plt.plot(uv,color='purple')
    plt.show()
    #Histograma UV
    plt.hist(surveys_df['UV'], 15,color='purple',ec='black')
    plt.title("Histograma de Rayos UV")
    plt.xlabel("Luz UV")
    plt.ylabel("Datos")
    plt.show()
    
    #Comparacion de las graficas
    def make_plot(axs):
        box = dict(facecolor='yellow', pad=3, alpha=0.2)
        
        # GRafica temperatura pos 0,0
        # Fixing random state for reproducibility
        ax1 = axs[0, 0]
        ax1.plot(temp, color="green")
        #ax1.set_title('Grafica de Temperatura')
        ax1.set_ylabel('Temperatura C°', bbox=box)
        ax1.set_ylim(0, 40)
        #Grafica de humedad pos 1,0
        ax3 = axs[1, 0]
        #ax3.set_title('Grafica de Humedad')
        ax3.set_ylabel('Humedad %', bbox=box)
        ax3.plot(hum, color="yellow")
        #Grafica de Co2 pos 0,1
        ax2 = axs[0, 1]
        #ax2.set_title('Grafica de CO2')
        ax2.plot(co, color="blue")
        ax2.set_ylabel('CO2', bbox=box)
        ax2.set_ylim(0, 5)
        #Grafica de UV pos 1,1
        ax4 = axs[1, 1]
        #ax4.set_title('Grafica de Rayos UV')
        ax4.plot(uv, color="purple")
        ax4.set_ylabel('UV', bbox=box)


    # Plot 1:
    fig, axs = plt.subplots(2, 2)
    fig.subplots_adjust(left=0.2, wspace=0.6)
    make_plot(axs)

    # just align the last column of axes:
    fig.align_ylabels(axs[:, 1])
    plt.show()

    conexion.commit()


conexion.close()
    
    
