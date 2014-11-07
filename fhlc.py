# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 13:20:47 2014
fhlc
Fire Heater Lining Calculation

футеровка: варианты перевода
имя существительное
lining - подкладка, выравнивание, облицовка, футеровка, подкладочный материал, выстилка
liner - лайнер, вкладыш, подкладка, прокладка, рейсовый пароход, футеровка
fettle - состояние, положение, футеровка
enwall - футеровка
inwall - футеровка

@author: Volovikov
"""
import numpy

# Расчет футеровки

# 1) Исходные данные:

# - Температура продуктов сгорания на перевале, degC
Tetta_Bridgewall = 709.0

# - Расчетная температура металла труб в камере радиации, degC
Temprature_Tube_Metall = 183.0

# - Температура продуктов сгорания на выходе из гладкотрубного пучка, degC
Tetta_Afte_Plain_Bandle = 594.0

# - Температура продуктов сгорания на выходе из пучка труб с развитой поверхностью, degC
Tetta_Afte_Fain_Bandle = 151.0

# - Температура горячего воздуха, degC
Temprature_Hot_Air = 80.0

# - Температура продуктов сгорания после ВП, degC
Temprature_Afte_Air_Heater = 151.0

# - Температура наружной поверхности оборудования в рабочей зоне, degC
Temprature_Surface_Work_Zone = 60.0

# - Температура наружной поверхности оборудования в необслуживаемой зоне, degC
Temprature_Surface_Notwork_Zone = 75.0

# - Температура окружающего воздуха, degC
Temperature_Environment = 23.6

# - Скорость ветра, m/s
Velocity_Wind = 0.0

# - Толщина однослойной изоляции (Задаемся) для следующих объектов, mm: 
# 0 - Под камеры радиации
# 1 - Экранированные стены
# 2 - Неэкранированные стены
# 3 - Стены гладкотрубной камеры конвекции
# 4 - Стены камеры конвекции с оребренными трубами
# 5 - Газосборник
# 6 - Дымовая труба
# 7 - Горячий воздуховод
NumberOfObject = 8
## Объекты        0      1      2      3      4     5     6     7
Delta_Lining = [200.0, 100.0, 100.0, 200.0, 150.0, 50.0, 50.0, 50.0]

# - Материал однослойной футеровки (Задаемся)
# Код материала футеровки:
# 1 - Алакс-0,9-1000
# 2 - Керамоволокно
## Объекты         0  1  2  3  4  5  6  7
Material_Lining = [1, 2, 2, 1, 1, 1, 1, 1]

# - Толщина обшивки (Задаемся), mm
## Объекты      0    1    2    3    4    5    6    7
Delta_Shell = [8.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]

# - Материал обшивки (Задаемся)
# Код материала обшивки:
# 0 - 09Г2С
# 1 - Ст3
## Объекты        0  1  2  3  4  5  6  7
Material_Shell = [0, 0, 0, 0, 0, 0, 0, 0]


# 2) Расчет

# - Коэффициент теплоотдачи от наружной поверхности к воздуху
Alfa_Air  = (5.8+11.6*numpy.sqrt(max(1.0,Velocity_Wind)))

# - Расчетная температура на поверхности футеровки, degC
## Объекты        0      1      2      3      4     5     6     7
T0 = Tetta_Bridgewall - 110
T1 = (Tetta_Bridgewall + Temprature_Tube_Metall)/2.0 + 55.0
T2 = Tetta_Bridgewall
T3 = max((Tetta_Bridgewall - 110),(Tetta_Bridgewall + Tetta_Afte_Plain_Bandle) / 2)
T4 = max((Tetta_Afte_Plain_Bandle - 110),(Tetta_Afte_Plain_Bandle + Tetta_Afte_Fain_Bandle) / 2)
T5 = Tetta_Afte_Fain_Bandle
T6 = Tetta_Afte_Fain_Bandle
T7 = Temprature_Afte_Air_Heater
Temperature_Design =  [T0, T1, T2, T3, T4, T5, T6, T7]
print ('Расчетная температура на поверхности футеровки, degC')
print (Temperature_Design)


# - Средняя температура в слое футеровки, degC
Temperature_Midle_Lining = [0.0]*len(Temperature_Design)
for elem in range(len(Temperature_Midle_Lining)):
    Temperature_Midle_Lining[elem] = (Temperature_Design[elem] + Temprature_Surface_Work_Zone)/2
print('Средняя температура в слое футеровки, degC')
print(Temperature_Midle_Lining)

# - Коэффициент теплопроводности обшивки, Вт/м
Lambda_Shell = [0.0]*len(Temperature_Design)
Lambda_Shell_Massiv =[ [50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 700.0, 900.0, 1100.0, 1200.0],
                       [45.0,  45.0,  45.0,  45.0,  45.0,  45.0,  45.0,  45.0,  45.0,  45.0]]
for elem in range(len(Temperature_Midle_Lining)):
    Lambda_Shell[elem] = numpy.interp(Temprature_Surface_Work_Zone,Lambda_Shell_Massiv[0],Lambda_Shell_Massiv[1])
print('Коэффициент теплопроводности обшивки, Вт/м')
print(Temperature_Midle_Lining)

# - Коэффициент теплопроводности футеровки, Вт/м
Lambda_Lining_Massiv01 = [[300.0,   400.0,  500.0,  600.0,  700.0],
                        [0.19,   0.205,   0.22,  0.235,   0.25]]
Lambda_Lining_Massiv02 = [[   0,  100,  200,  300,  400,  500,  600,   700,  800,   900, 1000, 1100, 1200, 1300, 1400, 1500],
                        [0.09, 0.09, 0.09, 0.09, 0.09, 0.11, 0.13, 0.155, 0.18, 0.215, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],]
Lambda_Lining = [0.0]*len(Temperature_Design)
for elem in range(len(Lambda_Lining)):
    if Material_Lining[elem] == 1:
        Lambda_Lining[elem] = numpy.interp(Temperature_Midle_Lining[elem],Lambda_Lining_Massiv01[0],Lambda_Lining_Massiv01[1])
    if Material_Lining[elem] == 2:
        Lambda_Lining[elem]  = numpy.interp(Temperature_Midle_Lining[elem],Lambda_Lining_Massiv02[0],Lambda_Lining_Massiv02[1])
print('Коэффициент теплопроводности футеровки, Вт/м') 
print(Lambda_Lining)

# - Коэффициент теплоотдачи от потока теплоносителя к поверхности футеровки, Вт/(м2*С)
Alfa_e_Massiv = [[50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 700.0, 900.0, 1100.0, 1200.0],
                 [12.0,  12.0,  12.0,  14.0,  18.0,  23.0,  47.0,  82.0,  140.0,  175.0]]
Alfa_e = [0.0]*len(Temperature_Design)
for elem in range(len(Alfa_e)):
    Alfa_e[elem]  = numpy.interp(Temperature_Design[elem],Alfa_e_Massiv[0],Alfa_e_Massiv[1])
print('Коэффициент теплоотдачи от потока теплоносителя к поверхности футеровки, Вт/(м2*С)')
print(Alfa_e)

# - Тепловой поток, Вт/м2
Q_Lining = [0.0]*len(Temperature_Design)
for elem in range(len(Q_Lining)):
    Q_Lining[elem]  = (Temperature_Design[elem]-Temperature_Environment)/((Delta_Shell[elem]/(1000*Lambda_Shell[elem]))+(Delta_Lining[elem]/(1000*Lambda_Lining[elem]))+1/Alfa_Air+1/Alfa_e[elem]) 
print('Тепловой поток, Вт/м2')
print(Q_Lining)

# - Температура на поверхности футеровки, degC
Temperature_On_Lining = [0.0]*len(Temperature_Design)
for elem in range(len(Temperature_On_Lining)):
    Temperature_On_Lining[elem]  = (Temperature_Design[elem]-Q_Lining[elem]/Alfa_e[elem]) 
print('Температура на поверхности футеровки, degC')
print(Temperature_On_Lining)

# - Температура наружной поверхности, degC
Temperature_On_Shell = [0.0]*len(Temperature_Design)
for elem in range(len(Temperature_On_Shell)):
    Temperature_On_Shell[elem]  = Temperature_Design[elem]-Q_Lining[elem]*(1/Alfa_e[elem]+Delta_Lining[elem]/(1000*Lambda_Lining[elem])+Delta_Shell[elem]/(1000*Lambda_Shell[elem])) 
print('Температура наружной поверхности, degC')
print(Temperature_On_Shell)
