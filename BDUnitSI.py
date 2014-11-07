# -*- coding: utf-8 -*-
"""
Spyder Editor

Модуль для хранения базы данных перевода внесистемных размерностей 
величин в систему СИ
"""


# Словарь - БД, содержащая имя внесистемной единицы и коэффициент перевода в 
# систему СИ. Все вроде легко и просто g - грамм - 0,001 kg
# FormDim - формула размерности физической величины для возможной проверки формулы размерности
UnitSI = []


""" Физическая величина — физическое свойство материального объекта, физического явления, процесса, которое может быть охарактеризовано количественно."""
# physical quantity 

# Основные единицы СИ и их размерности

"""Основная величина, Символ для размерности
    Длина, L
    Масса, M
    Время, T
    Электрический ток, I
    Термодинамическая температура, Tetta
    Количество вещества, N
    Сила света, J"""


# Длина, метр (metre)
UnitSI.append({'m': {'Quantity': 'Length', 'Value':1,'Unit':'m', 'FormDim': 'L'}})
# Масса, килограмм (kilogramme)
UnitSI.append({'kg': {'Quantity': 'Mass', 'Value':1,'Unit':'kg', 'FormDim': 'M'}})
# Время, секунда (second)
UnitSI.append({'s': {'Quantity': 'Time', 'Value':1,'Unit':'s', 'FormDim': 'T'}})
# Сила электрического тока, Ампер (Ampere)
UnitSI.append({'A': {'Quantity': 'Electric current', 'Value':1,'Unit':'A', 'FormDim': 'I'}})
# Термодинамическая температура, градус Кельвин 
UnitSI.append({'K': {'Quantity': 'Temperature', 'Value':1,'Unit':'degC', 'FormDim': 'Tetta'}})
# Тут, я бы хотел все нарушить и ввести свой Цельсий как основной!!!
UnitSI.append({'degC': {'Quantity': 'Temperature', 'Value':1,'Unit':'degC', 'FormDim': 'Tetta'}})
# Количество вещества, моль (mole)
UnitSI.append({'mol': {'Quantity': 'Amount of substance', 'Value':1,'Unit':'mol', 'FormDim': 'N'}})
# Сила света, кандела (candela)
UnitSI.append({'cd': {'Quantity': 'Luminous intensity', 'Value':1,'Unit':'cd', 'FormDim': 'J'}})


