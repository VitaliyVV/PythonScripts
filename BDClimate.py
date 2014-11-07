# -*- coding: utf-8 -*-
"""
Created on Мот Oct 20 08:20:36 2014
База данных по Климату
@author: Volovikov
"""


def fFindClimateSubRegion(vMT12, vMW, vMT5, vMH5):
    """Функция для определения климатического подрегиона"""
    SubRegion = 'None'
    if (vMT12 <= -32.0) and (4.0 <= vMT5 <= 19.0):
        SubRegion = 'IА'
    if (-28.0 <= vMT12 <= -14.0) and (12.0 <= vMT5 <= 21.0):
        SubRegion = 'IВ'
    if (-14.0 <= vMT12 <= -4.0) and (12.0 <= vMT5 <= 21.0):
        SubRegion = 'IIВ'
    if (-20.0 <= vMT12 <= -14.0) and (21.0 <= vMT5 <= 25.0):
        SubRegion = 'IIIА'
    if (-5.0 <= vMT12 <= 2.0) and (21.0 <= vMT5 <= 25.0):
        SubRegion = 'IIIБ'
    if (-14.0 <= vMT12 <= -5.0) and (21.0 <= vMT5 <= 25.0):
        SubRegion = 'IIIВ'
    if (-10.0 <= vMT12 <= 2.0) and (28.0 <= vMT5):
        SubRegion = 'IVА'
    if (0.0 <= vMT12 <= 2.0) and (25.0 <= vMT5 <= 28.0):
        SubRegion = 'IVВ'
    if (-15.0 <= vMT12 <= 0.0) and (25.0 < vMT5 < 28.0):
        SubRegion = 'IVГ'
    if (-32.0 <= vMT12 <= -14.0) and (10.0 <= vMT5 <= 20.0) and (vMH5 >= 75.0):
        SubRegion = 'IД'
    if (2.0 <= vMT12 <= 6.0) and (22.0 <= vMT5 <= 28.0) and (vMH5 >= 50.0):
        SubRegion = 'IVБ'
    if (vMT12 <= -28.0) and (vMW >= 5.0) and (0.0 <= vMT5 <= 13.0) and (vMH5 >= 75.0):
        SubRegion = 'IБ'
    if (-28.0 <= vMT12 <= -14.0) and (vMW >= 5.0) and (0.0 <= vMT5 <= 14.0) and (vMH5 >= 75.0):
        SubRegion = 'IГ'
    if (-14.0 <= vMT12 <= -4.0) and (vMW >= 5.0) and (8.0 <= vMT5 <= 12.0) and (vMH5 >= 75.0):
        SubRegion = 'IIА'
    if (-5.0 <= vMT12 <= -3.0) and (vMW >= 5.0) and (12.0 <= vMT5 <= 21.0) and (vMH5 >= 75.0):
        SubRegion = 'IIБ'
    if (-14.0 <= vMT12 <= -5.0) and (vMW >= 5.0) and (12.0 <= vMT5 <= 21.0) and (vMH5 >= 75.0):
        SubRegion = 'IIГ'
    return SubRegion

def fFindClimateRegion(varSubRegion):
    """Функция для определения климатического региона"""
    Region = 'None'
    for elem in ['IА','IБ','IВ','IГ','IД']:
        if varSubRegion == elem:
            Region = 'I'
    for elem in ['IIА','IIБ','IIВ','IIГ']:
        if varSubRegion == elem:
            Region = 'II'
    for elem in ['IIIА','IIIБ','IIIВ']:
        if varSubRegion == elem:
            Region = 'III'
    for elem in ['IVА','IVБ','IVВ','IVГ']:
        if varSubRegion == elem:
            Region = 'IV'
    return Region





Records = [{}]
# ID Города в базе данных
ID = 0
# Источник данных
Records[ID]['Source'] = 'СП 131.13330.2012 Строительная климатология.'.decode('utf-8')
# Наименование города
Records[ID]['City'] = 'Майкоп'.decode('utf-8')
# Географические координаты расположения города
Records[ID]['Latitude'] = 0.0
Records[ID]['Longitude'] = 0.0
Records[ID]['Rang'] = 0.0
# Данные холодного периода года
Records[ID]['ColdTime'] = {}

