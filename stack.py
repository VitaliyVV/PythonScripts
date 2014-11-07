# -*- coding: utf-8 -*-
"""
Created on Tue Sep 09 10:23:48 2014
Блок расчета дымовой трубы
@author: Volovikov
"""

# block0090.py - Блок расчета дымовой трубы

import numpy

class Interceptors:
    """ Класс интерцептор дымовой трубы
    Интерцептор имеет тип (спиральный, прямой), длину, высоту и ширину полосы.
    Спиральный интерцептор может иметь параметры спирали, по которой он будет построен
    """
    L = float() # Длина 
    H = float() # Высота спирали (часть от высоты трубы не менее 1/3)
    a = float() 
    b = float()
    Type = int()
    Pitch = float() # helix pitch - шаг спирали
    
    
    #Alfa = float()


class Lighnings:
    """ Класс футеровки дымовой трубы"""    
    pass

class Ankers:
    """ Класс анкеров дымовой трубы"""
    pass

class StiffeningRings:
    """ Класс колец жесткости дымовой трубы"""
    pass




class Stacks:
    """ Класс, описывающий дымовую трубу"""
    H = float()    
    DN = float()    
    Interceptor = Interceptors()
    Lighning = Lighnings()
    Anker = Ankers()
    StiffeningRing = StiffeningRings()


# Объект класса "Дымовая труба", с результатами ручного расчета
StackCalculated = Stacks()
# Высота дымовой трубы, м
StackCalculated.H = 10.0
# Наружний диаметр, м
StackCalculated.DN = 1200.0/1000.0

# Минимальный и максимальный шаги колец жесткости 
StackCalculated.StiffeningRing.PitchMin = StackCalculated.DN
StackCalculated.StiffeningRing.PitchMax = StackCalculated.DN*3.0


# Объект класса "Дымовая труба", с результатами расчета на FH
StackFH = Stacks()

# Объект класса "Дымовая труба", с результатами ручного расчета,
# откорректированными по ГОСТ
StackGOST = Stacks()




StackGOST.Interceptor.H = StackCalculated.H/3.0
StackGOST.Interceptor.a = StackCalculated.DN*0.1
StackGOST.Interceptor.Pitch = StackCalculated.DN*5.0






# Выбор диаметра дымовой трубы


def fwGas(G,ro,f):
    """ Определение скорости газа в дымовой трубе, м/с
    по массовому расходу продуктов сгорания, плотности газов и
    площади проходного сечения"""
    fwGas = G/ro/f    
    return fwGas

def fDensityProdCombation(t):
    """ Определение плотности дымовых газов по Нормам теплового расчета, кг/м**3"""
    fDensityProdCombation = 1.3*273.15/(273.15+t)
    return fDensityProdCombation
    
def fSqCircle(D):
    """ Определение площади круга по диаметру, м**2"""
    fSqCircle = numpy.pi*(D**2.0)/4.0
    return fSqCircle
    
# Для справки!!!
    # Оптимальная скорость продуктов сгорания в дымовой трубе лежит в интервале
    # 4 - 6 м/с
wGasOptim = 6

    # Скорость продуктов сгорания на выходе из трубы, т.е. в устье трубы должна
    # лежать в интервале 6 - 10 м/с
# The mouth of the chimney - Устье дымовой трубы
wGasMinMouth = 6

# Температура точки росы может определяться как в ручном расчете, по методике
# переданной Доверманом Г.И., так и с помощью программы BoilerDesigner, или по
# нормам теплового расчета котельных агрегатов
TOkkes = 90.0

# Температура продуктов сгорания в дымовой трубе должна быть выше точки росы
# как минимум на 20 градЦ [ГОСТ Р 53682-2009, п. 13.2.8, стр. 27]
TGasOu = TOkkes + 20.0

# Футеровка должна иметь анкерное крепление [п. 13.2.10 и 11.3.7]
# возможно необходим расчет анкера, его размеров и температуры металла анкера.
# размеры анкера определяются толщиной футеровки, температура анкера - расчетом
# по температуре газов и теплопроводности футеровки.



# Массовый расход дымовых газов, кг/с
# Это значение надо или самому считать или взять из расчета FH
G = 2.02

# Температура продуктов сгорания на входе в дымовую трубу, градЦ
# Или расчитывается самостоятельно или берется из FH
Tetta = 151.0

# Плотность продуктов сгорания в дымовой трубе, кг/м**3
DensityProdCombation = fDensityProdCombation(Tetta)

# Толщина обечайки, м
DeltaShell = 0.008

# Толщина футеровки  дымовой трубы, м
DeltaLighning = 0.05


# Диаметр проходного сечения дымовой трубы,м
D_proh = 1.2-DeltaShell*2-DeltaLighning*2-0.0

# Площадь проходного сечения дымовой трубы, м**2
SqStack = fSqCircle(D_proh)

# Скорость продуктов сгорания в дымовой трубе, м/с
wGas = fwGas(G, DensityProdCombation, SqStack)


# Перебор диаметров устья и поиск подходящего
werDiamInner = [0.700, 0.800, 0.900, 1.0, 1.1, 1.2]
werDiam = list()
wGas02 = list()

for (item, Diam) in enumerate(werDiamInner):
    werDiam.append(Diam-DeltaShell*2-DeltaLighning*2-0.0)
    wGas02.append(fwGas(G, fDensityProdCombation(Tetta), fSqCircle(werDiam[item])))
    