"""Производные единицы с собственными названиями
Величина	Единица	Обозначение	Выражение 
русское название	французское/английское название	русское	международное
Плоский угол	радиан	radian	рад	rad	м·м−1 = 1
Телесный угол	стерадиан	steradian	ср	sr	м2·м−2 = 1
Температура Цельсия[6]	градус Цельсия	degré Celsius/degree Celsius	°C	°C	K
Частота	герц	hertz	Гц	Hz	с−1
Сила	ньютон	newton	Н	N	кг·м·c−2
Энергия	джоуль	joule	Дж	J	Н·м = кг·м2·c−2
Мощность	ватт	watt	Вт	W	Дж/с = кг·м2·c−3
Давление	паскаль	pascal	Па	Pa	Н/м2 = кг·м−1·с−2
Световой поток	люмен	lumen	лм	lm	кд·ср
Освещённость	люкс	lux	лк	lx	лм/м² = кд·ср/м²
Электрический заряд	кулон	coulomb	Кл	C	А·с
Разность потенциалов	вольт	volt	В	V	Дж/Кл = кг·м2·с−3·А−1
Сопротивление	ом	ohm	Ом	Ω	В/А = кг·м2·с−3·А−2
Электроёмкость	фарад	farad	Ф	F	Кл/В = с4·А2·кг−1·м−2
Магнитный поток	вебер	weber	Вб	Wb	кг·м2·с−2·А−1
Магнитная индукция	тесла	tesla	Тл	T	Вб/м2 = кг·с−2·А−1
Индуктивность	генри	henry	Гн	H	кг·м2·с−2·А−2
Электрическая проводимость	сименс	siemens	См	S	Ом−1 = с3·А2·кг−1·м−2
Активность радиоактивного источника	беккерель	becquerel	Бк	Bq	с−1
Поглощённая доза ионизирующего излучения	грей	gray	Гр	Gy	Дж/кг = м²/c²
Эффективная доза ионизирующего излучения	зиверт	sievert	Зв	Sv	Дж/кг = м²/c²
Активность катализатора	катал	katal	кат	kat	моль/с
"""
# Плоский угол	радиан	radian	рад	rad	м·м−1 = 1
UnitSI.append({'rad': {'Quantity': 'Angle', 'Value':1,'Unit':'rad', 'FormDim': ''}})
# Телесный угол	стерадиан	steradian	ср	sr	м2·м−2 = 1
UnitSI.append({'sr': {'Quantity': 'Solid angle', 'Value':1,'Unit':'sr', 'FormDim': ''}})
# Частота	герц	hertz	Гц	Hz	с−1
UnitSI.append({'Hz': {'Quantity': 'Frequency', 'Value':1,'Unit':'Hz', 'FormDim': 'T**-1'}})
# Сила	ньютон	newton	Н	N	кг·м·c−2
UnitSI.append({'N': {'Quantity': 'Force, Weight', 'Value':1,'Unit':'N', 'FormDim': 'M*L*(T**-2)'}})
# Энергия	джоуль	joule	Дж	J	Н·м = кг·м2·c−2
UnitSI.append({'J': {'Quantity': 'Energy, Work, Heat', 'Value':1,'Unit':'J', 'FormDim': 'M*L**2*(T**-2)'}})
# Мощность	ватт	watt	Вт	W	Дж/с = кг·м2·c−3
UnitSI.append({'W': {'Quantity': 'Power, Radiant flux', 'Value':1,'Unit':'W', 'FormDim': 'M*L**2*(T**-3)'}})
# Давление	паскаль	pascal	Па	Pa	Н/м2 = кг·м−1·с−2
UnitSI.append({'Pa': {'Quantity': 'Pressure, Stress', 'Value':1,'Unit':'Pa', 'FormDim': 'M*(L**-1)*(T**-2)'}})
# Световой поток	люмен	lumen	лм	lm	кд·ср
UnitSI.append({'lm': {'Quantity': 'Luminous flux', 'Value':1,'Unit':'lm', 'FormDim': ''}})
# Освещённость	люкс	lux	лк	lx	лм/м² = кд·ср/м²
UnitSI.append({'lx': {'Quantity': 'Illuminance', 'Value':1,'Unit':'lx', 'FormDim': ''}})
# Электрический заряд	кулон	coulomb	Кл	C	А·с
UnitSI.append({'C': {'Quantity': 'Electric charge, Electricity', 'Value':1,'Unit':'C', 'FormDim': ''}})
# Разность потенциалов	вольт	volt	В	V	Дж/Кл = кг·м2·с−3·А−1
UnitSI.append({'V': {'Quantity': 'Voltage', 'Value':1,'Unit':'V', 'FormDim': 'M*(L**2)*(T**-3)*(I**-1)'}})
# Сопротивление	ом	ohm	Ом	Ω	В/А = кг·м2·с−3·А−2
UnitSI.append({'Om': {'Quantity': 'Electric resistance, Impedance, Reactance', 'Value':1,'Unit':'Om', 'FormDim': ''}})
# Электроёмкость	фарад	farad	Ф	F	Кл/В = с4·А2·кг−1·м−2
UnitSI.append({'F': {'Quantity': 'Electric capacitance', 'Value':1,'Unit':'F', 'FormDim': ''}})
# Магнитный поток	вебер	weber	Вб	Wb	кг·м2·с−2·А−1
UnitSI.append({'Wb': {'Quantity': 'Magnetic flux', 'Value':1,'Unit':'Wb', 'FormDim': ''}})
# Магнитная индукция	тесла	tesla	Тл	T	Вб/м2 = кг·с−2·А−1
UnitSI.append({'T': {'Quantity': 'Magnetic field strength', 'Value':1,'Unit':'T', 'FormDim': ''}})
# Индуктивность	генри	henry	Гн	H	кг·м2·с−2·А−2
UnitSI.append({'H': {'Quantity': 'Inductance', 'Value':1,'Unit':'H', 'FormDim': ''}})
# Электрическая проводимость	сименс	siemens	См	S	Ом−1 = с3·А2·кг−1·м−2
UnitSI.append({'S': {'Quantity': 'Electrical conductance', 'Value':1,'Unit':'S', 'FormDim': ''}})
# Активность радиоактивного источника	беккерель	becquerel	Бк	Bq	с−1
UnitSI.append({'Bq': {'Quantity': 'Radioactivity (decays per unit time)', 'Value':1,'Unit':'Bq', 'FormDim': ''}})
# Поглощённая доза ионизирующего излучения	грей	gray	Гр	Gy	Дж/кг = м²/c²
UnitSI.append({'Gy': {'Quantity': 'Absorbed dose (of ionizing radiation)', 'Value':1,'Unit':'Gy', 'FormDim': ''}})
# Эффективная доза ионизирующего излучения	зиверт	sievert	Зв	Sv	Дж/кг = м²/c²
UnitSI.append({'Sv': {'Quantity': 'Equivalent dose (of ionizing radiation)', 'Value':1,'Unit':'Sv', 'FormDim': ''}})
# Активность катализатора	катал	katal	кат	kat	моль/с
UnitSI.append({'kat': {'Quantity': 'Catalytic activity', 'Value':1,'Unit':'kat', 'FormDim': ''}})



# Производные единицы измерения массы:
UnitSI.append({'g': {'Quantity': 'Mass', 'Value':0.001,'Unit':'kg', 'FormDim': 'M'}})









def fConvUnitSI(Var):
    """ Функция перевода размерности величины с внесистемной в систему СИ
    Convert Unit to SI"""
    for elem in UnitSI:
        if Var['Unit'] in elem.keys():
            Var['Value'] = Var['Value']*elem[Var['Unit']]['Value']
            Var['Unit'] = elem[Var['Unit']]['Unit']
    return Var