# Температура воздуха наиболее холодных суток, обеспеченностью 0,98, °С
Records[ID]['ColdTime']['TempCold92'] = -27.0
# Температура воздуха наиболее холодных суток, обеспеченностью 0,92, °С
Records[ID]['ColdTime']['TempCold98'] = -22.0
# Температура воздуха наиболее холодной пятидневки, обеспеченностью 0,98, °С
Records[ID]['ColdTime']['Temp5Cold92'] = -21.0
# Температура воздуха наиболее холодной пятидневки, обеспеченностью 0,92, °С
Records[ID]['ColdTime']['Temp5Cold98'] = -19.0
# Температура воздуха, обеспеченностью 0,94, °С
Records[ID]['ColdTime']['Temp94'] = -6.0
# Абсолютная минимальная температура воздуха, °С			
Records[ID]['ColdTime']['AbsMinTemp'] = -34.0
# Средняя суточная амплитуда температуры воздуха наиболее холодного месяца, °С
Records[ID]['ColdTime']['AmplTempCold'] = 9.0

# Продолжительность периода со средней суточной температурой воздуха ≤0°С, сут
Records[ID]['ColdTime']['DurMidTemp0'] = 40.0
# Cредняя температура воздуха, периода со средней суточной температурой воздуха ≤0°С, °С
Records[ID]['ColdTime']['MidTemp0'] = -1.0
# Продолжительность периода со средней суточной температурой воздуха ≤8°С, сут
Records[ID]['ColdTime']['DurMidTemp8'] = 148.0
# Cредняя температура воздуха, периода со средней суточной температурой воздуха ≤8°С, °С
Records[ID]['ColdTime']['MidTemp8'] = 2.3
# Продолжительность периода со средней суточной температурой воздуха ≤10°С, сут
Records[ID]['ColdTime']['DurMidTemp10'] = 169.0
# Cредняя температура воздуха, периода со средней суточной температурой воздуха ≤10°С, °С
Records[ID]['ColdTime']['MidTemp10'] = 3.1

# Средняя месячная относительная влажность воздуха наиболее холодного месяца, %
Records[ID]['ColdTime']['HumCold'] = 79.0
# Средняя месячная относительная влажность воздуха в 15 ч наиболее холодного холодного месяца, %
Records[ID]['ColdTime']['HumCold15'] = 72.0

# Количество осадков за ноябрь - март, мм
Records[ID]['ColdTime']['OsadkyNovMar'] = 276

# Преобладающее направление ветра за декабрь - февраль, 
Records[ID]['ColdTime']['WindDirDecFeb'] = 'Ю'.decode('utf-8')
# Максимальная из средних скоростей ветра по румбам за январь, м/с
Records[ID]['ColdTime']['MaxWindJan'] = 5.7
# Средняя скорость ветра, за период со средней суточной температурой воздуха ≤8°С, м/с
Records[ID]['ColdTime']['WindSpeed'] = 3.0


# Данные теплого периода года
Records[ID]['HotTime'] = {}

# Барометрическое давление, гПа
Records[ID]['HotTime']['Pressure'] = 990.0

# Температура воздуха, обеспеченностью 0,95, °С
Records[ID]['HotTime']['TempHot95'] = 26.6
# Температура воздуха, обеспеченностью 0,98, °С
Records[ID]['HotTime']['TempHot98'] = 30.6

#Средняя максимальная температура воздуха наиболее теплого месяца, °С
Records[ID]['HotTime']['MidMaxTempHot'] = 29.0
# Абсолютная максимальная температура воздуха, °С
Records[ID]['HotTime']['AbsMaxTemp'] = 41.0
# Средняя суточная амплитуда температуры воздуха наиболее теплого месяца, °С
Records[ID]['HotTime']['AmplTempHot'] = 12.8

