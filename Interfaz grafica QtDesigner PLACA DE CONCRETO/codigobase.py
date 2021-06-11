# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:15:00 2020

@author: PC
"""

from math import*
print('CONCREPLACAS S.A. ')
Nombre=input('Nombre del cliente: ')
id=int(input('Ingrese no. del documento: '))
L=float(input('Ingresa la longitud de la placa: '))
A=float(input('Ingresa el ancho de la placa: '))
e=0.12
r=0.20
w_varilla=0.994
V=(L*A*e)
print('El volumen de la placa es: ', V, 'M3')

#CALCULO DE MATERIALES por metro cubico
cemento= (V*7)*1.05
arena= (V*0.56)
grava= (V*0.84)
agua= (V*180)
precio_cemento=(cemento*25000)
precio_arena=(arena*45000)
precio_grava=(grava*68000)
precio_agua=(agua*1000)

print('Total de cemento para la placa: ', '%.2f'%cemento, 'bolsas*50 kg', 'valor total del cemento: ', '%.0f'%precio_cemento, 'pesos')
print('Total de arena para la placa: ', '%.2f'%arena, 'M3', 'valor total del arena: ', '%.0f'%precio_arena, 'pesos')
print('Total de grava para la placa: ', '%.2f'%grava, 'M3', 'valor total del grava: ', '%.0f'%precio_grava, 'pesos')
print('Total de agua para la placa', '%.2f'%agua, 'Litros','valor total del agua: ', '%.0f'%precio_agua, 'pesos')

#acero figurado por metro linal

acero_ancho=(A/r)
acero_long=(L/r)
t_varillas_ancho=acero_ancho
t_varillas_long=acero_long

if A<=6:
    print('Total de varilas transversales: ', t_varillas_long, 'de 6 m cada varilla')
    t_met_ancho=(t_varillas_long*6)
    total_pesos_a=t_varillas_long*12500

else:
    print('Total de varilas transversales: ', t_varillas_long, 'de 12 m cada varilla')
    t_met_ancho=(t_varillas_long*12)
    total_pesos_a=t_varillas_long*25000

if L<=6:
    print('Total de varilas longitudinales: ', t_varillas_ancho, 'de 6 m cada varilla')
    t_met_long=(t_varillas_ancho*6)
    total_pesos_l=t_varillas_ancho*12500

else:
    print('Total de varilas longitudinales: ', t_varillas_ancho, 'de 12 m cada varilla')
    t_met_long=(t_varillas_ancho*12)
    total_pesos_l=t_varillas_ancho*25000

total_acero_lineal=(t_met_ancho+t_met_long)
t_w_acero=total_acero_lineal*w_varilla
total_pesosvarilla=total_pesos_a+total_pesos_l
print('Total acero x metros: ', total_acero_lineal,'metros de acero' )
print('Peso total del acero: ', '%.2f'%t_w_acero, 'Kg')
print('Valor total del acero: $',total_pesosvarilla )

#Mano de obra

mo=350000
m_o= V*mo
print('Valor total de la mano de obra $',m_o,)
#Maquinaria
mezcla_dora=35000
mezcladora=mezcla_dora

if V<=10:
    print('Valor total del alquiler de la mezcladora es de $35.000')

elif V>=11:
    print('Valor total del alquiler de la mezcladora es de $70.000')

#ACPM
acpm=3900
a_c_p_m= V*acpm
print('Valor total de la mano de obra es: $', m_o,)
print('Valor total del acpm es: $', a_c_p_m, )
#TOTAL A PAGAR
TOTAL=precio_cemento+precio_arena+precio_grava+precio_agua+total_acero_lineal+total_pesosvarilla+m_o+mezcladora+a_c_p_m

print('¡EL COSTO TOTAL DEL PRESUPUESTO ES!: $',TOTAL)