# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:53:36 2020

@author: PC
"""

#Se plantea un problema donde se desea calcular con cuanto dinero disponen 3 áreas de\n",
#una obra(mano de obra,materiales, dinero extra). Presupuestando un monto inicial y colocando un porcentaje de manera\n",
#hipotética a cada área(se puede elegir cualquier porcentaje dividiendolo entre las 3 areas), efectuando esto, sabiendo la cantidad con la que cuenta cada\n",
#área, se desea saber si dicho presupuesto alcanza."
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

#PRESUPUESTO DE LA OBRA
nombre=input('NOMBRE DEL INGENIERO O CONSTRUCTOR: ')
presupuesto=(float(input('Digite dinero presupuestado para la obra: ')))
por_mano=float(input('DIGITE EL PORCENTAJE MANO DE OBRA: '))
por_mats=float(input('DIGITE EL PORCENTAJE MATERIALES: '))
por_extra=float(input('DIGITE EL PORCENTAJE DINERO EXTRA: '))
deci_mano=(por_mano/100)
deci_mats=(por_mats/100)
deci_extra=(por_extra/100)
pre_mano=(presupuesto*deci_mano)
pre_extra=(presupuesto*deci_extra)
pre_mats=(presupuesto*deci_mats)
print('El presupuesto para la mano de obra sera de: $',pre_mano)
print('El presupuesto para los materiales sera de: $',pre_mats)
print('El presupuesto para dinero extra de la sera de: $',pre_extra)

#PRESUPUESTO DE LOS MATERIALES ¿ALCANZA?

n=int(input('Digite cantidad de materiales: '))
for i in range (1,n+1):
    precio_mats=float(input('Digite precio de los materiales: '))
    acupre=acupre+precio_mats
print('El total del precio de los materiales es: $',acupre)

if acupre>pre_mats:
    print('No alcanza el presupuesto')
elif acupre<=pre_mats:
    print('El presupuesto asignado si alcanza')
#PRESUPUESTO DE MANO DE OBRA ¿ALCANZA?    
can_trab=int(input('Digite numero de trabajadores: '))
sueldo=float(input('Digite sueldo a pagar a cada trabajador: $'))
totalsueldos=(can_trab*sueldo)
if totalsueldos>pre_mano :
    print('No alcanza el presupuesto de mano de obra')
elif totalsueldos<=pre_mano:
    print('El presupuesto asignado si alcanza')
    
#PRESUPUESTO DE DINERO EXTRA
val_extra=float(input('Digite el valor extra gastado:'))

if val_extra>pre_extra:
    print('No alcanza el presupuesto')
elif val_extra<=pre_extra:
    print('Si alcanza el presupuesto asignado')
    
valortotal=acupre+totalsueldos+val_extra

print('El valor total de la Construccion es de: $',valortotal)
if presupuesto>=valortotal:
    sobrante=presupuesto-valortotal
    print('El dinero sobrante es: $',sobrante)
elif presupuesto<valortotal:
    sobrante=presupuesto-valortotal
    sobrante=(sobrante*-1)
    print('El dinero faltante es: $',sobrante)
    
    
    