# Средняя месячная относительная влажность воздуха наиболее теплого месяца, %
Records[ID]['HotTime']['HumHot'] = 67.0
# Средняя месячная относительная влажность воздуха в 15 ч наиболее теплого месяца, %
Records[ID]['HotTime']['HumHot15'] = 48.0

# Количество осадков за апрель - октябрь, мм
Records[ID]['HotTime']['OsadkyAprOct'] = 481.0
# Суточный максимум осадков, мм
Records[ID]['HotTime']['OsadkyMax'] = 88.0

# Преобладающее направление ветра за июнь - август, 
Records[ID]['HotTime']['WindDirJunAug'] = 'Ю'.decode('utf-8')
# Минимальная из средних скоростей ветра по румбам за июль, м/с
Records[ID]['HotTime']['MinWindJul'] = 2.1


# Данные по среднемесячным температурам и годовой температуре
Records[ID]['MidTemp'] = {}
Records[ID]['MidTemp']['Month'] = [-1.4, 0.3, 4.1, 11.3, 16.5, 19.7, 22.2, 21.9, 17.1, 11.2, 6.2, 1.4]
Records[ID]['MidTemp']['Year'] = 10.9


# Данные по среднемесячным температурам и годовому парциальному давлению водяного пара, гПа
Records[ID]['MidPressVapor'] = {}
Records[ID]['MidPressVapor']['Month'] = [4.6, 5.1, 5.9, 8.7, 12.5, 15.4, 17.4, 16.8, 13.5, 9.9, 7.6, 5.7]
Records[ID]['MidPressVapor']['Year'] = 10.3


Records[ID]['ClimateRegion'] = {}
Records[ID]['ClimateRegion']['Region'] = fFindClimateSubRegion(Records[ID]['MidTemp']['Month'][11], Records[ID]['ColdTime']['WindSpeed'], Records[ID]['MidTemp']['Month'][5], Records[ID]['HotTime']['HumHot']).decode('utf-8')
Records[ID]['ClimateRegion']['SubRegion'] = fFindClimateRegion(Records[ID]['ClimateRegion']['Region']).decode('utf-8')

# Зона солнечной радиации
Records[ID]['ZoneSolarRad'] = {}


# ID Города в базе данных
ID = ID + 1
Records.append({})
# Источник данных
Records[ID]['Source'] = 'СП 131.13330.2012 Строительная климатология.'.decode('utf-8')
# Наименование города
Records[ID]['City'] = 'Майкоп'.decode('utf-8')
# Географические координаты расположения города
Records[ID]['Latitude'] = 0.0
Records[ID]['Longitude'] = 0.0
Records[ID]['Rang'] = 0.0
# Данные холодного периода года
Records[ID]['ColdTime'] = {}

# Температура воздуха наиболее холодных суток, обеспеченностью 0,98, °С
Records[ID]['ColdTime']['TempCold92'] = -27.0
# Температура воздуха наиболее холодных суток, обеспеченностью 0,92, °С
Records[ID]['ColdTime']['TempCold98'] = -22.0
# Температура воздуха наиболее холодной пятидневки, обеспеченностью 0,98, °С
Records[ID]['ColdTime']['Temp5Cold92'] = -21.0
# Температура воздуха наиболее холодной пятидневки, обеспеченностью 0,92, °С
Records[ID]['ColdTime']['Temp5Cold98'] = -19.0
# Температура воздуха, обеспеченностью 0,94, °С
Records[ID]['ColdTime']['Temp94'] = -6.0
# Абсолютная минимальная температура воздуха, °С			
Records[ID]['ColdTime']['AbsMinTemp'] = -34.0
# Средняя суточная амплитуда температуры воздуха наиболее холодного месяца, °С
Records[ID]['ColdTime']['AmplTempCold'] = 9.0

