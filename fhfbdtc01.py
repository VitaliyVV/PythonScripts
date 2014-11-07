# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 15:04:07 2014
# Fire Heater Fire Box DTC (конструктивный расчет) не дотягивает до конструкторского, потому что идет подбор только по ГОСТу Р.
# Подбор допустимой геометрии топочной камеры
@author: Volovikov
"""
import numpy
# Подбор допустимой геометрии топочной камеры

# Исходные данные

# Тип печи: 1 - цилиндрическая; 2 - коробчатая
TypeFH = 2
# Расчетное теплопоглощение печи, МВт
QFH = 4.4

# Дополнительные исходные данные

# ИД по трубам
# Наружний диаметр радиационных труб, м
DTubeOuRad = 0.159
# Толщина стенки радиационных труб, м
DeltaTubeRad = 0.008
# Внутренний диаметр радиационных труб, м
DTubeInRad = DTubeOuRad - 2.0*DeltaTubeRad

# ИД по отводам
# Наружний диаметр отвода радиационных труб, м
DTubeOuRadOtv = 0.159
# Толщина стенки отвода радиационных труб, м
DeltaTubeRadOtv = 0.008
# Внутренний диаметр отвода радиационных труб, м
DTubeInRadOtv = DTubeOuRadOtv - 2.0*DeltaTubeRadOtv
# Межцентровое расстояние отвода радиационных труб, м
MCROtv = 0.3

# ИД по горелкам

# Тип горелки: 1 - инжекционная; 2 - дутьевая
TypeBurner = 1
# Тип сжигаемого топлива: 1 - мазут; 2 - газ
TypeFuel = 2

# Данные по каталагам

# Каталог НПЦ ЭО
# Номинальная мощность одной горелки, МВт
Q1BurnerCatalog01 = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]
# Наружный диаметр горелочного камня горелки, м
DOuBurnerStone01 = [0.5, 0.5, 0.5, 0.65, 0.8, 0.8, 0.9, 0.9]
# Расстояние между горелочными камнями
DistanceBurnerStone01 = [0.2]*8
# Номинальная длина видимого факела, не более, м
# на мазуте, м
if TypeFuel == 1:
    FlameLength01 = [2.5, 3.0, 3.0, 3.5, 4.5, 5.5, 7.0, 8.5]
# на газе, м
if TypeFuel == 2:
    FlameLength01 = [2.0, 2.5, 2.5, 3.0, 4.0, 5.0, 6.5,	8.0]


# Отношение максимально возможной мощности печи к номинальной мощности горелки по каталогу
RatioQB = [0.0]*len(Q1BurnerCatalog01)
for elem in range(len(RatioQB)):
    RatioQB[elem] = QFH*1.2/Q1BurnerCatalog01[elem]

# Коэффициент увеличения мощности печи для подбора числа горелок, п. 14.1.17, стр. 31 ГОСТ Р 53682-2009
kQB = [0.0]*len(Q1BurnerCatalog01)
for elem in range(len(kQB)):
    if numpy.trunc(RatioQB[elem]) <= 5:
        kQB[elem] = 1.2
    if numpy.trunc(RatioQB[elem]) == 6 or numpy.trunc(RatioQB[elem]) ==7:
        kQB[elem] = 1.15
    if numpy.trunc(RatioQB[elem]) >= 8:
        kQB[elem] = 1.1
    
# Надо дополнить и обработать в соответствии с п. 14.1.7 ГОСТ Р !!!!
# неточность пока что в коэффициенте 1,2 он может быть меньше при определенных условиях
# - а именно, когда число горелок больше 5

# Число требуемых горелок, заданной мощности
NBurner = [0.0]*len(Q1BurnerCatalog01)
for elem in range(len(NBurner)):
    NBurner[elem] =  numpy.ceil(QFH*kQB[elem]/Q1BurnerCatalog01[elem])

# Максимальное тепловыделение на одну горелку, МВт
MQ1B = [0.0]*len(NBurner)
for elem in range(len(NBurner)):
    MQ1B[elem] = QFH*kQB[elem]/NBurner[elem]

# Результаты расчета

# Минимальный коэффициент - отношение высоты радиационной камеры к ширине
kmin = 1.5
# Максимальный коэффициент - отношение высоты радиационной камеры к ширине
if TypeFH == 1:
    kmax = 2.75
if TypeFH == 2:
    if (QFH < 3.5):
        kmax = 2.0
    if (QFH >= 3.5) and (QFH < 7.0):
        kmax = 2.5
    if (QFH >=  7.0):
        kmax = 2.75

# Определение функций расчета длин из ГОСТ Р

def flength01(TypeFuel, TypeBurner, MQ1B):
    """ Функция определения расстояния по вертикали до осевой линии потолочных труб или до огнеупора (только при вертикальном факеле), м"""
    # Для жидкого топлива
    if TypeFuel == 1:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength01 = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0,  3.5,   4.0),
            (4.3, 5.6, 7.0, 8.3, 9.7, 11.0,  12.4))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength01 = 0.0
    # Для газового топлива
    if TypeFuel == 2:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength01 = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (2.6, 3.6, 4.6, 5.6, 6.7, 7.7, 8.7, 9.7, 10.7, 11.7))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength01 = 0.0
    return flength01        

def flength02(TypeFuel, TypeBurner, MQ1B):
    """ Функция определения расстояния по горизонтали от осевой линии горелки до осевой линии стеновых труб, м"""
    # Для жидкого топлива
    if TypeFuel == 1:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength02 = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0),
            (0.8, 0.9, 1.1, 1.2, 1.3, 1.4, 1.6))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength02 = numpy.interp(MQ1B,
            (2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0),
            (0.932, 1.182, 1.359, 1.52, 1.664, 1.919, 2.143, 2.346))
    # Для газового топлива
    if TypeFuel == 2:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength02 = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (0.6, 0.7, 0.8, 1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.8))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength02 = numpy.interp(MQ1B,
            (2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0),
            (0.932, 1.182, 1.359, 1.52, 1.664, 1.786, 1.923, 2.035))
    return flength02        

def flength03(TypeFuel, TypeBurner, MQ1B):
    """ Функция определения расстояния по горизонтали от осевой линии горелки до неэкранированного огнеупора, м"""
    # Для жидкого топлива
    if TypeFuel == 1:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength03 = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0,  3.5,   4.0),
            (0.56, 0.7, 0.83, 0.96, 1.09, 1.22, 1.35))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength03 = 0.0
    # Для газового топлива
    if TypeFuel == 2:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength03 = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (0.44, 0.56, 0.7, 0.83, 0.96, 1.09, 1.22, 1.35, 1.48, 1.61))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength03 = 0.0
    return flength03        

def flength04(TypeFuel, TypeBurner, MQ1B):
    """ Функция определения расстояния  между противоположными горелками (при горизонтальном факеле), м"""    """ Функция определения расстояния по горизонтали от осевой линии горелки до неэкранированного огнеупора, м"""
    # Для жидкого топлива
    if TypeFuel == 1:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength04 = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0,  3.5,   4.0),
            (6.5, 8.8, 11.2, 13.3, 14.8, 16.4, 18.0))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength04 = 0.0
    # Для газового топлива
    if TypeFuel == 2:
        # Для инжекционной горелки
        if TypeBurner == 1:
            flength04 = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (3.4, 4.9, 6.5, 8.1, 9.6, 11.1, 11.9, 12.6, 13.4, 14.2))
        # Для дутьевой горелки
        if TypeBurner == 2:
            flength04 = 0.0
    return flength04        


# Расчеты

# Инициализация
Nvar = [0]*len(NBurner)
if TypeFH == 2:
    HFireboxMin=[0.0]*len(NBurner)
    AFireboxMin=[0.0]*len(NBurner)
    HFireboxMax=[0.0]*len(NBurner)
    BFireboxMin=[0.0]*len(NBurner)
    EpsQBurner= [0.0]*len(NBurner)
    print 'Q = {} МВт'.format(QFH)
    for elem in range(len(NBurner)):
        Nvar[elem]=elem+1
        # Миниальное расстояние по вертикали между огнеупорами или осями труб, м
        # Минимально возможная высота
        HFireboxMin[elem] = flength01(TypeFuel, TypeBurner, MQ1B[elem])
        # Минимальная ширина топки или ее диаметр - расстояние между экранированными стенами (расстоние между боковыми экранированными стенами)
        AFireboxMin[elem] = 2.0*flength02(TypeFuel, TypeBurner, MQ1B[elem])
        # Приблизительная максимально возможная высота топки
        HFireboxMax[elem] = AFireboxMin[elem]*kmax
        # Минимальная глубина растояние между боковыми огнеупорными неэкранированными стенами, м (В)
        BFireboxMin[elem] = 2.0*flength03(TypeFuel, TypeBurner, MQ1B[elem])+(DOuBurnerStone01[elem]+DistanceBurnerStone01[elem])*(NBurner[elem]-1)
        EpsQBurner[elem] = (Q1BurnerCatalog01[elem]- MQ1B[elem])*100/Q1BurnerCatalog01[elem]
# Вывод результатов
        print 'Nvar = {}, NBurner={}, Q1B = {}, MQ1B = {}, EpsQ = {} %, HFMin = {}, HFMax = {}, A = {}, B = {}'.format(Nvar[elem], NBurner[elem], Q1BurnerCatalog01[elem], MQ1B[elem], EpsQBurner[elem], HFireboxMin[elem], HFireboxMax[elem], AFireboxMin[elem], BFireboxMin[elem])
# Результаты

# Выбранный вариант 
Nrez = range(0,11,1)
for elem0 in range(len(NBurner)):
    A = [0.0]*len(Nrez)
    B = [0.0]*len(Nrez)
    H = [0.0]*len(Nrez)
    print ' ***** Nvar = {}, NBurner = {}, Q1B = {} МВт, FL = {} м'.format(elem0+1,NBurner[elem0], Q1BurnerCatalog01[elem0], FlameLength01[elem0])
    for elem in range(len(A)):
        A[elem] = numpy.trunc(AFireboxMin[elem0])+numpy.trunc((AFireboxMin[elem0]-numpy.trunc(AFireboxMin[elem0]))*10)/10+0.1*elem
        Regul01 = 1
        if Regul01 == 1:
            B[elem] = 1.5*A[elem]
            Check01 = (B[elem] >= BFireboxMin[elem0])
        if Regul01 == 2:
            B[elem] = BFireboxMin[elem0]
            Check01 = (B[elem]>= AFireboxMin[elem0]*1.1)
        H[elem] = kmax*A[elem]
        if (H[elem] >= HFireboxMin[elem0]) and (A[elem] >= AFireboxMin[elem0]) and Check01 and (FlameLength01[elem0] <= 2.0*H[elem]/3.0) :
            print 'A={:5} м, B={:5} м, 2/3H = {:5.3} м, H={:5} м'.format(A[elem], B[elem], 2*H[elem]/3, H[elem])
