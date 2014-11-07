# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:09:35 2014

@author: Volovikov
"""

#import numpy as np
#import scipy as sp



# Подготовим структуру данных для хранения исходных данных и результатов расчетов 
#
# DTC = DesignThermalCalculation
# STC = SimulationThermalCalculation

ID= {}
TechData = {}
Rez = {}
Note = {}
        
# Пример доступа до поля и присвоения переменной значения, переменная - словарь
#dataAH['DesignThermalCalculation']['ID']['Key'] = [156]


# Объект - воздухоподогреватель с данными ручного счета
# Air Heater Manual Calculation



# Наружний диаметр труб, м - Задаемся ИД
ID['DOut'] = {'Value': 45.0/1000.0, 'Unit': 'm'}

# Толщина стенки трубы, м - Задаемся ИД
ID['TubeThickness'] = {'Value': 1.5/1000.0, 'Unit': 'm'}

# Внутренний диаметр трубы, м - РР
Rez['DIn'] = {'Value': ID['DOut']['Value']-2.0*ID['TubeThickness']['Value'], 'Unit': 'm'}

# Высота одного хода ВП, м - Задаемся ИД
ID['H1Unit'] = {'Value': 2.0, 'Unit': 'm'}

# Число ходов ВП, шт - Задаемся ИД
ID['ZUnit'] = {'Value': 4.0, 'Unit': 'm'}

# Технологическая прибавка к шагу трубы в трубной доске, м - Задаемся ИД
ID['TechDeltaS1'] = {'Value': 11.0/1000.0, 'Unit': 'm'}

# Поперечный шаг труб, м - Задаемся ИД
ID['S1'] = {'Value': 80.0/1000.0, 'Unit': 'm'}
Rez['S1'] = {'Value': max(ID['S1']['Value'], ID['DOut']['Value']+ID['TechDeltaS1']['Value']), 'Unit': 'm'}

# Продольный шаг труб, м - Задаемся ИД
ID['S2'] = {'Value': 40.0/1000.0, 'Unit': 'm'}
Rez['S2'] = {'Value': max(ID['S2']['Value'], ((ID['DOut']['Value']+ID['TechDeltaS1']['Value'])**2-(Rez['S1']['Value']*0.5)**2)**0.5), 'Unit': 'm'}
#AHMC.ThermCalc.DC.Rez.S2 = max(AHMC.ThermCalc.DC.ID.S2, ((AHMC.ThermCalc.DC.ID.DOut+AHMC.ThermCalc.DC.ID.TechDeltaS1)**2-(AHMC.ThermCalc.DC.Rez.S1*0.5)**2)**0.5)
#
#
#
#



def ftStMinNear (tAH1, TettaAH2):
    return tAH1+0.35*(TettaAH2-tAH1)

    
tAH1 = [-33.0, -22.0, 10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0]
TSt=[]
for elem in tAH1:
    TSt.append(ftStMinNear(elem,190))
