# Продолжительность периода со средней суточной температурой воздуха ≤0°С, сут
Records[ID]['ColdTime']['DurMidTemp0'] = 40.0
# Cредняя температура воздуха, периода со средней суточной температурой воздуха ≤0°С, °С
Records[ID]['ColdTime']['MidTemp0'] = -1.0
# Продолжительность периода со средней суточной температурой воздуха ≤8°С, сут
Records[ID]['ColdTime']['DurMidTemp8'] = 148.0
# Cредняя температура воздуха, периода со средней суточной температурой воздуха ≤8°С, °С
Records[ID]['ColdTime']['MidTemp8'] = 2.3
# Продолжительность периода со средней суточной температурой воздуха ≤10°С, сут
Records[ID]['ColdTime']['DurMidTemp10'] = 169.0
# Cредняя температура воздуха, периода со средней суточной температурой воздуха ≤10°С, °С
Records[ID]['ColdTime']['MidTemp10'] = 3.1

# Средняя месячная относительная влажность воздуха наиболее холодного месяца, %
Records[ID]['ColdTime']['HumCold'] = 79.0
# Средняя месячная относительная влажность воздуха в 15 ч наиболее холодного холодного месяца, %
Records[ID]['ColdTime']['HumCold15'] = 72.0

# Количество осадков за ноябрь - март, мм
Records[ID]['ColdTime']['OsadkyNovMar'] = 276

# Преобладающее направление ветра за декабрь - февраль, 
Records[ID]['ColdTime']['WindDirDecFeb'] = 'Ю'.decode('utf-8')
# Максимальная из средних скоростей ветра по румбам за январь, м/с
Records[ID]['ColdTime']['MaxWindJan'] = 5.7
# Средняя скорость ветра, за период со средней суточной температурой воздуха ≤8°С, м/с
Records[ID]['ColdTime']['WindSpeed'] = 3.0


# Данные теплого периода года
Records[ID]['HotTime'] = {}

# Барометрическое давление, гПа
Records[ID]['HotTime']['Pressure'] = 990.0

# Температура воздуха, обеспеченностью 0,95, °С
Records[ID]['HotTime']['TempHot95'] = 26.6
# Температура воздуха, обеспеченностью 0,98, °С
Records[ID]['HotTime']['TempHot98'] = 30.6

#Средняя максимальная температура воздуха наиболее теплого месяца, °С
Records[ID]['HotTime']['MidMaxTempHot'] = 29.0
# Абсолютная максимальная температура воздуха, °С
Records[ID]['HotTime']['AbsMaxTemp'] = 41.0
# Средняя суточная амплитуда температуры воздуха наиболее теплого месяца, °С
Records[ID]['HotTime']['AmplTempHot'] = 12.8

# Средняя месячная относительная влажность воздуха наиболее теплого месяца, %
Records[ID]['HotTime']['HumHot'] = 67.0
# Средняя месячная относительная влажность воздуха в 15 ч наиболее теплого месяца, %
Records[ID]['HotTime']['HumHot15'] = 48.0

# Количество осадков за апрель - октябрь, мм
Records[ID]['HotTime']['OsadkyAprOct'] = 481.0
# Суточный максимум осадков, мм
Records[ID]['HotTime']['OsadkyMax'] = 88.0

# Преобладающее направление ветра за июнь - август, 
Records[ID]['HotTime']['WindDirJunAug'] = 'Ю'.decode('utf-8')
# Минимальная из средних скоростей ветра по румбам за июль, м/с
Records[ID]['HotTime']['MinWindJul'] = 2.1


# Данные по среднемесячным температурам и годовой температуре
Records[ID]['MidTemp'] = {}
Records[ID]['MidTemp']['Month'] = [-1.4, 0.3, 4.1, 11.3, 16.5, 19.7, 22.2, 21.9, 17.1, 11.2, 6.2, 1.4]
Records[ID]['MidTemp']['Year'] = 10.9


# Данные по среднемесячным температурам и годовому парциальному давлению водяного пара, гПа
Records[ID]['MidPressVapor'] = {}
Records[ID]['MidPressVapor']['Month'] = [4.6, 5.1, 5.9, 8.7, 12.5, 15.4, 17.4, 16.8, 13.5, 9.9, 7.6, 5.7]
Records[ID]['MidPressVapor']['Year'] = 10.3


Records[ID]['ClimateRegion'] = {}
Records[ID]['ClimateRegion']['Region'] = fFindClimateSubRegion(Records[ID]['MidTemp']['Month'][11], Records[ID]['ColdTime']['WindSpeed'], Records[ID]['MidTemp']['Month'][5], Records[ID]['HotTime']['HumHot']).decode('utf-8')
Records[ID]['ClimateRegion']['SubRegion'] = fFindClimateRegion(Records[ID]['ClimateRegion']['Region']).decode('utf-8')

# Зона солнечной радиации
Records[ID]['ZoneSolarRad'] = {}




#
# Краткое добавление строчки в базу
#
## ID Города в базе данных
#ID = ID+1
#Records.append(
#{'Source': 'СП 131.13330.2012 Строительная климатология.'.decode('utf-8'),
#'City' : 'Майкоп'.decode('utf-8'),
#'Latitude' : 0.0,
#'Longitude' : 0.0,
#'Rang' : 0.0,
#'ColdTime': {
#    'TempCold92' : -27.0,
#    'TempCold98' : -22.0,
#    'Temp5Cold92' : -21.0,
#    'Temp5Cold98' : -19.0,
#    'Temp94' : -6.0,
#    'AbsMinTemp' : -34.0,
#    'AmplTempCold' : 9.0,
#    'DurMidTemp0' : 40.0,
#    'MidTemp0' : -1.0,
#    'DurMidTemp8' : 148.0,
#    'MidTemp8' : 2.3,
#    'DurMidTemp10': 169.0,
#    'MidTemp10' : 3.1,
#    'HumCold' : 79.0,
#    'HumCold15' : 72.0,
#    'OsadkyNovMar' : 276,
#    'WindDirDecFeb' : 'Ю'.decode('utf-8'),
#    'MaxWindJan' : 5.7,
#    'WindSpeed' : 3.0
#    },
#'HotTime' : {
#    'Pressure' : 990.0,
#    'TempHot95' : 26.6,
#    'TempHot98' : 30.6,
#    'MidMaxTempHot' : 29.0,
#    'AbsMaxTemp' : 41.0,
#    'AmplTempHot' : 12.8,
#    'HumHot' : 67.0,
#    'HumHot15' : 48.0,
#    'OsadkyAprOct' : 481.0,
#    'OsadkyMax' : 88.0,
#    'WindDirJunAug' : 'Ю'.decode('utf-8'),
#    'MinWindJul' : 2.1
#    },
#'MidTemp' : {
#    'Month' : [-1.4, 0.3, 4.1, 11.3, 16.5, 19.7, 22.2, 21.9, 17.1, 11.2, 6.2, 1.4],
#    'Year' : 10.9
#    },
#'MidPressVapor' : {
#    'Month' : [4.6, 5.1, 5.9, 8.7, 12.5, 15.4, 17.4, 16.8, 13.5, 9.9, 7.6, 5.7],
#    'Year' : 10.3
#    },
#'ZoneSolarRad' : {}
#})
#
#'ClimateRegion' : {
#    'Region' : fFindClimateSubRegion(Records[ID]['MidTemp']['Month'][11], Records[ID]['ColdTime']['WindSpeed'], Records[ID]['MidTemp']['Month'][1], Records[ID]['HotTime']['HumHot']).decode('utf-8'),
#    'SubRegion' : fFindClimateRegion(Records[ID]['ClimateRegion']['Region']).decode('utf-8')
#    },
#






Records1 = [{}]
# Данные по солнечной радиации
Records1[0]['SolarRad'] = {}
# Данные по горизонтальной солнечной радиации
Records1[0]['SolarRad']['Goriz'] = {}
# Данные по вертикальной солнечной радиации
Records1[0]['SolarRad']['Vert'] = {}



def fViewSolarRadiation():
    SolarRad = {}
    return SolarRad




# Шляться по БД

def fShowRecords(varCity):
    """ Показать запись базы данных """
    for elem in Records:
        if (varCity == elem['City']):
            return elem
