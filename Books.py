# -*- coding: utf-8 -*-
from xlpython import *
import numpy
#import openpyxl


"""
Created on 10-11-2015
# Функции к EXCELL
@author: Volovikov
"""

"""
Список литературы:
0. Различные справочники и справочные данные
1. Каталог трубчатые печи
2. РТМ 26-02-67-84 Методика расчета на прочность элементов печей
3. РТМ 26-02-40-77 Тепловой расчет трубчатых печей. Нормативный метод
4. Расчет воздухоподогревателей и других теплообменников


Открытые и для себя в том числе библиотеки работы
с теплофизикой веществ и их вызов
1. CoolProp (http://www.coolprop.org/
https://github.com/CoolProp/CoolProp)
2. Termo (https://github.com/CalebBell/thermo)


Вызов:
1. 
import CoolProp
PropsSI('D', 'T', 298.15, 'P', 101325, 'Nitrogen')
2. 
>>> import thermo
>>>tol = thermo.Chemical('toluene')
>>>tol.Tm, tol.Tb, tol.Tc
(179.2, 383.75, 591.75)
>>> tol.rho, tol.Cp, tol.k, tol.mu
(862.2380125827527, 1706.0746129119084, 0.13034801424538045, 0.0005521951637285534)



"""


@xlfunc
def f_b_000_Interpolate(x,xp,yp):
  '''Linear interpolation one variable from two Exell vectors'''
  Rez = numpy.interp(x,xp,yp)
  return Rez

@xlfunc
def f_b_000_Interpolate2D(x1,x2,VY1,VY2,MZ):
  '''Linear interpolation 2 variable from two Exell vectors and matrix'''
  Y1Rez = []
  for ind,elem in enumerate(VY1):
    Y1Rez.append(numpy.interp(x2,VY2[ind],MZ[ind]))
  Rez = numpy.interp(x1,VY1,Y1Rez)
  return Rez


@xlfunc
def f_b_000_S_perehod(a,b,h,d):
  '''S_perehod'''
  h1 = (h*h+(b-d)*(b-d)*0.25)**0.5
  s1 = 0.5*a*h1
  h2 = (h*h+0.25*(a-d)*(a-d))**0.5
  s2 = 0.5*b*h2
  aa1 = (0.25*b*b+h2*h2)**0.5
  bb1 = (0.25*a*a+h1*h1)**0.5
  cc1 = numpy.pi*d*0.25
  p = (aa1+bb1+cc1)*0.5
  s3 = (p*(p-aa1)*(p-bb1)*(p-cc1))**0.5  
  Rez = 2.0*s1+2.0*s2+4.0*s3
  return Rez

@xlfunc
def f_b_000_S_cylindr(d,h):
  '''S_cilindr'''
  Rez = numpy.pi*d*(h+0.5*d)
  return Rez

@xlfunc
def f_b_000_V_cylindr(d,h):
  '''V_cilindr'''
  Rez = 0.25*numpy.pi*d*d*h
  return Rez

@xlfunc
def f_b_000_eval(Rez):
  '''Eval python exspresions'''
  return str(eval(str(Rez)))
 









# Книга 1 - Каталог трубчатые печи

# 
@xlfunc
def f_b_001_f_01_Phi3(qf,qt):
  """Phi3 """  
  Rez = qf/qt
  return Rez

@xlfunc
def f_b_001_f_02_EtaN(Phi1,Phi2,Phi3):
  """EtaN """  
  Rez = Phi1*Phi2*Phi3
  return Rez

@xlfunc
def f_b_001_f_03_EtaER(Hx,F,EtaN):
  """EtaER """  
  Rez = Hx*EtaN/F
  return Rez

@xlfunc
def f_b_001_f_04_DzetaR(EtaER):
  """DzetaR """  
  Rez = 1/EtaER
  return Rez

@xlfunc
def f_b_001_f_05_F(D,ro,w):
  """F, m2 """  
  Rez = D/(ro*w)
  return Rez

@xlfunc
def f_b_001_f_06_W(D,ro,d,n):
  """W, m/s """  
  Rez = D/(ro*n*0.25*d*d*numpy.pi)
  return Rez
  
@xlfunc
def f_b_001_f_07_ir(i2,Qp,D,tp,tyx):
  """ir,  """  
  Rez = i2 - Qp*(2000.0-0.98*tp)/(2000.0-1.05*tyx)/D
  return Rez

@xlfunc
def f_b_001_f_08_qf(qfs,Phi1,Phi1s,Phi2,Phi2s,Phi3,Phi3s):
  """qf,  """  
  Rez = qfs*Phi1*Phi2*Phi3/(Phi1s*Phi2s*Phi3s)
  return Rez

@xlfunc
def f_b_001_f_09_OtnPhi3(qd1,qd2,a):
  """Phi3/Phi3s"""  
  Rez = 0.5*(qd1+qd2)*a/qd2
  return Rez

@xlfunc
def f_b_001_f_10_qd1(Teta_dop,Tay_p,Alfa_p,Phi1,Phi2):
  """qd1"""  
  Rez = (Teta_dop-Tay_p)*Alfa_p*Phi1*Phi2
  return Rez

@xlfunc
def f_b_001_f_11_qd2(Teta_dop,Tay_2,Alfa_2,Phi1,Phi2):
  """qd2"""  
  Rez = (Teta_dop-Tay_2)*Alfa_2*Phi1*Phi2
  return Rez

@xlfunc
def f_b_001_f_12_Tp(Psi,Cs,Hp,Hs,qf,qp,Teta):
  """Tp, K"""  
  Rez = 100.0*((Hp/Hs/Cs*(qf-qp)+(Teta/100.0)**4.0)/Psi)**(0.25)
  return Rez

@xlfunc
def f_b_001_f_13_Psi(lf,lt):
  """Psi"""  
  Rez = 1.4-0.3*lf/lt
  return Rez

@xlfunc
def f_b_001_f_14_Psi(lf,lt):
  """Psi"""  
  Rez = 1.55-0.3*lf/lt
  return Rez

@xlfunc
def f_b_001_f_15_Psi(lf,lt):
  """Psi"""  
  Rez = 1.45-0.3*lf/lt
  return Rez

@xlfunc
def f_b_001_f_16_qp(Alfak,Psik,Tp,Teta):
  """qp"""  
  Rez = Alfak*(Psik*Tp-Teta)
  return Rez

@xlfunc
def f_b_001_f_17_Alfak(a,Tp,Teta):
  """Alfak"""  
  Rez = a*(Tp-Teta)**0.25
  return Rez

@xlfunc
def f_b_001_f_18_TetaN(TaySr,qp,Alfa2,Delta3,Lambda3):
  """TetaN, K"""  
  Rez = TaySr+273.15+qp/Alfa2+qp*Delta3/Lambda3
  return Rez
  
@xlfunc
def f_b_001_f_19_TaySr(Tay1,Tay2):
  """TaySr, K"""  
  Rez = 0.5*(Tay1+Tay2)
  return Rez


# Книга 2 - РТМ 26-02-67-84 Методика расчета на прочность элементов печей

@xlfunc
def f_b_002_f_01_SrTube(P,Dn,Sigma):
  """Sr, mm or m"""  
  Rez = P*Dn/(2.0*Sigma+P)
  return Rez
  
@xlfunc
def f_b_002_f_02_Sisp(Sr,f,c1,c2):
  """Sisp, mm or m"""  
  Rez = Sr+f*c1+c2
  return Rez
  
@xlfunc
def f_b_002_f_03_Smin(Dn):
  """Smin, mm"""  
  Rez = numpy.interp(Dn,[73.0,89.0,102.0,108.0,114.0,121.0,127.0,159.0,168.0,219.0,273.0,325.0],[4.5,5.0,5.0,5.0,5.5,5.5,5.5,6.0,6.0,7.0,8.0,8.0])
  return Rez
  
@xlfunc
def f_b_002_f_04_f(T,TypeStile):
  """Check and calculate f - not release!!! """  
  Rez = 1.0
  return Rez  

@xlfunc
def f_b_002_f_05_Y(RDn):
  """Smin, mm"""  
  Rez = numpy.interp(RDn,[1.0,1.5,2.0,3.0,4.0,5.0,6.0,7.0],[1.5,1.25,1.17,1.1,1.07,1.06,1.05,1.04])
  return Rez

@xlfunc
def f_b_002_f_06_SrOtv(P,Dn,Sigma,Y):
  """Sr otvod"""  
  Rez = P*Dn*Y/(2.0*Sigma+P)
  return Rez    

@xlfunc
def f_b_002_f_07_DeltaRast(Dvn,b,S,c):
  """DeltaRast"""  
  Rez = 1.0/(1.0+(b*b/(Dvn*(S-c))))
  return Rez

@xlfunc
def f_b_002_f_08_SrRast(P,Dn,Sigma,Y,DeltaRast):
  """Sr otvod"""  
  Rez = P*Dn*Y/(2.0*Sigma*(1+DeltaRast)+P)
  return Rez    

@xlfunc
def f_b_002_f_09_STubeOtvRast(P,Dn,Sigma,Y,f,b,Sisp,c,c1,c2):
  """S
    P - presure, MPa
    Dn - Diameter, mm
    Sigma - MPa,
    Y - paramert,
    f - parametr, = 1.0,
    b - shirina rastochki, mm,
    Sisp - ispolnitelnaya tolshina stenki otvoda, mm
    c - c1+c2
  """  
  Rez = P*Dn*Y/(2.0*Sigma*(1+1.0/(1.0+(b*b/((Dn-2*Sisp)*(Sisp-c1-c2)))))+P)+f*c1+c2
  return Rez

# Книга 3 - РТМ 26-02-40-77 Тепловой расчет трубчатых печей. Нормативный метод

@xlfunc
def f_b_003_f_02_DensityFuelGas(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2,
                                H2,H2S,O2,N2,Ar,H2O,CO,CO2,SO2):
  '''Density Fuel Gas, кг/м3'''
  # Таблица плотностей газов [3]:
  part1 = (0.536*1.0+0.045*4.0)*CH4+(0.536*2.0+0.045*6.0)*C2H6
  part2 = (0.536*3.0+0.045*8.0)*C3H8+(0.536*4.0+0.045*10.0)*C4H10
  part3 = (0.536*5.0+0.045*12.0)*C5H12+(0.536*6.0+0.045*14.0)*C6H14
  part4 = (0.536*6.0+0.045*12.0)*C6H12+(0.536*6.0+0.045*6.0)*C6H6
  part5 = (0.536*2.0+0.045*4.0)*C2H4+(0.536*3.0+0.045*6.0)*C3H6
  part6 = (0.536*4.0+0.045*8.0)*C4H8+(0.536*5.0+0.045*10.0)*C5H10
  part7 = (0.536*4.0+0.045*6.0)*C4H6+(0.536*2.0+0.045*2.0)*C2H2
  part8 = 0.0899*H2+1.53*H2S+1.43*O2+1.25*N2+1.7837*Ar+0.804*H2O
  part9 = 1.25*CO+1.96*CO2+2.926*SO2
  Rez = 0.01*(part1+part2+part3+part4+part4+part5+part6+part7+part8+part9)
  return Rez
  
@xlfunc
def f_b_003_f_03_QnrFuelGas(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2,
                                H2,H2S,O2,N2,Ar,H2O,CO,CO2,SO2):
  '''Qnr Fuel Gas, Дж/м3'''
  Rez = (0.01*(23.37*H2S+12.64*CO+10.79*H2+35.88*CH4+64.36*C2H6+93.18*C3H8
  +123.15*C4H10+156.63*C5H12+59.06*C2H4+86.0*C3H6+113.51*C4H8+140.38*C6H6))*1.0e6
  return Rez

@xlfunc
def f_b_003_f_03_QnrFuelOil(Crab,Hrab,Orab,Srab):
  '''Qnr Fuel Oil, Дж/кг'''
  Rez = (339.13*Crab+1256.0*Hrab-108.86*(Orab-Srab))*1000.0
  return Rez

@xlfunc
def f_b_003_f_04_V0PCFuelOil(Crab,Hrab,Orab,Srab):
  '''V0PCFuelOil, м3 дымовых газов на 1 кг топлива'''
  Rez = (0.0889*(Crab+0.375*Srab)+0.265*Hrab-0.0333*Orab)
  return Rez

@xlfunc
def f_b_003_f_05_L0PCFuelOil(Crab,Hrab,Orab,Srab):
  '''L0PCFuelOil, кг дымовых газов на 1 кг топлива'''
  Rez = (0.1115*(Crab+0.375*Srab)+0.342*Hrab-0.0431*Orab)
  return Rez

@xlfunc
def f_b_003_f_06_VRO20PCFuelOil(Crab,Srab):
  ''' Объем трехатомных газов, м3/кг'''
  Rez = 1.866*(Crab+0.375*Srab)*0.01
  return Rez

@xlfunc
def f_b_003_f_07_GRO20PCFuelOil(Crab,Srab):
  ''' Масса трехатомных газов, кг/кг'''
  Rez = (3.76*Crab+2.0*Srab)*0.01
  return Rez

@xlfunc
def f_b_003_f_08_V0N2PCFuelOil(V0PCFuelOil,Nrab):
  ''' Теоретический объем азота, м3/кг'''
  Rez = 0.79*V0PCFuelOil+(0.008*Nrab)
  return Rez

@xlfunc
def f_b_003_f_09_G0N2PCFuelOil(L0PCFuelOil,Nrab):
  ''' Теоретическая масса азота, кг/кг'''
  Rez = 0.769*L0PCFuelOil+(0.01*Nrab)
  return Rez

@xlfunc
def f_b_003_f_10_V0H2OPCFuelOil(V0PCFuelOil,Hrab,Nrab,GfWapor):
  ''' Теоретический объем водяных паров, м3/кг'''
  Rez = (0.111*Hrab+0.0124*Nrab)+0.0161*V0PCFuelOil+1.24*GfWapor
  return Rez

@xlfunc
def f_b_003_f_11_G0H2OPCFuelOil(L0PCFuelOil,Hrab,Nrab,GfWapor):
  ''' Теоретическая масса водяных паров, кг/кг'''
  Rez = (0.0894*Hrab+0.01*Nrab)+0.01*L0PCFuelOil+GfWapor
  return Rez

@xlfunc
def f_b_003_f_12_VH2OPCFuelOil(V0H2OPCFuelOil,V0PCFuelOil,AlfaMax):
  ''' Объем водяных паров при избытке воздуха, м3/кг'''
  Rez = V0H2OPCFuelOil+0.0161*(AlfaMax-1.0)*V0PCFuelOil
  return Rez

@xlfunc
def f_b_003_f_13_GH2OPCFuelOil(G0H2OPCFuelOil,L0PCFuelOil,AlfaMax):
  ''' Масса водяных паров при максимальном избытке воздуха, кг/кг'''
  Rez = G0H2OPCFuelOil+0.01*(AlfaMax-1.0)*L0PCFuelOil
  return Rez

@xlfunc
def f_b_003_f_14_VPCFuelOil(VRO20PCFuelOil,V0N2PCFuelOil,VH2OPCFuelOil,V0PCFuelOil,AlfaMax):
  ''' Объем дымовых газов при максимальном избытке воздуха, м3/кг'''
  Rez = VRO20PCFuelOil+V0N2PCFuelOil+VH2OPCFuelOil+(AlfaMax-1.0)*V0PCFuelOil
  return Rez

@xlfunc
def f_b_003_f_15_GPCFuelOil(GRO20PCFuelOil,G0N2PCFuelOil,GH2OPCFuelOil,L0PCFuelOil,Arab,V0PCFuelOil,AlfaMax):
  ''' Количество дымовых газов при максимальном избытке воздуха, кг/кг'''
  Rez = GRO20PCFuelOil+G0N2PCFuelOil+GH2OPCFuelOil+(AlfaMax-1.0)*L0PCFuelOil
  return Rez

@xlfunc
def f_b_003_f_16_GPCFuelOil(AlfaMax,Arab,V0PCFuelOil,GfSteam):
  ''' Количество дымовых газов при максимальном избытке воздуха, кг/кг'''
  Rez = 1.0-Arab/100.0+1.306*AlfaMax*V0PCFuelOil+GfSteam
  return Rez

@xlfunc
def f_b_003_f_17_AlfaPCMaxGOST(TypeFuel,TypeTraction):
  ''' Коэффициент избытка воздуха максимальный по ГОСТ Р
  TypeFuel: 1 - Gas; 2 - Oil.
  TypeTraction: 1 - Natural; 2 - Force.'''
  if TypeFuel == 1:
    if TypeTraction == 1:
      Rez = 1.2
    if TypeTraction == 2:
      Rez = 1.15
  if TypeFuel == 2:
    if TypeTraction == 1:
      Rez = 1.25
    if TypeTraction == 2:
      Rez = 1.2
  return Rez

@xlfunc
def f_b_003_f_18_MuAshPCFuelOil(Arab,Aun,GPCFuelOil):
  ''' Концентрация золы в продуктах сгорания, кг/кг'''
  Rez = Arab*Aun/(100.0*GPCFuelOil)
  return Rez

@xlfunc
def f_b_003_f_19_V0PCFuelGas(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2,
                                H2,H2S,O2,CO):
  '''  # Теоретическое количество сухого воздуха, необходимого для полного
  # сгорания топлива (коэффициент избытка воздуха a=1)
  #V0PCFuelGas, м3 дымовых газов на 1 м3 топлива'''
  part1 = 0.5*CO+0.5*H2+1.5*H2S-O2
  part2 = 2.0*CH4+3.5*C2H6+5.0*C3H8+6.5*C4H10+8.0*C5H12+9.5*C6H14+9.0*C6H12
  part3 = 7.5*C6H6+3.0*C2H4+4.5*C3H6+6.0*C4H8+7.5*C5H10+5.5*C4H6+2.5*C2H2
  Rez = 0.0476*(part1+part2+part3)
  return Rez

@xlfunc
def f_b_003_f_20_VRO20PCFuelGas(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2,
                                H2,H2S,CO,CO2,SO2):
  '''  # Объем трехатомных газов, м3/м3'''
  part1 = H2+H2S+CO+CO2+SO2
  part2 = CH4+2.0*C2H6+3.0*C3H8+4.0*C4H10+5.0*C5H12+6.0*C6H14+6.0*C6H12
  part3 = 6.0*C6H6+2.0*C2H4+3.0*C3H6+4.0*C4H8+5.0*C5H10+4.0*C4H6+2.0*C2H2
  Rez = 0.01*(part1+part2+part3)
  return Rez

@xlfunc
def f_b_003_f_21_V0N2PCFuelGas(V0PCFuelGas,N2):
  '''  # Теоретический объем азота, м3/м3'''
  Rez = 0.79*V0PCFuelGas+(0.001*N2)
  return Rez

@xlfunc
def f_b_003_f_22_V0H2OPCFuelGas(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2,
                                H2,H2S,H2O,
                                dGas,V0PCFuelGas):
  '''  # Теоретический объем водяных паров, м3/м3'''
  part1 = H2S+H2+0.124*dGas+H2O
  part2 = 2.0*CH4+3.0*C2H6+4.0*C3H8+5.0*C4H10+6.0*C5H12+7.0*C6H14+6.0*C6H12
  part3 = 3.0*C6H6+2.0*C2H4+3.0*C3H6+4.0*C4H8+5.0*C5H10+6.0*C4H6+C2H2
  Rez = 0.01*(part1+part2+part3)+0.0161*V0PCFuelGas
  return Rez

@xlfunc
def f_b_003_f_23_GPCFuelGas(GRO20PCFuelGas,G0N2PCFuelGas,GH2OPCFuelGas,L0PCFuelGas,Alfa):
  ''' Количество дымовых газов при максимальном избытке воздуха, кг/кг'''
  Rez = GRO20PCFuelGas+G0N2PCFuelGas+GH2OPCFuelGas+(Alfa-1.0)*L0PCFuelGas
  return Rez

@xlfunc
def f_b_003_f_24_GPCFuelGas2(dGas, roGas, V0, Alfa):
  ''' Количество дымовых газов при максимальном избытке воздуха, кг/кг'''
  Rez = 1+0.001*dGas*roGas+1.306*Alfa*V0/roGas
  return Rez

@xlfunc
def f_b_003_f_25_GPCFuelGas3(dGas, roGas, V0, Alfa):
  ''' Количество дымовых газов при максимальном избытке воздуха, кг/кг'''
  Rez = roGas+0.001*dGas+1.306*Alfa*V0
  return Rez

@xlfunc
def f_b_003_f_26_IAir(V0,t):
  ''' Энтальпия воздуха, кДж/м3 (кДж/кг топл)'''
  # Энтальпия 1 м3 воздуха, кДж/м3 (кДж/кг топл)
  ctAir = numpy.interp(t,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0],
                     [-132.7, 0.0, 132.7, 267.0, 403.0, 542.0, 685.0, 830.0, 979.0,1129.0,1283.0, 1438.0, 1595.0, 1754.0, 1914.0, 2076.0, 2239.0, 2403.0, 2567.0, 2732.0, 2899.0, 3066.0, 3234.0, 3402.0, 3571.0, 3740.0, 3910.0])
  Rez = V0*ctAir
  return Rez

@xlfunc
def f_b_003_f_27_IAir1(L0,t):
  ''' Энтальпия воздуха, кДж/кг'''
  # Энтальпия 1 кг воздуха, кДж/кг
  ct1Air = numpy.interp(t,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0],
                     [-102.1, 0.0, 102.1, 206.0, 312.0, 419.0, 529.0, 642.0, 758.0, 874.0, 991.0, 1111.0, 1234.0, 1357.0, 1480.0, 1606.0, 1732.0, 1859.0, 1985.0, 2111.0, 2241.0, 2370.0, 2500.0, 2630.0])
  Rez = L0*ct1Air
  return Rez

@xlfunc
def f_b_003_f_28_IProductCombution(VRO2,V0N2,V0H2O,V0,Tetta,Alfa):
  ''' Энтальпия продуктов сгорания, кДж/м3 (кДж/кг топл)'''
  ctAir = 1
  # Энтальпия 1 м3 углекислого газа, кДж/м3
  ctCO2 = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0],
                     [-171.7, 0.0, 171.7, 360.0, 563.0, 776.0, 999.0,1231.0,1469.0,1712.0,1961.0, 2213.0, 2458.0, 2717.0, 2977.0, 3239.0, 3503.0, 3769.0, 4036.0, 4305.0, 4574.0, 4844.0, 5115.0, 5386.0, 5658.0, 5930.0, 6203.0])

  # Энтальпия 1 м3 азота, кДж/м3 (кДж/кг топл)
  ctN2 = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0],
                     [-130.1, 0.0, 130.1, 261.0, 394.0, 529.0, 667.0, 808.0, 952.0,1098.0,1247.0, 1398.0, 1551.0, 1705.0, 1853.0, 2009.0, 2166.0, 2324.0, 2484.0, 2644.0, 2804.0, 2965.0, 3127.0, 3289.0, 3452.0, 3615.0, 3778.0])

  # Энтальпия 1 м3 водяных паров, кДж/м3 (кДж/кг топл)
  ctH2O = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0],
                     [-150.5, 0.0, 150.5, 304.0, 463.0, 626.0, 795.0, 969.0,1149.0,1334.0,1526.0, 1723.0, 1925.0, 2132.0, 2344.0, 2559.0, 2779.0, 3002.0, 3229.0, 3458.0, 3690.0, 3926.0, 4163.0, 4402.0, 4643.0, 4888.0, 5132.0])

  # Энтальпия 1 м3 воздуха, кДж/м3 (кДж/кг топл)
  ctAir = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0],
                     [-132.7, 0.0, 132.7, 267.0, 403.0, 542.0, 685.0, 830.0, 979.0,1129.0,1283.0, 1438.0, 1595.0, 1754.0, 1914.0, 2076.0, 2239.0, 2403.0, 2567.0, 2732.0, 2899.0, 3066.0, 3234.0, 3402.0, 3571.0, 3740.0, 3910.0])

  Rez = VRO2*ctCO2+V0N2*ctN2+V0H2O*ctH2O+V0*ctAir*(Alfa-1.0)
  return Rez

@xlfunc
def f_b_003_f_29_IProductCombution1(LRO2,L0N2,L0H2O,L0,Tetta,Alfa):
  ''' Энтальпия продуктов сгорания, кДж/кг'''
  # Энтальпия 1 кг углекислого газа, кДж/кг
  ct1CO2 = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0],
                     [ -86.6, 0.0,  86.6, 182.0, 285.0, 393.0, 507.0, 623.0, 744.0, 868.0, 994.0, 1122.0, 1252.0, 1384.0, 1517.0, 1651.0, 1779.0, 1920.0, 2056.0, 2193.0, 2329.0, 2468.0, 2601.0, 2745.0])

  # Энтальпия 1 кг азота, кДж/кг
  ct1N2 = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0],
                     [-104.0, 0.0, 104.0, 208.0, 314.0, 422.0, 531.0, 643.0, 757.0, 875.0, 995.0, 1115.0, 1236.0, 1357.0, 1481.0, 1608.0, 1732.0, 1859.0, 1987.0, 2114.0, 2244.0, 2372.0, 2503.0, 2633.0])

  # Энтальпия 1 кг водяных паров, кДж/кг
  ct1H2O = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0],
                     [-187.6, 0.0, 187.6, 378.0, 575.0, 778.0, 988.0,1201.0,1425.0,1660.0,1893.0, 2143.0, 2393.0, 2647.0, 2913.0, 3178.0, 3453.0, 3729.0, 4010.0, 4296.0, 4583.0, 4878.0, 5170.0, 5466.0])

  # Энтальпия 1 кг воздуха, кДж/кг
  ct1Air = numpy.interp(Tetta,
                     [-100.0, 0.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0],
                     [-102.1, 0.0, 102.1, 206.0, 312.0, 419.0, 529.0, 642.0, 758.0, 874.0, 991.0, 1111.0, 1234.0, 1357.0, 1480.0, 1606.0, 1732.0, 1859.0, 1985.0, 2111.0, 2241.0, 2370.0, 2500.0, 2630.0])

  Rez = LRO2*ct1CO2+L0N2*ct1N2+L0H2O*ct1H2O+L0*ct1Air*(Alfa-1.0)
  return Rez

@xlfunc
def f_b_003_f_30_cFuelGas(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2,
                                H2,H2S,O2,N2,Ar,H2O,CO,CO2,SO2,dGas,t):
  '''Теплоемкость газового топлива, отнесенная к 1м3 сухого газа, кДж/(м3*К)'''
  # Таблица теплоемкостей газов [3]:
  cCH4 = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0],
                     [1.548,1.642,1.757,1.883,2.012,2.138,2.261,2.38,2.495,2.603,2.7])
  cC2H6 = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0],
                     [2.21,2.495,2.776,3.046,3.308,3.557,3.776,3.985,4.183,4.363,4.529])

  cC3H8 = numpy.interp(t,
                     [0.0,1000.0],
                     [3.049,6.462])
  cC4H10 = numpy.interp(t,
                     [0.0,1000.0],
                     [4.129,8.402])
  cC5H12 = numpy.interp(t,
                     [0.0,1000.0],
                     [5.13,10.346])
  # Приблизительно!!!
  cC6H14 = numpy.interp(t,
                     [0.0,1000.0],
                     [5.13,10.346])
  # Приблизительно!!!                    
  cC6H12 = numpy.interp(t,
                     [0.0,1000.0],
                     [5.13,10.346])
  # Приблизительно!!!
  cC6H6 = numpy.interp(t,
                     [0.0,1000.0],
                     [5.13,10.346])

  # Приблизительно!!!
  cC2H4 = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0],
                     [2.21,2.495,2.776,3.046,3.308,3.557,3.776,3.985,4.183,4.363,4.529])

  # Приблизительно!!!
  cC3H6 = numpy.interp(t,
                     [0.0,1000.0],
                     [3.049,6.462])
  # Приблизительно!!!
  cC4H8 = numpy.interp(t,
                     [0.0,1000.0],
                     [4.129,8.402])
  # Приблизительно!!!
  cC5H10 = numpy.interp(t,
                     [0.0,1000.0],
                     [5.13,10.346])
  # Приблизительно!!!
  cC4H6 = numpy.interp(t,
                     [0.0,1000.0],
                     [4.129,8.402])
  # Приблизительно!!!
  cC2H2 = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0],
                     [2.21,2.495,2.776,3.046,3.308,3.557,3.776,3.985,4.183,4.363,4.529])

  cH2 = numpy.interp(t,
                     [0.0,1000.0],
                     [1.278,1.328])

  cH2S = numpy.interp(t,
                     [0.0,1000.0],
                     [1.508,1.85])

  cO2 = numpy.interp(t,
                     [0.0,1000.0],
                     [1.3069,1.5909])

  cN2 = numpy.interp(t,
                     [0.0,2300.0],
                     [1.2955,1.5021])
  # Приблизительно!!!
  cAr = numpy.interp(t,
                     [0.0,2300.0],
                     [1.2955,1.5021])

  cH2O = numpy.interp(t,
                     [0.0,2300.0],
                     [1.4954,2.0204])

  cCO = numpy.interp(t,
                     [0.0,1000.0],
                     [1.3,1.411])

  cCO2 = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0],
                     [1.6010,1.7016,1.7887,1.8641,1.9312,1.9902,2.0426,2.09,2.1327,2.1708,2.2052,2.2366,2.2655,2.2915,2.3154,2.3372,2.3573,2.3761,2.3933,2.4092,2.4239,2.4377,2.4503,2.462])

  # Приблизительно!!!
  cSO2 = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0],
                     [1.6010,1.7016,1.7887,1.8641,1.9312,1.9902,2.0426,2.09,2.1327,2.1708,2.2052,2.2366,2.2655,2.2915,2.3154,2.3372,2.3573,2.3761,2.3933,2.4092,2.4239,2.4377,2.4503,2.462])


  part1 = cCH4*CH4+cC2H6*C2H6+cC3H8*C3H8+cC4H10*C4H10
  part2 = cC5H12*C5H12+cC6H14*C6H14+cC6H12*C6H12+cC6H6*C6H6
  part3 = cC2H4*C2H4+cC3H6*C3H6+cC4H8*C4H8+cC5H10*C5H10
  part4 = cC4H6*C4H6+cC2H2*C2H2
  part5 = cH2*H2+cH2S*H2S+cO2*O2+cN2*N2+cAr*Ar+cH2O*H2O
  part6 = cCO*CO+cCO2*CO2+cSO2*SO2
  Rez = 0.01*(part1+part2+part3+part4+part4+part5+part6)+0.00124*cH2O*dGas
  return Rez

@xlfunc
def f_b_003_f_31_xTrEkran(TypeEkr,Obm_D,S_D):
  ''' Угловой коэффициент трубных экранов
  TypeEkr: 1 - odnoradniy gladkotrubniy s uchetom izlucheniya obmurovki;
  2 - odnoradniy gladkotrubniy bez ucheta izlucheniya obmurovki pri obm_D >=0.5;
  3 - dvuhradniy gladkotrubniy ekran s uchetom izlucheniya obmurovki pri Obm_D >= 1.4'''
  if TypeEkr == 1:
    if Obm_D >= 1.4:
      Rez = numpy.interp(S_D,
                         [1.0,2.0,3.0,4.0],
                         [1.0,0.9,0.72,0.58])
    if Obm_D >= 0 and Obm_D < 1.4:
      Rez0 =  numpy.interp(S_D,
                         [1.0,2.0,3.0,4.0],
                         [1.0,0.7,0.47,0.36])
      Rez05 = numpy.interp(S_D,
                         [1.0,2.0,3.0,4.0],
                         [1.0,0.82,0.63,0.5])
      Rez08 = numpy.interp(S_D,
                         [1.0,2.0,3.0,4.0],
                         [1.0,0.86,0.68,0.54])
      Rez14 = numpy.interp(S_D,
                         [1.0,2.0,3.0,4.0],
                         [1.0,0.9,0.72,0.58])
      Rez = numpy.interp(Obm_D,
                         [0.0,0.5,0.8,1.4],
                         [Rez0,Rez05,Rez08,Rez14])
  if TypeEkr == 2:
    Rez = numpy.interp(S_D,
                       [1.0,2.0,3.0,4.0],
                       [1.0,0.61,0.43,0.34])
  if TypeEkr == 3:
    Rez = numpy.interp(S_D,
                       [1.0,2.0,3.0],
                       [1.0,0.98,0.90])
  return Rez

@xlfunc
def f_b_003_f_32_kgrp(Teta,rH2O,rp,pg,s):
  ''' Коэффициент ослабления лучей для топочной среды, 1/(м*кГс/см2)'''
  Rez = (0.78+1.6*rH2O/((pg*rp*s)**0.5)-0.1)*(1-0.37*(Teta+273.15)/1000.0)*rp
  return Rez

@xlfunc
def f_b_003_f_33_Cr_Hr(CH4,C2H6,C3H8,C4H10,C5H12,C6H14,C6H12,C6H6,
                                C2H4,C3H6,C4H8,C5H10,C4H6,C2H2):
  ''' Соотношение содержания углерода и водорода в топливном газе'''
  part1 = 0.25*CH4+1.0/3.0*C2H6+3.0/8.0*C3H8+4.0/10.0*C4H10+5.0/12.0*C5H12+6.0/14.0*C6H14+0.5*C6H12
  part2 = C6H6+0.5*C2H4+0.5*C3H6+0.5*C4H8+0.5*C5H10+4.0/6.0*C4H6+C2H2
  Rez = 0.12*(part1+part2)
  return Rez

@xlfunc
def f_b_003_f_34_kAsh(Regime,Teta,AlfaFH,Cr_Hr):
  ''' Коэффициент ослабления лучей сажистыми частицами, 1/(м*кГс/см2)
  Regime:
  0 - RTM and NTR 1973;
  1 - NTR 1990.'''
  if Regime == 1:
    Rez = 1.2/(1.0+AlfaFH*AlfaFH)*(1.6*(Teta+273.15)/1000.0-0.5)*(Cr_Hr**0.4)/10.0
  if Regime == 0:
    Rez = 0.03*(2.0-AlfaFH)*(1.6*(Teta+273.15)/1000.0-0.5)*Cr_Hr
    if AlfaFH > 2.0:
      Rez = 0
  return Rez

@xlfunc
def f_b_003_f_35_aGas(kG,pG,s):
  ''' Степень черноты газов'''
  Rez = 1.0-numpy.exp(-(kG)*pG*s)
  return Rez

@xlfunc
def f_b_003_f_36_Bo(phi,Br,VC_Gas,TetaAd,Hl):
  ''' Число Больцмана '''
  Rez = phi*Br*VC_Gas/(5.670367e-8*(TetaAd+273.15)**3.0*Hl)
  return Rez

@xlfunc
def f_b_003_f_37_DeltaKsi(TypeRadPart,af,Ksi):
  ''' Величина Дельта Кси:
  TypeRadPart:
  1 - kamernie topki;
  2 - topki s izluchaushimi stenami (sloevie ytopki);
  '''
  if TypeRadPart == 1.0:
    if Ksi <= 0.5:
      Rez = (1.0-af)/(1.0-af*Ksi)
    if Ksi > 0.5:
      Rez = (1.0-af-(2.0*Ksi-1.0)*(1.0-af/Ksi)/Ksi)/(1.0-af*Ksi-(2.0*Ksi-1.0)*(1.0-af)/Ksi)
  if TypeRadPart == 2.0:
    Rez = (1.0-Ksi)/(1.0+Ksi*(1.0/af-1.0))
  return Rez

@xlfunc
def f_b_003_f_38_DeltaKsiNast(af,Ksi,Rr):
  ''' Величина Дельта Кси для топок с настильными стенами:
  TypeRadPart:
  3 - topki s nastilnimi stenami
  '''
  Rez = 1.0/(1.0+Ksi*(1.0/af-1.0)*(1.0-Rr*(1.0-af)))
  return Rez

@xlfunc
def f_b_003_f_39_A_FH(TypeRadPart,af,Ksi,An,DeltaKsi):
  ''' Приведенная степень черноты топочной камеры по методу ВТИ-ЭНИН:
  TypeRadPart:
  1 - kamernie topki;
  2 - topki s izluchaushimi stenami (sloevie ytopki);
  '''
  if TypeRadPart == 1.0:
    if Ksi < 0.8:
      Rez = 1.0/(1.0/An+Ksi*(1.0/af-1.0)*DeltaKsi) 
    if Ksi >= 0.8:
      Rez = 1.0/(1.0/An+Ksi*(1.0/af-1.0)) 
  if TypeRadPart == 2.0:
    Rez = 1.0/(1.0/An+Ksi*(1.0/af-1.0)*DeltaKsi) 
  return Rez

@xlfunc
def f_b_003_f_40_A_FHNast(af,KsiL,KsiN,An,Rr,DeltaKsi):
  ''' Приведенная степень черноты топочной камеры по методу ВТИ-ЭНИН:
  TypeRadPart:
  3 - topki s nastilnimi stenami
  '''
  Rez = 1.0/(1.0/An+KsiL*(1.0/af-1.0)*DeltaKsi+Rr*KsiN*(1.0/af-1.0)*(1.0-af)) 
  return Rez

@xlfunc
def f_b_003_f_41_BetaFH(Ksi):
  ''' Поправочный коэффициент, учитывающий действительное расположение экранов:
  Для камерной топки со свободным факелом
  '''
  if Ksi <=0.35:
    Rez = 0.8
  if Ksi > 0.35 and Ksi <= 0.55:
    Rez = 0.85
  if Ksi > 0.55 and Ksi <= 0.8:
    Rez = 0.9
  if Ksi > 0.8:
    Rez = 1.0
  return Rez

@xlfunc
def f_b_003_f_42_TetaEf4(TypeFuel,TypeRadPart,TetaNSt,lt,lf):
  ''' Температурная функция TetaЭфективная4:
  TypeFuel:
  1 - Gas;
  2 - Oil.  
  TypeRadPart:
  1 - kamernie topki so svobodnim fakelom;
  2 - topki s izluchaushimi stenami (sloevie topki)
  Здесь вместо lf и lt надо подставлять B2 и B1;
  3 - topki s nastil'nimi stenami
  '''
  Rez2 = 1.0 # Поправочный коэффициент на температуру
  if TetaNSt >=500.0 and TetaNSt<=950.0:
    Rez2 = 1.0-0.00035*(TetaNSt-500.0)
  if TypeRadPart == 1:
    if TypeFuel == 1:
      Rez1 = 1.45-0.3*lf/lt
    if TypeFuel == 2:
      Rez1 = 1.40-0.3*lf/lt
  if TypeRadPart == 2:
    Rez1 = 1.75-0.2*lf/lt # Здесь вместо lf и lt надо подставлять B2 и B1
  if TypeRadPart == 3:
    if TypeFuel == 1:
      Rez1 = 1.55-0.3*lf/lt
    if TypeFuel == 2:
      Rez1 = 1.50-0.3*lf/lt
  Rez = Rez1*Rez2  
  return Rez

@xlfunc
def f_b_003_f_43_AlfaKGBelokon(Ab,TetaT2,TayMid,RSigma,qRad):
  ''' Коэффициент теплоотдачи конвекцией от топочных газов к поверхности экранных труб
  по Белоконю Н.И.'''
  Rez = Ab*(TetaT2-(TayMid+RSigma*qRad))**0.25
  return Rez

@xlfunc
def f_b_003_f_44_KT(TetaT2,at,TetaEf4,TetaNOtn,AlfaKG,Hrad,Hl):
  ''' Приведенная характеристика теплообмена в топке, K т'''
  Rez = at*(TetaEf4-TetaNOtn**4.0)+(AlfaKG*(1-TetaNOtn)*Hrad/(5.670367e-8*Hl*((TetaT2+237.15)**3.0)))
  return Rez

@xlfunc
def f_b_003_f_45_TetaT2OtnKT(OtnKBo):
  ''' Относительная температура газов на выходе из топки, TetaT2Otn'''
  VectOtnKBo = [0.0217,0.024,0.0265,0.0288,0.0313,0.0338,0.0365,0.039,0.0416,
                0.0444,0.0472,0.0498,0.0527,0.0557,0.0584,0.0613,0.0644,0.0674,
                0.0705,0.0739,0.077,0.0801,0.0836,0.0869,0.0903,0.0939,0.097,
                0.1004,0.1042,0.1076,0.113,0.115,0.119,0.123,0.127,0.131,
                0.135,0.1395,0.1435,0.1475,0.152,0.157,0.161,0.166,0.17,0.175,
                0.18,0.185,0.19,0.195,0.2,0.205,0.211,0.216,0.221,0.227,0.232,
                0.238,0.244,0.248,0.256,0.262,0.268,0.274,0.28,0.286,0.294,
                0.3,0.307,0.312,0.321,0.328,0.336,0.343,0.351,0.358,0.366,
                0.373,0.382,0.39,0.398,0.406,0.415,0.424,0.432,0.44,0.45,
                0.46,0.468,0.478,0.488,0.497,0.509,0.529,0.53,0.539,0.549,
                0.561,0.571,0.584,0.593,0.605,0.618,0.63,0.641,0.653,0.668,
                0.681,0.692,0.708,0.72,0.732,0.748,0.76,0.775,0.79,0.806,
                0.821,0.836,0.85,0.866,0.883,0.901,0.918,0.935,0.95,0.969,
                0.985,1.003,1.022,1.041,1.06,1.08,1.1,1.12,1.14,1.16,1.18,
                1.202,1.227,1.25,1.27,1.294,1.32,1.343,1.363,1.39,1.4,1.44,
                1.47,1.495,1.53,1.544,1.58,1.61,1.64,1.663,1.69,1.73,1.76,
                1.796,1.82,1.855,1.89,1.92,1.955,1.99,2.025,2.07,2.11,2.15,
                2.18,2.225,2.27,2.31,2.35,2.38,2.44,2.48,2.53,2.57,2.61,
                2.66,2.72,2.77,2.81,2.86,2.92,2.96,3.03,3.08,3.14,3.2,3.25,
                3.32,3.38,3.45,3.51,3.57,3.65,3.71,3.78,3.85,3.93,4.0,4.08,
                4.14,4.22,4.32,4.39,4.46,4.56,4.65,4.74,4.84,4.92,5.0,5.11,
                5.21,5.31,5.41,5.52,5.62,5.73,5.84,5.97,6.08,6.2,6.32,6.35,
                6.57,6.7,6.85,7.0,7.15,7.25,7.42,7.55,7.71,7.85,8.0,8.27,
                8.35,8.5,8.68,8.85,9.05,9.25,9.45,9.61,9.8,10.0,10.2,10.41,
                10.65,10.85,11.1,11.34,11.6,11.8,12.04,12.34,12.6,12.85,
                13.16,13.4,13.7,14.0,14.3,14.6,14.9,15.3,15.6,15.95,16.3,
                16.7,17.0,17.5,17.8,18.2,18.7,19.1,19.5,19.9,20.3,20.9,
                21.3,21.9,22.4,22.9,23.4]  
  VectTetaT2Otn = [0.98,0.978,0.976,0.974,0.972,0.97,0.968,0.966,0.964,0.962,
                   0.96,0.958,0.956,0.954,0.952,0.95,0.948,0.946,0.944,0.942,
                   0.94,0.938,0.936,0.934,0.932,0.93,0.928,0.926,0.924,0.922,
                   0.92,0.918,0.916,0.914,0.912,0.91,0.908,0.906,0.904,0.902,
                   0.9,0.898,0.896,0.894,0.892,0.89,0.888,0.886,0.884,0.882,
                   0.88,0.878,0.876,0.874,0.872,0.87,0.868,0.866,0.864,0.862,
                   0.86,0.858,0.856,0.854,0.852,0.85,0.848,0.846,0.844,0.842,
                   0.84,0.838,0.836,0.834,0.832,0.83,0.828,0.826,0.824,0.822,
                   0.82,0.818,0.816,0.814,0.812,0.81,0.808,0.806,0.804,0.802,
                   0.8,0.798,0.796,0.794,0.792,0.79,0.788,0.786,0.784,0.782,
                   0.78,0.778,0.776,0.774,0.772,0.77,0.768,0.766,0.764,0.762,
                   0.76,0.758,0.756,0.754,0.752,0.75,0.748,0.746,0.744,0.742,
                   0.74,0.738,0.736,0.734,0.732,0.73,0.728,0.726,0.724,0.722,
                   0.72,0.718,0.716,0.714,0.712,0.71,0.708,0.706,0.704,0.702,
                   0.7,0.698,0.696,0.694,0.692,0.69,0.688,0.686,0.684,0.682,
                   0.68,0.678,0.676,0.674,0.672,0.67,0.668,0.666,0.664,0.662,
                   0.66,0.658,0.656,0.654,0.652,0.65,0.648,0.646,0.644,0.642,
                   0.64,0.638,0.636,0.634,0.632,0.63,0.628,0.626,0.624,0.622,
                   0.62,0.618,0.616,0.614,0.612,0.61,0.608,0.606,0.604,0.602,
                   0.6,0.598,0.596,0.594,0.592,0.59,0.588,0.586,0.584,0.582,
                   0.58,0.578,0.576,0.574,0.572,0.57,0.568,0.566,0.564,0.562,
                   0.56,0.558,0.556,0.554,0.552,0.55,0.548,0.546,0.544,0.542,
                   0.54,0.538,0.536,0.534,0.532,0.53,0.528,0.526,0.524,0.522,
                   0.52,0.518,0.516,0.514,0.512,0.51,0.508,0.506,0.504,0.502,
                   0.5,0.498,0.496,0.494,0.492,0.49,0.488,0.486,0.484,0.482,
                   0.48,0.478,0.476,0.474,0.472,0.47,0.468,0.468,0.464,0.462,
                   0.46,0.458,0.456,0.454,0.452,0.45,0.448,0.446,0.444,0.442,
                   0.44,0.438,0.436,0.434,0.432,0.43,0.428,0.426,0.424,0.422,
                   0.42,0.418,0.416,0.414,0.412,0.41,0.408,0.406,0.404,0.402,
                   0.4]
  Rez = numpy.interp(OtnKBo,VectOtnKBo,VectTetaT2Otn)
  return Rez

@xlfunc
def f_b_003_f_46_TetaT2(TetaEf4,HRad,Hl,at,qRad,qRK,TetaN):
  ''' Температура газов на выходе из топки, С'''
  part1 = HRad*(qRad-qRK)/(Hl*at*5.670367e-8)
  part2 = ((TetaN+273.15)/100.0)**4.0
  Rez = ((1.0/TetaEf4)*(part1+part2))**0.25-273.15
  return Rez

@xlfunc
def f_b_003_f_47_DeltaTBelokon(TetaAd,TetaN,TetaT2,IT2,Br,AlfaKG,HRad,Hl,at):
  ''' Температурная поправка к теплопередаче по Белоконю Н.И.'''
  part1 = AlfaKG*HRad*(TetaAd-TetaN)
  part2 = 5.670367e-8*Hl*at*((TetaN+273.15)**4.0)
  part3 = IT2*Br/TetaT2+AlfaKG*HRad
  Rez = (part1-part2)/part3
  return Rez

@xlfunc
def f_b_003_f_48_XBelokon(TetaAd,DeltaT,TetaT2,IT2,Br,AlfaKG,HRad,Hl,at):
  ''' Аргумент излучения Белоконя Н.И.'''
  part1 = 10*5.670367*Hl*at*(((TetaAd+273.15-DeltaT)/1000.0)**3.0)
  part2 = IT2*Br/TetaT2+AlfaKG*HRad
  Rez = part1/part2
  return Rez

@xlfunc
def f_b_003_f_49_BetaSBelokon(XBelokon):
  ''' Характеристика излучения Белоконя Н.И.'''
  Rez = 1.0/(0.25+(0.1875+(0.141+XBelokon)**0.5)**0.5)
  return Rez

@xlfunc
def f_b_003_f_50_Phi1CilindrFH(Dtr,Str,Dzm):
  ''' Коэффициент Фи1 от относительного диаметра и окружности радиантного
  змеевика, рис 2 стр 37 РТМ 26-02'''
  Line18 = numpy.interp(Dzm/Dtr,
                       [10.0,20.0,30.0,40.0,50.0,60.0],
                       [0.45,0.49,0.5,0.51,0.52,0.53])
  Line20 = numpy.interp(Dzm/Dtr,
                       [10.0,20.0,30.0,40.0,50.0,60.0],
                       [0.5,0.54,0.55,0.55,0.55,0.56])
  Rez = numpy.interp(Str/Dtr,[1.8,2.0],[Line18,Line20])
  return Rez

@xlfunc
def f_b_003_f_51_Phi1KorobFH(TypeEkr,Dtr,Str):
  ''' Коэффициент Фи1 от относительного шага и типа экрана
  TypeEkr: 
    1 - dvusvetniy ekran odnoryadniy
    2 - dvusvetniy ekran dvuhriadniy s peremennim shagom
    3 - !!! odnoryadniy nastenniy ekran i dvuhriadniy ekran dvustoronnego scvesheniya
    Рисунок 2-2 стр. 38 РТМ 26-02
  '''
  if TypeEkr == 1:
    Rez = numpy.interp(Str/Dtr,
                       [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4,2.6,2.8, 3.0, 3.2, 3.4, 3.6, 3.8,4.0],
                       [0.65,0.72,0.77,0.81,0.84,0.86,0.88,0.9,0.9,0.91,0.92,0.92,0.93,0.93,0.93,0.93])
  if TypeEkr == 2:
    Rez = numpy.interp(Str/Dtr,
                       [1.0, 1.2, 1.4, 1.6,1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8,4.0],
                       [0.48,0.52,0.58,0.6,0.63,0.65,0.68,0.69,0.71,0.72,0.73,0.74,0.74,0.74,0.75,0.75])
  if TypeEkr == 3:
    Rez = numpy.interp(Str/Dtr,
                       [1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0],
                       [0.32,0.4,0.45,0.48,0.53,0.55,0.58,0.6,0.62,0.64,0.65,0.67,0.68,0.69,0.7])
  return Rez

@xlfunc
def f_b_003_f_52_k_HeatTrans(Alfa1,Delta1,Lambda1,DeltaM,LambdaM,Delta2,Lambda2,Alfa2):
  '''Koefficient teploperedachi formula 7-10 NTR  1998
  '''
  Rez = 1.0/(1/Alfa1+Delta1/Lambda1+DeltaM/LambdaM+Delta2/Lambda2+1/Alfa2)
  return Rez

@xlfunc
def f_b_003_f_53_k_HeatTrans(Psi,Alfa1,Alfa2,Ql,Q):
  '''Koefficient teploperedachi formula 7-15 + NTR 1998 
  '''
  Rez = Psi*Alfa1/(1.0+(1+Ql/Q)*Alfa1/Alfa2)
  return Rez

@xlfunc
def f_b_003_f_54_k_HeatTrans(Psi,Alfa1,Alfa2,Ql,Q,H,Hvn):
  '''Koefficient teploperedachi formula 7-17a + NTR 1998 
  '''
  Rez = Psi*Alfa1/(1.0+(1+Ql/Q)*Alfa1*H/(Alfa2*Hvn))
  return Rez

@xlfunc
def f_b_003_f_55_AlfaPr(TypeOreb,OtnHtrH,OtnHorH,E,Mu,PhiE,AlfaK):
  '''Koefficient privedenniy teplootdachi orebrennih trub formula 7-21 + NTR 1998
  TypeOreb: 0 - circle; 1 - square 
  '''
  Rez = (OtnHtrH+OtnHorH*E*Mu*PhiE)*AlfaK
  return Rez

@xlfunc
def f_b_003_f_56_Alfa1PrivOrebrTube(TypeBundle,TypeOreb,
                                DTube,s1,s2,z2,HReb,DeltaReb,SReb,LambdaReb,
                                Re,Pr,LambdaPC):
  '''Koefficient teplootdachi orebrennih trub formula 7-52 + NTR 1998
  TypeBundle: 0 - chess; 1 - corridor   
  TypeOreb: 0 - circle; 1 - square (then DReb = C -сторона квадрата!!!) 
  '''
  Sigma1 = s1/DTube
  Sigma2 = s2/DTube  
  
  if TypeOreb == 0:
    DReb = DTube+2.0*HReb
    PsiR = (DReb**2.0-DTube**2.0+2*DReb*DeltaReb)/(2*DTube*SReb)+1-DeltaReb/SReb 
  if TypeOreb == 1:
    DReb = 1.13*HReb
    PsiR = 2.0*(DReb**2.0-0.785*DTube**2.0+2*DReb*DeltaReb)/(numpy.pi*DTube*SReb)+1-DeltaReb/SReb 
#    HReb = 0.5*(1.13*DReb-DTube)

  if TypeBundle == 0:
    ParamX = Sigma1/Sigma2-1.26/PsiR-2.0
  if TypeBundle == 1:
    ParamX = 4.0*(PsiR/7.0+2-Sigma2)
    
  Phi = numpy.tanh(ParamX)

  Cs = (1.36-Phi)*(11.0/(PsiR+8.0)-0.14)

  Cz = 1.0
  if z2 < 8.0:
    if Sigma1/Sigma2 < 2.0:
      Cz = 3.15*(z2**0.05)-2.5
    if Sigma1/Sigma2 >= 2.0:
      Cz = 3.5*(z2**0.03)-2.75      

  n = 0.7+0.08*Phi+0.005*PsiR
  AlfaK = 0.113*Cs*Cz*(LambdaPC/DTube)*(Re**n)*(Pr**0.33)

  mReb = (2.0*AlfaK/(DeltaReb*LambdaReb))**0.5
  KoefMHReb = mReb*HReb
  
  MuR = 1.0 # Без сужения по высоте ребра. Если есть сужение у литых ребер, требуется ввести две толщины ребра
  # Корневую и на вершине и Номограмму 6 оцифровать НТР 98 стр 219

  OtnHtrH = (1.0-DeltaReb/SReb)/PsiR
  OtnHorH = 1.0 - OtnHtrH

  PhiE = 1.0-0.058*KoefMHReb 

  ER_Dd10 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,4.0,5.0],
                         [1.0,0.99,0.95,0.9,0.83,0.766,0.7,0.634,0.58,0.53,0.486,0.45,0.41,0.38,0.356,0.335,0.25,0.2])
  ER_Dd12 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6],
                         [1.0,0.985,0.95,0.89,0.82,0.75,0.68,0.62,0.56])
  ER_Dd16 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.5,3.0,3.5,3.75],
                         [1.0,0.98,0.94,0.87,0.8,0.72,0.65,0.58,0.53,0.48,0.44,0.4,0.34,0.28,0.245,0.22])
  ER_Dd20 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0],
                         [1.0,0.98,0.93,0.855,0.77,0.7,0.62,0.554,0.5,0.45,0.41,0.38,0.345,0.315,0.3,0.275])
  ER_Dd30 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,4.0,5.0],
                         [1.0,0.975,0.91,0.82,0.73,0.64,0.56,0.5,0.44,0.4,0.36,0.33,0.3,0.276,0.26,0.24,0.15,0.12])
  ER_Dd40 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,4.0,4.5,5.0],
                         [1.0,0.97,0.9,0.79,0.68,0.59,0.51,0.45,0.4,0.355,0.32,0.29,0.27,0.25,0.23,0.215,0.12,0.1,0.1])
  ER_Dd50 = numpy.interp(KoefMHReb,
                         [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0],
                         [1.0,0.965,0.87,0.75,0.64,0.54,0.466,0.4,0.36,0.32,0.29,0.26,0.24,0.22,0.21,0.19])
                         
  ER = numpy.interp(DReb/DTube,
                    [1.0, 1.2, 1.6, 2.0, 3.0, 4.0, 5.0],
                    [ER_Dd10,ER_Dd12,ER_Dd16,ER_Dd20,ER_Dd30,ER_Dd40,ER_Dd50])
  
  
  AlfaPriv = (OtnHtrH+OtnHorH*ER*MuR*PhiE)*AlfaK  
  Rez = AlfaPriv
  return Rez

@xlfunc
def f_b_003_f_57_FPCOrTube(TypeCalc,TypeBundle,AG,BG,DTube,s1,s2,HReb,DeltaReb,SReb):
  '''Ploshad' prohodnogo sechenia gazohoda s orebrennimi trubami
  TypeCalc: 0 - NTR 1998; 1 - NTR 1973;
  TypeBundle: 0 - chess; 1 - corridor
  '''
  Sigma1 = s1/DTube
  Sigma2 = s2/DTube
  Sigma2sh = ((0.5*Sigma1)**2.0+Sigma2**2.0)**0.5
  FPC = (1.0-1.0*(1.0+2.0*HReb*DeltaReb/(SReb*DTube))/Sigma1)*AG*BG
  Rez = FPC
  if TypeCalc == 0 and TypeBundle == 0 and (Sigma1-1.0)/(Sigma2-1.0)>1.7:
    Rez = 2*FPC*(Sigma2sh-1.0)/(Sigma1-1.0)
  return Rez

@xlfunc
def f_b_003_f_58_FPCGlTube(TypeCalc,TypeBundle,AG,BG,DTube,LTube,z1,s1,s2):
  '''Ploshad' prohodnogo sechenia gazohoda s orebrennimi trubami
  TypeCalc: 0 - NTR 1998; 1 - NTR 1973;
  TypeBundle: 0 - chess; 1 - corridor
  '''
  FPC = AG*BG-z1*LTube*DTube
  Rez = FPC
  Sigma1 = s1/DTube
  Sigma2 = s2/DTube
  Sigma2sh = ((0.5*Sigma1)**2.0+Sigma2**2.0)**0.5
  if TypeCalc == 0 and TypeBundle == 0 and (Sigma1-1.0)/(Sigma2-1.0)>1.7:
    Rez = 2*FPC*(Sigma2sh-1.0)/(Sigma1-1.0)
  return Rez


@xlfunc
def f_b_003_f_59_AlfaK1(TypeBundle,Re,Pr,DTube,s1,s2,z2,Lambda):
  '''Alfa01 - flow between tube, 1998 NTR
  TypeBundle: 0 - chess; 1 - corridor
  '''
  if TypeBundle == 0:
    Sigma1 = s1/DTube
    Sigma2 = s2/DTube
    Sigma2d = ((0.5*Sigma1)**2.0+Sigma2**2.0)**0.5
    PhiSigma = (Sigma1-1.0)/(Sigma2d-1.0)
    # Cs
    if (PhiSigma > 0.1)and (PhiSigma <=1.7):  
      Cs = 0.95*(PhiSigma**0.1)
      if (PhiSigma > 1.7) and (PhiSigma <= 4.5):
        if Sigma1 < 3.0:
          Cs = 0.77*(PhiSigma**0.5)
        if Sigma1 >= 3.0:
          Cs = 0.95*(PhiSigma**0.1)
    # Cz  
    if (z2 < 10.0) and (Sigma1 < 3.0):
      Cz = 3.12*(z2**0.05)-2.5
    if (z2 < 10.0) and (Sigma1 >= 3.0):
      Cz = 4*(z2**0.02)-3.2
    if z2 >= 10.0:
      Cz = 1.0
    # Nu
    Nu = 0.36*(Re**0.6)*(Pr**0.33)
    # Alfa
    Alfa = Nu*Lambda*Cs*Cz/DTube

  if TypeBundle == 1.0:
    # Если Рейнольдс больше 1500 и меньше 100 000 !!!
    Sigma1 = s1/DTube
    Sigma2 = s2/DTube
    
    # Cs
    Cs = (1.0+(2.0*Sigma1-3.0)*(1-0.5*Sigma2)**3.0)**(-2)    
    if (Sigma1 <= 1.5) or (Sigma2 >= 2.0):  
      Cs = 1.0
    if (Sigma1 > 3.0) and (Sigma2 < 2.0):
      (1.0+3.0*(1-0.5*Sigma2)**3.0)**(-2)    
    # Cz  
    if (z2 < 10.0):
      Cz = 0.91-0.0125*(z2-2.0)
    if z2 >= 10.0:
      Cz = 1.0
    # Nu
    Nu = 0.2*(Re**0.65)*(Pr**0.33)
    # Alfa
    Alfa = Nu*Lambda*Cs*Cz/DTube
  return Alfa

@xlfunc
def f_b_003_f_60_AlfaL(a,T,Tz):
  '''AlfaL, W/(m2*K) 1998 NTR f 7-64
  a - stepen' chernoty potoka gazov
  T - temperatura produktov sgorania, K
  Tz - temperatura zagryznennoi stenki, K
  '''
  Rez = 5.67e-8*(0.8+1.0)*0.5*a*T*T*T*(1-(Tz/T)**3.6)/(1-Tz/T)
  return Rez

@xlfunc
def f_b_003_f_61_sEfConvBundle(DTube,s1,s2):
  '''sEf, m 1998 NTR f 7-67
  '''
  Rez = 0.9*DTube*(4.0*s1*s2/(numpy.pi*DTube*DTube)-1.0)
  return Rez

@xlfunc
def f_b_003_f_62_TetaZagrSt(tProd,Psi,Alfa1,Alfa2,QL,QBG,Br,H):
  '''Teta zagr Stenki , C 1998 NTR f 7-69
  '''
  Rez = tProd+((1.0/Alfa1+1.0/Alfa2)/Psi-1.0/Alfa1)*Br*(QL+QBG)/H
  return Rez

@xlfunc
def f_b_003_f_63_HOrTube(DTube,LTube,NTube,HReb,DeltaReb,NReb):
  '''HOrTube, m2  '''
  DReb = DTube+2.0*HReb
  Rez = DTube*numpy.pi*LTube*NTube*(1-(NReb-1)*DeltaReb)+(NReb-1)*LTube*NTube*(DReb*numpy.pi*DeltaReb+0.5*numpy.pi*(DReb**2.0-DTube**2.0))
  return Rez

@xlfunc
def f_b_003_f_64_FindRootOnLineX(t1,t2,Qt1,Qt2,Qb1,Qb2):
  '''Find Root on Line: Teta'''
  Rez = (Qb1*t2-Qb2*t1-Qt1*t2+Qt2*t1)/(Qb1-Qb2-Qt1+Qt2)
  return Rez


@xlfunc
def f_b_003_f_65_FindRootOnLineY(t1,t2,Qt1,Qt2,Qb1,Qb2):
  '''Find Root on Line: Q'''
  k1 = (Qt2-Qt1)/(t2-t1)
  t = (Qb1*t2-Qb2*t1-Qt1*t2+Qt2*t1)/(Qb1-Qb2-Qt1+Qt2)
  Rez = k1*(t-t1)+Qt1
  return Rez


@xlfunc
def f_b_003_f_66_kQB(RatioQB):
  ''' Коэффициент увеличения мощности печи для подбора числа горелок, п. 14.1.17, стр. 31 ГОСТ Р 53682-2009 '''
  # Отношение максимально возможной мощности печи к номинальной мощности горелки по каталогу
  if numpy.trunc(RatioQB) <= 5:
    Rez = 1.2
  if numpy.trunc(RatioQB) == 6 or numpy.trunc(RatioQB) ==7:
    Rez = 1.15
  if numpy.trunc(RatioQB) >= 8:
    Rez = 1.1
  return Rez

@xlfunc
def f_b_003_f_67_lengthFB01(TypeFuel, TypeBurner, MQ1B):
  """ Функция определения расстояния по вертикали до осевой линии потолочных труб или до огнеупора (только при вертикальном факеле), м
  Тип сжигаемого топлива (TypeFuel): 1 - мазут; 2 - газ
  Тип горелки (TypeBurner): 1 - инжекционная; 2 - дутьевая """
  # Для жидкого топлива
  if TypeFuel == 1:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
           (1.0, 1.5, 2.0, 2.5, 3.0,  3.5,   4.0),
           (4.3, 5.6, 7.0, 8.3, 9.7, 11.0,  12.4))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = 0.0
  # Для газового топлива
  if TypeFuel == 2:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (2.6, 3.6, 4.6, 5.6, 6.7, 7.7, 8.7, 9.7, 10.7, 11.7))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = 0.0
  return Rez

@xlfunc
def f_b_003_f_68_lengthFB02(TypeFuel, TypeBurner, MQ1B):
  """ Функция определения расстояния по горизонтали от осевой линии горелки до осевой линии стеновых труб, м
  Тип сжигаемого топлива (TypeFuel): 1 - мазут; 2 - газ
  Тип горелки (TypeBurner): 1 - инжекционная; 2 - дутьевая """
  # Для жидкого топлива
  if TypeFuel == 1:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0),
            (0.8, 0.9, 1.1, 1.2, 1.3, 1.4, 1.6))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = numpy.interp(MQ1B,
            (2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0),
            (0.932, 1.182, 1.359, 1.52, 1.664, 1.919, 2.143, 2.346))
  # Для газового топлива
  if TypeFuel == 2:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (0.6, 0.7, 0.8, 1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.8))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = numpy.interp(MQ1B,
            (2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0),
            (0.932, 1.182, 1.359, 1.52, 1.664, 1.786, 1.923, 2.035))
  return Rez

@xlfunc
def f_b_003_f_69_lengthFB03(TypeFuel, TypeBurner, MQ1B):
  """ Функция определения расстояния по горизонтали от осевой линии горелки до неэкранированного огнеупора, м
  Тип сжигаемого топлива (TypeFuel): 1 - мазут; 2 - газ
  Тип горелки (TypeBurner): 1 - инжекционная; 2 - дутьевая"""
  # Для жидкого топлива
  if TypeFuel == 1:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0,  3.5,   4.0),
            (0.56, 0.7, 0.83, 0.96, 1.09, 1.22, 1.35))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = 0.0
  # Для газового топлива
  if TypeFuel == 2:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (0.44, 0.56, 0.7, 0.83, 0.96, 1.09, 1.22, 1.35, 1.48, 1.61))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = 0.0
  return Rez
  
@xlfunc
def f_b_003_f_70_lengthFB04(TypeFuel, TypeBurner, MQ1B):
  """ Функция определения расстояния  между противоположными горелками (при горизонтальном факеле), м
  Тип сжигаемого топлива (TypeFuel): 1 - мазут; 2 - газ
  Тип горелки (TypeBurner): 1 - инжекционная; 2 - дутьевая"""
  # Для жидкого топлива
  if TypeFuel == 1:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (1.0, 1.5, 2.0, 2.5, 3.0,  3.5,   4.0),
            (6.5, 8.8, 11.2, 13.3, 14.8, 16.4, 18.0))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = 0.0
  # Для газового топлива
  if TypeFuel == 2:
    # Для инжекционной горелки
    if TypeBurner == 1:
      Rez = numpy.interp(MQ1B,
            (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0),
            (3.4, 4.9, 6.5, 8.1, 9.6, 11.1, 11.9, 12.6, 13.4, 14.2))
    # Для дутьевой горелки
    if TypeBurner == 2:
      Rez = 0.0
  return Rez        

@xlfunc
def f_b_003_f_71_LambdaMet(Material,t):
  """ Функция определения теплопроводности твердых материалов, Вт/(м*К):
  Material:
  1 - Сталь 3;
  2 - Сталь 10, 20;
  3 - Сталь 12Х1МФ, 12ХМФ;
  4 - Сталь 12ХМ, 15ХМ;
  5 - 12Х2МФСР;
  6 - 11Х11В2МФ (ЭИ-756);
  7 - 12Х18Н10Т, 12Х18Н12Т;
  8 - 12Х14Н14В2М (ЭИ-257), 09Х14Н19В2БР (695Р);
  
  
  """
  if Material == 1:
    A = -3.32/100.0
    B = 55.0
    t0 = 0
  
  if Material == 2:
    A = -2.47/100.0
    B = 52.5
    t0 = 0
  
  if Material == 3:
    A = -2.47/100.0
    B = 42.2
    t0 = 300.0

  if Material == 4:
    A = -1.85/100.0
    B = 38.7
    t0 = 300.0

  if Material == 5:
    A = -1.16/100.0
    B = 33.6
    t0 = 300.0

  if Material == 6:
    A = -1.16/100.0
    B = 24.0
    t0 = 300.0

  if Material == 7:
    A = 1.62/100.0
    B = 21.3
    t0 = 400.0
  
  if Material == 8:
    A = 1.51/100.0
    B = 20.0
    t0 = 400.0

  Rez = A*(t-t0)+B
  return Rez        

@xlfunc
def f_b_003_f_72_LambdaMaterial(Material,t):
  """ Функция определения теплопроводности твердых материалов, Вт/(м*К):
  1) Steel:
  1.1) NTR KA 1998: 1-8.
  2) Lining:
  2.1) Источник - служебные записки ООО "ЭСКОРТ": 101-160.
  2.2) Источник ВСН 314-73 ММСС СССР, Приложение 1: 201-
  2.3) Источник ВСН 315-80 ММСС СССР: 250-
  2.4) Источник ВСН 429-81 ММСС СССР, Таблица 1, стр. 4: 301-311.
  2.5) Источник Программа расчета футеровок: 501-523.
  3) Others:
  -
  """
  def LambdaMat(A,B,t0,t):
      Rez0 = A*(t-t0)+B
      return Rez0

# Steel:  
  # 1 - Сталь 3;
  # Предельная температура применения - 400 С
  # Плотность - 7850 кг/м3
  if Material == 1:
    Rez = LambdaMat(-3.32/100.0,55.0,0,t)
  # 2 - Сталь 10, 20; Предельная температура применения - 400 С 
  if Material == 2:
    Rez = LambdaMat(-2.47/100.0,52.5,0,t)
  # 3 - Сталь 12Х1МФ, 12ХМФ; Предельная температура применения - 400 С     
  if Material == 3:
    Rez = LambdaMat(-2.47/100.0,42.2,300.0,t)
  # 4 - Сталь 12ХМ, 15ХМ;
  if Material == 4:
    Rez = LambdaMat(-1.85/100.0,38.7,300.0,t)
  # 5 - 12Х2МФСР;
  if Material == 5:
    Rez = LambdaMat(-1.16/100.0,33.6,300.0,t)
  # 6 - 11Х11В2МФ (ЭИ-756);
  if Material == 6:
    Rez = LambdaMat(-1.16/100.0,24.0,300.0,t)    
  # 7 - 12Х18Н10Т, 12Х18Н12Т;
  if Material == 7:
    Rez = LambdaMat(1.62/100.0,21.3,400.0,t)    
  # 8 - 12Х14Н14В2М (ЭИ-257), 09Х14Н19В2БР (695Р);
  if Material == 8:
    Rez = LambdaMat(1.51/100.0,20.0,400.0,t)

# Lining:

  # Источник - служебные записки ООО "ЭСКОРТ"

  # 101
  # Керамоволокно Cerablanket (1260)/CerachemBlanket (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 64
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 101:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.12,0.20,0.30,0.43])

  # 102
  # Керамоволокно Cerablanket (1260)/CerachemBlanket (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 96
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 102:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.11,0.16,0.23,0.32])

  # 103
  # Керамоволокно Cerablanket (1260)/CerachemBlanket (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 128
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 103:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.10,0.15,0.20,0.27])

  # 104 !!! - Стены печи
  # Керамоволокно Cerablanket (1260)/CerachemBlanket (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 160
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 104:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.09,0.13,0.18,0.25])

  # 105
  # Керамоволокно Z-Blok (1260)/Z-Blok (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 160
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 105:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.11,0.16,0.23,0.31])

  # 106
  # Керамоволокно Z-Blok (1260)/Z-Blok (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 180
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 106:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.10,0.15,0.22,0.30])

  # 107
  # Керамоволокно Z-Blok (1260)/Z-Blok (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 200
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 107:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.09,0.14,0.20,0.28])

  # 108
  # Керамоволокно Pyro-Blok (1260)/Pyro-Blok (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 160
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 108:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.11,0.18,0.25,0.34])

  # 109
  # Керамоволокно Pyro-Blok (1260)/Pyro-Blok (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 192
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 109:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.10,0.16,0.23,0.31])

  # 110
  # Керамоволокно Pyro-Blok (1260)/Pyro-Blok (1425)
  # Предельно допустимая температура применения, С: 1260/1425
  # Плотность,кг/м3: 240
  # Morgan Thermal Ceramics ОАО Сухоложский огнеупорный завод
  if Material == 110:
    Rez = numpy.interp(t,
                       [400,600,800,1000],
                       [0.09,0.14,0.20,0.28])

  # 121
  # Легковесный бетон Алакс-0,6-1000
  # Предельно допустимая температура применения, С: 1000
  # Плотность,кг/м3: 600
  # ООО "Алитер-акси"
  if Material == 121:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.14,0.16,0.18,0.20,0.22])

  # 122
  # Легковесный бетон Алакс-0,7-1000
  # Предельно допустимая температура применения, С: 1000
  # Плотность,кг/м3: 700
  # ООО "Алитер-акси"
  if Material == 122:
    Rez = numpy.interp(t,
                       [300,500,700],
                       [0.15,0.17,0.19])

  # 123 !!! Стены и газоход печи!!!
  # Легковесный бетон Алакс-0,9-1000
  # Предельно допустимая температура применения, С: 1000
  # Плотность,кг/м3: 900
  # ООО "Алитер-акси"
  if Material == 123:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.2,0.22,0.24,0.26,0.28])

  # 124
  # Легковесный бетон Алакс-1,0-1000
  # Предельно допустимая температура применения, С: 1000
  # Плотность,кг/м3: 1000
  # ООО "Алитер-акси"
  if Material == 124:
    Rez = numpy.interp(t,
                       [300,500,700],
                       [0.21,0.24,0.27])

  # 125
  # Легковесный бетон Алакс-1,0-1350 (1250)
  # Предельно допустимая температура применения, С: 1350 (1250)
  # Плотность,кг/м3: 1000
  # ООО "Алитер-акси"
  if Material == 125:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.26,0.3,0.33,0.37,0.42])

  # 126
  # Легковесный бетон Алакс-1,2-1200
  # Предельно допустимая температура применения, С: 1200
  # Плотность,кг/м3: 1200
  # ООО "Алитер-акси"
  if Material == 126:
    Rez = numpy.interp(t,
                       [300,500,700,900],
                       [0.27,0.3,0.33,0.37])

  # 127
  # Легковесный бетон Алакс-1,2-1350
  # Предельно допустимая температура применения, С: 1350
  # Плотность,кг/м3: 1200
  # ООО "Алитер-акси"
  if Material == 127:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.37,0.4,0.43,0.46,0.5])

  # 128
  # Легковесный бетон Алакс-1,4-1350(А)
  # Предельно допустимая температура применения, С: 1350
  # Плотность,кг/м3: 1400
  # ООО "Алитер-акси"
  if Material == 128:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.47,0.5,0.53,0.56,0.59])

  # 129
  # Легковесный бетон Алакс-1,6-1800
  # Предельно допустимая температура применения, С: 1800
  # Плотность,кг/м3: 1600
  # ООО "Алитер-акси"
  if Material == 129:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100,1300],
                       [0.66,0.7,0.75,0.82,0.87,0.96])

  # 130
  # Легковесный бетон Алакс-1,6-1800/4C
  # Предельно допустимая температура применения, С: 1800
  # Плотность,кг/м3: 1600
  # ООО "Алитер-акси"
  if Material == 130:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100,1300],
                       [0.76,0.8,0.85,0.91,0.98,1.05])

  # 131
  # Легковесный бетон Алкор-45
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 
  # ООО "Алитер-акси"
  if Material == 131:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.92,1.0,1.09,1.2,1.3])

  # 132
  # Легковесный бетон Алкор-37-25
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 
  # ООО "Алитер-акси"
  if Material == 132:
    Rez = numpy.interp(t,
                       [300,500,700,900,1100],
                       [0.71,0.80,0.88,0.99,1.08])

  # 140
  # Блоки из керамического волокна ТБКВ
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 200
  # ООО "СпецОгнеупорКомплект"
  if Material == 140:
    Rez = numpy.interp(t,
                       [200,300,500,800,1000],
                       [0.06,0.08,0.12,0.18,0.22])

  # 141
  # Блоки из керамического волокна ТБКВ-Z
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 200
  # ООО "СпецОгнеупорКомплект"
  if Material == 141:
    Rez = numpy.interp(t,
                       [200,300,500,800,1000],
                       [0.06,0.08,0.14,0.24,0.31])

  # 142
  # теплоизоляционные изделия из силиката кальция марки ТИСК
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 250-1000
  # ООО "СпецОгнеупорКомплект"
  if Material == 142:
    Rez = numpy.interp(t,
                       [225.5,328.5,432.0,542.0],
                       [0.07,0.09,0.11,0.14])

  # 150
  # Теплоизоляционный бетон "Слокер-100-V-10"
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 1000
  # ООО ПКФ "ЦЕМОГНЕУПОР"
  if Material == 150:
    Rez = numpy.interp(t,
                       [365,475],
                       [0.24,0.3])

  # 151
  # Теплоизоляционный бетон "Слокер-100-V-8"
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 800
  # ООО ПКФ "ЦЕМОГНЕУПОР"
  if Material == 151:
    Rez = numpy.interp(t,
                       [362,472],
                       [0.22,0.22])

  # 160 - Подозрительные данные по матам!!!
  # Маты МКРВ-200 ?????
  # Предельно допустимая температура применения, С: 
  # Плотность,кг/м3: 
  #
  if Material == 160:
    Rez = numpy.interp(t,
                       [25,300,600],
                       [0.039,0.127,0.147])


  # Источник ВСН 314-73 ММСС СССР

  # 201
  # Обычный тяжелый бетон
  # Предельно допустимая температура применения, С: 300
  # Плотность,кг/м3: 
  if Material == 201:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300],
                       [1.12,1.14,1.21,1.28])

  # 202
  # Жаростойкий бетон с заполнителем хромит
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 202:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [1.12,1.14,1.17,1.20,1.25,1.30,1.33,1.35,1.40,1.50])

  # 203
  # Жаростойкий бетон с заполнителем базальт, диабаз, андезит
  # Предельно допустимая температура применения, С: 700
  # Плотность,кг/м3: 
  if Material == 203:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700],
                       [1.02,1.04,1.10,1.16,1.21,1.27,1.33,1.39])

  # 204
  # Жаростойкий бетон с заполнителем шамот
  # Предельно допустимая температура применения, С: 900
  # Плотность,кг/м3: 
  if Material == 204:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900],
                       [0.62,0.64,0.7,0.76,0.81,0.87,0.93,0.98,1.10])

  # 205
  # Жаростойкий бетон с заполнителем шлак, бой обыкновенного глиняного кирпича
  # Предельно допустимая температура применения, С: 700
  # Плотность,кг/м3: 
  if Material == 205:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700],
                       [0.56,0.58,0.63,0.68,0.72,0.77,0.82,0.87])

  # 206
  # Жаростойкий бетон с заполнителем артикский туф
  # Предельно допустимая температура применения, С: 700
  # Плотность,кг/м3: 
  if Material == 206:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700],
                       [0.54,0.56,0.61,0.66,0.7,0.75,0.8,0.85])

  # 207
  # Легкий жаростойкий бетон с заполнителем из керамзита с плотностью 1200
  # Предельно допустимая температура применения, С: 700
  # Плотность,кг/м3: 1200
  if Material == 207:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700],
                       [0.33,0.35,0.39,0.43,0.46,0.5,0.54,0.58])

  # 208
  # Легкий жаростойкий бетон с заполнителем из керамзита с плотностью 1500
  # Предельно допустимая температура применения, С: 700
  # Плотность,кг/м3: 1500
  if Material == 208:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700],
                       [0.37,0.40,0.46,0.51,0.57,0.63,0.69,0.75])

  # 209
  # Динасовый
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 209:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [1.38,1.39,1.43,1.46,1.49,1.53,1.56,1.59,1.66,1.72])

  # 210
  # Шамотный
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 210:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [0.63,0.65,0.71,0.77,0.82,0.87,0.93,0.99,1.1,1.21])

  # 211
  # Каолиновый
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 211:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [1.54,1.55,1.57,1.6,1.62,1.64,1.66,1.68,1.73,1.77])

  # 212
  # Высокоглиноземистый
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 212:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [1.51,1.5,1.48,1.46,1.44,1.42,1.4,1.38,1.34,1.3])

  # 213
  # Магнезитовый
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 213:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [5.16,5.07,4.84,4.61,4.38,4.15,3.92,3.69,3.23,2.77])

  # 214
  # Магнезитохромитовый
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 214:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [3.44,3.39,3.24,3.1,2.96,2.82,2.67,2.53,2.24,1.96])

  # 215
  # Хромомагнезитовый
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 215:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [2.36,2.32,2.25,2.18,2.1,2.02,1.95,1.88,1.72,1.58])

  # 216
  # Динасовый легковесный
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 
  if Material == 216:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [0.49,0.5,0.52,0.55,0.57,0.6,0.62,0.65,0.7,0.75])

  # 217
  # Шамотный легковесный 1300
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 1300
  if Material == 217:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [0.42,0.43,0.47,0.5,0.53,0.56,0.6,0.63,0.7,0.76])

  # 218
  # Шамотный легковесный 1000
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 1000
  if Material == 218:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [0.29,0.3,0.33,0.36,0.39,0.42,0.45,0.48,0.54,0.6])

  # 219
  # Шамотный легковесный 800
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 800
  if Material == 219:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [0.2,0.21,0.23,0.25,0.27,0.29,0.31,0.33,0.36,0.4])

  # 220
  # Шамотный легковесный 400
  # Предельно допустимая температура применения, С: 1100
  # Плотность,кг/м3: 400
  if Material == 220:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900,1100],
                       [0.11,0.11,0.13,0.14,0.16,0.17,0.18,0.2,0.23,0.25])

  # 221
  # Диатомитовый марки 600
  # Предельно допустимая температура применения, С: 900
  # Плотность,кг/м3: 
  if Material == 221:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900],
                       [0.12,0.13,0.15,0.17,0.19,0.21,0.23,0.25,0.29])

  # 222
  # Диатомитовый марки 500
  # Предельно допустимая температура применения, С: 900
  # Плотность,кг/м3: 
  if Material == 222:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900],
                       [0.10,0.11,0.13,0.15,0.17,0.19,0.21,0.23,0.27])

  # 223
  # Асбестовый картон
  # Предельно допустимая температура применения, С: 500
  # Плотность,кг/м3: 
  if Material == 223:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500],
                       [0.14,0.15,0.16,0.17,0.18,0.19])

  # 224
  # Глиняный обыкновенный кирпич
  # Предельно допустимая температура применения, С: 900
  # Плотность,кг/м3: 
  if Material == 224:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900],
                       [0.43,0.44,0.49,0.53,0.58,0.62,0.66,0.71,0.8])

  # 225
  # Совелитовые плиты марки 400
  # Предельно допустимая температура применения, С: 500
  # Плотность,кг/м3: 
  if Material == 225:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500],
                       [0.076,0.08,0.089,0.098,0.107,0.116])

  # 226
  # Совелитовые плиты марки 350
  # Предельно допустимая температура применения, С: 500
  # Плотность,кг/м3: 
  if Material == 226:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500],
                       [0.073,0.077,0.085,0.093,0.102,0.111])

  # 227
  # Асбестовермикулит 250
  # Предельно допустимая температура применения, С: 500
  # Плотность,кг/м3: 
  if Material == 227:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500],
                       [0.076,0.083,0.1,0.119,0.137,0.155])

  # 228
  # Маты минеральные 250
  # Предельно допустимая температура применения, С: 500
  # Плотность,кг/м3: 
  if Material == 228:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500],
                       [0.06,0.067,0.083,0.099,0.115,0.131])

  # 229
  # Вермикулит обожженный 125
  # Предельно допустимая температура применения, С: 900
  # Плотность,кг/м3: 
  if Material == 229:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700,900],
                       [0.076,0.084,0.104,0.124,0.145,0.165,0.185,0.2,0.25])

  # 230
  # Асбозурит 600
  # Предельно допустимая температура применения, С: 700
  # Плотность,кг/м3: 
  if Material == 230:
    Rez = 4.1868/3.6*numpy.interp(t,
                       [50,100,200,300,400,500,600,700],
                       [0.15,0.16,0.17,0.18,0.2,0.22,0.23,0.25])



  '''# Источник ВСН 315-80 ММСС СССР

  # 251 - Перлитобетон на портландцементе с тонкомолотым шамотом
  # Предельно допустимая температура применения, С: 500
  # Объемная масса бетона в высушенном состоянии,кг/м3: 800 
  if Material == 251:
    Rez = numpy.interp(t,
                       [20.0,600.0],
                       [0.19,   0.205,   0.22,  0.235,   0.25])
  '''
  # Источник ВСН 429-81 ММСС СССР, Таблица 1, стр. 4


  # 301
  # Муллитокремнеземистая вата, МКРВ
  # Предельно допустимая температура применения, С: 1150
  # Объемная масса,кг/м3: 100 
  # ГОСТ 23619-79
  # Богдановинский огнеупорный завод (Сухолонское производство), Северский доломитный завод
  if Material == 301:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0,1200.0],
                       [0.08,0.12,0.17,0.29,0.47,0.79])

  # 302
  # Муллитокремнеземистый рулонный материал, МКРР-130
  # Предельно допустимая температура применения, С: 1150
  # Объемная масса,кг/м3: 130 
  # ГОСТ 23619-79
  # Богдановинский огнеупорный завод (Сухолонское производство), Северский доломитный завод
  if Material == 302:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0,1200.0],
                       [0.14,0.17,0.22,0.31,0.50,0.79])

  # 303
  # Муллитокремнеземистые плиты на органической связке, МКРП-340
  # Предельно допустимая температура применения, С: 1150
  # Объемная масса,кг/м3: 340 
  # ГОСТ 23619-79
  # Богдановичский огнеупорный завод, Северский доломитный завод, Первоуральский динасовый завод
  if Material == 303:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0,1200.0],
                       [0.15,0.19,0.23,0.29,0.40,0.53])

  # 304
  # Муллитокремнеземистый войлок, МКРВ-200
  # Предельно допустимая температура применения, С: 1150
  # Объемная масса,кг/м3: 200 
  # ГОСТ 23619-79
  # Богдановичский огнеупорный завод (Сухолонское производство)
  if Material == 304:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0,1200.0],
                       [0.09,0.12,0.14,0.20,0.33,0.58])

  # 305
  # Плиты на основе муллитокремнеземистой ваты и глиняной связки, ШВП-350
  # Предельно допустимая температура применения, С: 1200
  # Объемная масса,кг/м3: 350 
  # ТУ 36-2345-80
  # Апрелевский опытный завод теплоизоляционных изделий, ВНИПИ Теплопроект
  if Material == 305:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0,1200.0],
                       [0.15,0.17,0.19,0.23,0.29,0.43])

  # 306
  # Теплоизоляционные композиции 1
  # Предельно допустимая температура применения, С: 850
  # Объемная масса,кг/м3: 400 
  # ВСН 412-80 ММСС СССР
  # Апрелевский опытный завод теплоизоляционных изделий, ВНИПИ Теплопроект
  if Material == 306:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0],
                       [0.17,0.2,0.24,0.3,0.41])

  # 307
  # Теплоизоляционные композиции 2
  # Предельно допустимая температура применения, С: 1000
  # Объемная масса,кг/м3: 600 
  # ВСН 412-80 ММСС СССР
  # Апрелевский опытный завод теплоизоляционных изделий, ВНИПИ Теплопроект
  if Material == 307:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0],
                       [0.21,0.23,0.29,0.36,0.44])

  # 308
  # Шнуры теплоизоляционные из муллитокремнеземистой ваты
  # Предельно допустимая температура применения, С: 1150
  # Объемная масса,кг/м3: 200 
  # ТУ 36-1695-79
  # Беличское НПО «Теплозвукоизоляция»
  if Material == 308:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0,800.0,1000.0,1200.0],
                       [0.07,0.12,0.19,0.26,0.44,0.58])

  # 309
  # Плиты теплоизоляционные из минеральной ваты на синтетическом связующем
  # Предельно допустимая температура применения, С: 500
  # Объемная масса,кг/м3: 100 
  # ГОСТ 9673-72
  # ПО «Мосасботермостекло», Вильнюсское ПО силикатных изделий
  if Material == 309:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0],
                       [0.086,0.109,0.188])

  # 310
  # Плиты теплоизоляционные из минеральной ваты на синтетическом связующем
  # Предельно допустимая температура применения, С: 500
  # Объемная масса,кг/м3: 125 
  # ГОСТ 9673-72
  # ПО «Мосасботермостекло», Вильнюсское ПО силикатных изделий
  if Material == 310:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0],
                       [0.038,0.112,0.192])

  # 311
  # Плиты теплоизоляционные повышенной жесткости из минеральной ваты на синтетическом связующем
  # Предельно допустимая температура применения, С: 500
  # Объемная масса,кг/м3: 200 
  # ГОСТ 22950-78
  # Коммунарский завод строительных конструкций
  if Material == 311:
    Rez = numpy.interp(t,
                       [200.0,400.0,600.0],
                       [0.105,0.14,0.174])

                       
  # Источник Программа расчета футеровок
  # Расчетная формула исходная Lambda = a + b*B, где B=10^-4*t, преобразуется в установленную в программе формулу!!!
  # 501 - 
  # Название                      Плотность  t. max   a     b
  # Динасовые обычные              2.00       1700   0.82  6.8
  if Material == 501:
    Rez = LambdaMat(6.8/10000.0,0.82,0,t)    

  # 502 - 
  # Название                      Плотность  t. max   a     b
  # Динасовые плотные              2.10       1700   1.60  3.8
  if Material == 502:
    Rez = LambdaMat(3.8/10000.0,1.60,0,t)    

  # 503 - 
  # Название                      Плотность  t. max   a     b
  # Шамотные                       1.90       1350   0.70  6.4
  if Material == 503:
    Rez = LambdaMat(6.4/10000.0,0.7,0,t)    

  # 504 - 
  # Название                      Плотность  t. max   a     b
  # Шамотные класса "А"            1.90       1400   0.90  2.3
  if Material == 504:
    Rez = LambdaMat(2.3/10000.0,0.9,0,t)    

  # 505 - 
  # Название                      Плотность  t. max   a     b
  # Многошамотные                  2.50       1350   1.04  1.5
  if Material == 505:
    Rez = LambdaMat(1.5/10000.0,1.04,0,t)    

  # 506 - 
  # Название                      Плотность  t. max   a     b
  # Полукислые                     2.30       1400   0.70  7.0
  if Material == 506:
    Rez = LambdaMat(7.0/10000.0,0.7,0,t)    

  # 507 - 
  # Название                      Плотность  t. max   a     b
  # Магнезитовые                   2.80       1700   6.30  -27.0
  if Material == 507:
    Rez = LambdaMat(-27.0/10000.0,6.3,0,t)    

  # 508
  # Название                      Плотность  t. max   a     b
  # Хроммагнезитовые               2.70       1700   2.80  -8.7
  if Material == 508:
    Rez = LambdaMat(-8.7/10000.0,2.8,0,t)    

  # 509
  # Название                      Плотность  t. max   a     b
  # Магнезитохромитовые            2.80       1700   4.10  -16.0
  if Material == 509:
    Rez = LambdaMat(-16.0/10000.0,4.1,0,t)    

  # 510
  # Название                      Плотность  t. max   a     b
  # Корундовые                     3.50       1850   3.26  -12.0
  if Material == 510:
    Rez = LambdaMat(-12.0/10000.0,3.26,0,t)    

  # 511
  # Название                      Плотность  t. max   a     b
  # Динасовые легковесные          1.00       1500   0.50  3.70
  if Material == 511:
    Rez = LambdaMat(3.7/10000.0,0.5,0,t)    

  # 512
  # Название                      Плотность  t. max   a     b
  # Шамотные легковесные           1.30       1300   0.47  3.80
  if Material == 512:
    Rez = LambdaMat(3.8/10000.0,0.47,0,t)    

  # 513
  # Название                      Плотность  t. max   a     b
  # Шамотные легковесные           1.00       1250   0.32  3.50
  if Material == 513:
    Rez = LambdaMat(3.5/10000.0,0.32,0,t)    

  # 514
  # Название                      Плотность  t. max   a     b
  # Шамотные легковесные           0.80       1200   0.23  2.20
  if Material == 514:
    Rez = LambdaMat(2.2/10000.0,0.23,0,t)    

  # 515
  # Название                      Плотность  t. max   a     b
  # Шамотные легковесные           0.40       1100   0.12  1.60
  if Material == 515:
    Rez = LambdaMat(1.6/10000.0,0.12,0,t)    

  # 516
  # Название                      Плотность  t. max   a     b
  # Красный кирпич                 1.60       900    0.47  0.51
  if Material == 516:
    Rez = LambdaMat(0.51/10000.0,0.47,0,t)    

  # 517
  # Название                      Плотность  t. max   a     b
  # Диатомит. кирпич               0.60       900    0.12  1.50
  if Material == 517:
    Rez = LambdaMat(0.12/10000.0,1.5,0,t)    

  # 518
  # Название                      Плотность  t. max   a     b
  # Асбест                         1.20       500    0.16  1.40
  if Material == 518:
    Rez = LambdaMat(1.4/10000.0,0.16,0,t)    

  # 519
  # Название                      Плотность  t. max   a     b
  # Шлаковая вата                  0.20       600    0.05  1.40
  if Material == 519:
    Rez = LambdaMat(1.4/10000.0,0.05,0,t)    

  # 520
  # Название                      Плотность  t. max   a     b
  # Минеральная вата               0.25       600    0.05  -0.06
  if Material == 520:
    Rez = LambdaMat(-0.06/10000.0,0.05,0,t)    

  # 521
  # Название                      Плотность  t. max   a     b
  # Минеральный войлок             0.30       650    0.06  -0.08
  if Material == 521:
    Rez = LambdaMat(-0.08/10000.0,0.06,0,t)    

  # 522
  # Название                      Плотность  t. max   a     b
  # Каолиновая вата                0.20       1250   0.01  0.10
  if Material == 522:
    Rez = LambdaMat(0.1/10000.0,0.01,0,t)    

  # 523
  # Название                      Плотность  t. max   a     b
  # Плиты из каол. ваты            0.40       1250   0.12  1.60
  if Material == 523:
    Rez = LambdaMat(1.6/10000.0,0.12,0,t)    
                       
  return Rez        


@xlfunc
def f_b_003_f_73_Alfa_e(t):
  """ Функция определения коэффициента теплоотдачи от продуктов сгорания
  к футеровке, Вт/(м2*К)
  Согласно Приложению А,
  РТМ-13-2012, интерполяция по расчетной температуре горячей стороны футеровки
  """
  Rez = numpy.interp(t,
                     [50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 700.0, 900.0, 1100.0, 1200.0],
                     [12.0,  12.0,  12.0,  14.0,  18.0,  23.0,  47.0,  82.0,  140.0,  175.0])
  return Rez

@xlfunc
def f_b_003_f_74_BuEf(Bu):
  """ Функция определения эффективного критерия Бугера
  """
  Rez = 1.6*numpy.log((1.4*Bu*Bu+Bu+2.0)/(1.4*Bu*Bu-Bu+2.0))
  return Rez

@xlfunc
def f_b_003_f_75_TetaT2OtnNTR98(M,BuEf,Bo):
  ''' Относительная температура газов на выходе из топки, TetaT2Otn'''
  Rez = (Bo**0.6)/(M*(BuEf**0.3)+(Bo**0.6))
  return Rez

@xlfunc
def f_b_003_f_76_TetaT2_NTR98(Ta,M,BuEf,Psi,FSt,Phi,Br,VCsr):
  ''' Температура газов на выходе из топки, TetaT2 NTR 1998'''
  part1 = 5.67e-11*Psi*FSt*Ta*Ta*Ta
  part2 = Phi*Br*VCsr
  part3 = (part1/part2)**0.6
  part4 = (1.0+M*(BuEf**0.3)*part3) 
  Rez = (Ta/part4)-273.15
  return Rez







'''
  # Объемные доли
  r1RO2PCFuelOil = VRO20PCFuelOil/V1PCFuelOil
  r2RO2PCFuelOil = VRO20PCFuelOil/V2PCFuelOil
  r1H2OPCFuelOil = V0H2OPCFuelOil/V1PCFuelOil
  r2H2OPCFuelOil = VH2OPCFuelOil/V2PCFuelOil
  rp1PCFuelOil = r1RO2PCFuelOil+r1H2OPCFuelOil
  rp2PCFuelOil = r2RO2PCFuelOil+r2H2OPCFuelOil
'''


# Книга 4 - Моя книга по расчету печей - сборная солянка нужных мне функций
# Ручной расчет трубчатых печей

@xlfunc
def f_b_004_f_01_Test():
  Rez = 10000.0
  return Rez


  
@xlfunc
def f_b_004_f_04_MuFHrad(TypeFuel,TetaFH2):
  '''Коэффициент прямой отдачи топки, определенный графически'''
  if TypeFuel == 1.0:
    Rez = numpy.interp(TetaFH2,[500.0,600.0,700.0,800.0,900.0,1000.0,1100.0],
                               [0.719,0.67,0.619,0.567,0.515,0.462,0.406])
  if TypeFuel == 2.0:
    Rez = numpy.interp(TetaFH2,[500.0,600.0,700.0,800.0,900.0,1000.0,1100.0],
                               [0.699,0.645,0.589,0.532,0.475,0.416,0.356])
  return Rez

@xlfunc
def f_b_004_f_05_KPDFH(TypeFuel,Teta):
  '''Коэффициент топливный печи, определенный графически'''
  if TypeFuel == 1.0:
    Rez = numpy.interp(Teta,[200.0,300.0,400.0,500.0],
                               [85.1, 80.2, 75.1, 69.8])
  if TypeFuel == 2.0:
    Rez = numpy.interp(Teta,[200.0,300.0,400.0,500.0],
                               [85.0, 80.1, 75.0, 69.5])
  return Rez

@xlfunc
def f_b_004_f_06_TetaFH2Graf(qMid,tst):
  '''qMid kJ/m2, tst - C'''
  Rez1 = numpy.interp(tst, [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0],
                            [546.0, 557.0, 580.0, 608.0, 660.0, 712.0, 775.0])
  Rez2 = numpy.interp(tst, [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0],
                            [723.0, 722.0, 735.0, 757.0, 787.0, 817.0, 857.0])
  Rez3 = numpy.interp(tst, [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0],
                            [807.0, 810.0, 820.0, 835.0, 860.0, 895.0, 930.0])
  Rez4 = numpy.interp(tst, [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0],
                            [920.0, 910.0, 910.0, 925.0, 945.0, 970.0, 1000.0])
  Rez5 = numpy.interp(tst, [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0],
                            [976.0, 978.0, 980.0, 990.0, 1000.0,1040.0, 1080.0])
  Rez = numpy.interp(qMid, [11630.0, 23260.0, 34890.0, 46520.0, 58150.0],
                           [Rez1,Rez2,Rez3,Rez4,Rez5])                     
  return Rez

@xlfunc
def f_b_004_f_07_Mtube(DTube,DeltaSt,LTube,RoTube):
  '''Mass tube'''
  Rez = numpy.pi*DTube*LTube*DeltaSt*RoTube
  return Rez


@xlfunc
def f_b_004_f_10_s2MinAH(DTube,MinRast,s1):
  '''s2 Min in Air Heater '''
  Rez = ((MinRast+DTube)**2.0-(s1/2.0)**2.0)**0.5
  return Rez

@xlfunc
def f_b_004_f_11_nTubeAH(Q1,T1Mid,DTube,DeltaStTube,w1):
  '''N Tube in 1 hod Air Heater'''
  Part01 = 4.0*Q1*(T1Mid+273.15)
  Part02 = numpy.pi*((DTube-2.0*DeltaStTube)**2.0)*273.15*w1
  Rez = round(Part01/Part02)
  return Rez

@xlfunc
def f_b_004_f_12_z1AH(Q1,T1Mid,DTube,s1,hAH,w1):
  '''z1 Tube in 1 row Air Heater'''
  Part01 = Q1*(T1Mid+273.15)
  Part02 = hAH*(s1-DTube)*w1*273.15
  Rez = round(Part01/Part02)
  return Rez

@xlfunc
def f_b_004_f_13_w1AH(d,Delta,z1,z2,Q1,t1):
  '''w1 flow in Tube'''
  Rez = round((4.0*Q1*(t1+273.15))/(z1*z2*numpy.pi*((d-2.0*Delta)**2.0)*273.15))
  return Rez

@xlfunc
def f_b_004_f_14_w2AH(Regim,d,s1,s2,h,z1,Q2,t2):
  '''w2 flow between Tube
   Regim = 0 - 1973,
   Regim = 1 - 1999'''
  if Regim == 0.0:
    if (z1*h*(s1-d) != 0.0) and (s2/d != 1.0):
      Rez = (Q2*(t2+273.15))/(z1*h*(s1-d)*273.15)
    else: Rez = 9999999 # показатель ошибки!
  if Regim == 1.0:
    Rez = (Q2*(t2+273.15))/(z1*h*(s1-d)*273.15)
    if ((s1/d-1.0)/(s2/d-1.0)>1.7) and (z1*h*(s1-d) != 0.0) and (s2/d != 1.0):
      Rez = (Q2*(t2+273.15))/(2.0*273.15*(z1*h*(s1-d))*((((s1/(2.0*d))**2.0+(s2/d)**2.0)**0.5)-1.0)/(s2/d-1.0))
  return Rez

@xlfunc
def f_b_004_f_15_PDensityAH(d,s1,s2):
  '''PDensity AH - Kompaktnost'''
  Rez = numpy.pi*d/(s1*s2/(d*d))
  return Rez

@xlfunc
def f_b_004_f_15_LambdaGidr(Re,Delta):
  '''Lambda Gidravl 
  Delta = DeltaSherohovatosti/DVnutrTube  '''
  Re0 = 742.9*numpy.exp(0.00679/Delta)
  Re01 = 2002.2-8889*Delta
  Re1 = 580.0+(425.3/(Delta**0.25))+(44.0/(Delta**0.5))+(4.01/Delta)
  Re2 = 2090.0*(1.0/Delta)**0.0635
  if (Delta >= 1e-8) and (Delta <= 1e-5):
    Re3 = 2.0e5-(9.4/Delta)+(1.17/(Delta**1.25))-(0.0017/(Delta**1.5))
  if (Delta >= 1e-5) and (Delta <= 1e-2):
    Re3 = (20.8/Delta)-(3.7/(Delta**1.25))+(0.501/(Delta**1.5))-(0.0678/(Delta**1.65))+(0.0002/(Delta**2.0))
  Re4 = (16100.0/Delta)
  Eps = 1.0e-8
  if (Delta <= 0.00135):
    if (Re >= 0.0) and (Re <= 1990.2):
      Rez = 64.0/Re
    if (Re > 1990.2) and (Re <= 3179.582):
      Rez = 0.008547*numpy.exp(-(0.0017*(3179.58-Re))**2.0)+0.032
    if (Re > 3179.582) and (Re <= 4000.0):
      Rez = 2.53042e-6*Re+0.0325013
    if (Re > 4000.0) and (Re <= Re3):
      Rez = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
    if (Re > Re3) and (Re <= Re4):
      Rez1 = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
      Rez = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez1**0.5))+(Delta/3.7)))**2.0))
      while (abs(Rez-Rez1) > Eps):
        Rez1 = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez**0.5)))+(Delta/3.7)))**2.0)
        Rez = Rez1
    if (Re > Re4):
      Rez = 1.0/(2.0*numpy.log10(3.7/Delta))
  if (Delta > 0.00135) and (Delta <= 0.002789):
    if (Re >= 0.0) and (Re <= Re01):
      Rez = 64.0/Re
    if (Re > Re01) and (Re <= Re2):
      LambdaG = 0.032
      Lambda2 = 7.244*(Re2**(-0.643))
      Rez = (Lambda2-LambdaG)*numpy.exp(-((0.0017*(Re2-Re))**2.0))+LambdaG
    if (Re > Re2) and (Re <= 4000.0):
      LambdaG = 0.032
      Lambda2 = 7.244*(Re2**(-0.643))
      LambdaRe2 = (Lambda2-LambdaG)*numpy.exp(-((0.0017*(Re2-Re))**2.0))+LambdaG
      Lambda4000 = 1.0/((1.8*numpy.log10(4000.0)-1.64)**2.0)
      Rez = LambdaRe2*(4000.0-Re)/(4000.0-Re2)+Lambda4000*(Re-Re2)/(4000.0-Re2)
    if (Re > 4000.0) and (Re <= Re3):
      Rez = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
    if (Re > Re3) and (Re <= Re4):
      Rez1 = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
      Rez = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez1**0.5)))+(Delta/3.7)))**2.0)
      while (abs(Rez-Rez1) > Eps):
        Rez1 = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez**0.5)))+(Delta/3.7)))**2.0)
        Rez = Rez1
    if (Re > Re4):
      Rez = 1.0/(2.0*numpy.log10(3.7/Delta))
  if (Delta > 0.002789) and (Delta <= 0.007):
    if (Re > 0.0) and (Re <= Re01):
      Rez = 64.0/Re
    if (Re > Re01) and (Re <= Re2):
      LambdaG = 0.032
      Lambda2 = 7.244*(Re2**(-0.643))
      Rez = (Lambda2-LambdaG)*numpy.exp(-((0.0017*(Re2-Re))**2.0))+LambdaG
    if (Re > Re2) and (Re <= 4000.0):
      LambdaG = 0.032
      Lambda2 = 7.244*(Re2**(-0.643))
      LambdaRe2 = (Lambda2-LambdaG)*numpy.exp(-((0.0017*(Re2-Re))**2.0))+LambdaG
      LambdaRez1 = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
      LambdaRez = 1.0/((2.0*numpy.log10((2.51/(Re*(LambdaRez1**0.5)))+(Delta/3.7)))**2.0)
      while (abs(LambdaRez-LambdaRez1) > Eps):
        LambdaRez1 = 1.0/((2.0*numpy.log10((2.51/(Re*(LambdaRez**0.5)))+(Delta/3.7)))**2.0)  
        LambdaRez = LambdaRez1
      Lambda4000 = LambdaRez
      Rez = LambdaRe2*(4000.0-Re)/(4000.0-Re2)+Lambda4000*(Re-Re2)/(4000.0-Re2)
    if (Re > 4000.0) and (Re <= Re4):
      Rez1 = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
      Rez = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez1**0.5)))+(Delta/3.7)))**2.0)
      while (abs(Rez-Rez1) > Eps):
        Rez1 = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez**0.5)))+(Delta/3.7)))**2.0)
        Rez = Rez1
    if (Re > Re4):
      Rez = 1.0/(2.0*numpy.log10(3.7/Delta))
  if (Delta > 0.007):
    if (Re > 0.0) and (Re <= Re0):
      Rez = 64.0/Re
    if (Re > Re0) and (Re <= Re1):
      Rez = 4.4*(Re**(-0.595))*(numpy.exp(-(0.00275/Delta)))
    if (Re > Re1) and (Re <= Re2):
      Lambda1 = 0.0775-(0.0109/(Delta**0.286))
      Lambda2 = 0.145/(Delta**(-0.244))
      LambdaG = Lambda1-0.0017
      Rez = (Lambda2-LambdaG)*numpy.exp(-((0.0017*(Re2-Re))**2.0))+LambdaG
    if (Re > Re2) and (Re <= 4000.0):
      Lambda1 = 0.0775-(0.0109/(Delta**0.286))
      Lambda2 = 0.145/(Delta**(-0.244))
      LambdaG = Lambda1-0.0017
      LambdaRe2 = (Lambda2-LambdaG)*numpy.exp(-((0.0017*(Re2-Re))**2.0))+LambdaG
      LambdaRez1 = 1.0/((1.8*numpy.log10(4000.0)-1.64)**2.0)
      LambdaRez = 1.0/((2.0*numpy.log10((2.51/(4000.0*(LambdaRez1**0.5)))+(Delta/3.7)))**2.0)
      while (abs(LambdaRez-LambdaRez1) > Eps):
        LambdaRez1 = 1.0/((2.0*numpy.log10((2.51/(4000.0*(LambdaRez**0.5)))+(Delta/3.7)))**2.0)  
        LambdaRez = LambdaRez1
      Lambda4000 = LambdaRez
      Rez = LambdaRe2*(4000.0-Re)/(4000.0-Re2)+Lambda4000*(Re-Re2)/(4000.0-Re2)
    if (Re > 4000.0) and (Re <= Re4):
      Rez1 = 1.0/((1.8*numpy.log10(Re)-1.64)**2.0)
      Rez = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez1**0.5)))+(Delta/3.7)))**2.0)
      while (abs(Rez-Rez1) > Eps):
        Rez1 = 1.0/((2.0*numpy.log10((2.51/(Re*(Rez**0.5)))+(Delta/3.7)))**2.0)
        Rez = Rez1
    if (Re > Re4):
      Rez = 1.0/(2.0*numpy.log10(3.7/Delta))
  return Rez

@xlfunc
def f_b_004_f_16_Alfa01(Re,Pr,dn,s1,s2,z2,Lambda):
  '''Alfa01 - flow between tube, 1998 NTR  '''
  Sigma1 = s1/dn
  Sigma2 = s2/dn
  Sigma2d = ((0.25*(Sigma1**2)+(Sigma2**2))**0.5)
  PhiSigma = (Sigma1-1)/(Sigma2d-1)
# Cs
  if (PhiSigma > 0.1)and (PhiSigma <=1.7):  
    Cs = 0.95*(PhiSigma**0.1)
  if (PhiSigma > 1.7) and (PhiSigma <= 4.5):
    if Sigma1 < 3.0:
      Cs = 0.77*(PhiSigma**0.5)
    if Sigma1 >= 3.0:
      Cs = 0.95*(PhiSigma**0.1)
# Cz  
  if (z2 < 10.0) and (Sigma1 < 3.0):
    Cz = 3.12*(z2**0.05)-2.5
  if (z2 < 10.0) and (Sigma1 >= 3.0):
    Cz = 4*(z2**0.02)-3.2
  if z2 >= 10.0:
    Cz = 1.0
# Nu
  Nu = 0.36*(Re**0.6)*(Pr**0.33)
# Alfa
  Alfa = Nu*Lambda*Cs*Cz/dn
  return Alfa

@xlfunc
def f_b_004_f_17_Alfa02(Re0,Pr,d,L,Delta,Lambda):
  '''Alfa02 - flow in tube, Gnilinsky '''
  Re = Re0*L/d
  Nu_L_force_Lam = ((2.0**0.5)*((((0.798*(Pr**0.5))**(-4.0))+((0.479*(Pr**(1.0/3.0)))**(-4.0)))**(-0.25)))*(Re**0.5)
  if (Pr >= 0.5):
    Nu_L_force_Turb = (0.037*(Re**0.8)*(Pr**0.4))
  else: Nu_L_force_Turb = 0.037*((Re*Pr)**0.8)
  Nu_L_force = ((Nu_L_force_Lam**4.0)+(Nu_L_force_Turb**4.0))**0.25  
  Nu_d_beg = Nu_L_force*d/L
  if (Pr > 0.6):
    if (Re < 1000.0):
      Nu_d_Turb_inf = 0.0
    else:
      Dzetta = f_b_004_f_15_LambdaGidr(Re,Delta)
      Nu_d_Turb_inf = (Dzetta/8.0)*(Re-1000.0)*Pr/(1.0+12.7*((Dzetta/8.0)**0.5)*((Pr**(2.0/3.0))-1))
  else:
    Nu_d_Turb_inf = 0.021*((Re*Pr)**0.8)  
  Nu_d_Lam_inf = 4.0
  Nu_d_inf = ((Nu_d_Lam_inf**4.0)+(Nu_d_Turb_inf**4.0))**0.25
  Nu_d = ((Nu_d_beg**4.0)+(Nu_d_inf**4.0))**0.25
# Alfa
  Alfa = Nu_d*Lambda/L
  return Alfa

@xlfunc
def f_b_004_f_18_DzettaChessBundle(d,s1,s2,z2,Re):
  '''The drag coefficient of chess tube bundle cube of air heater'''
  Sigma1 = s1/d
  s2d = (0.25*(s1**2.0)+(s2**2.0))**0.5
  Phi = (s1-d)/(s2d-d)
  Dzetta0 = 0.0
  if (Phi >= 0.1) and (Phi <= 1.7):
    if (Sigma1 >= 1.44):
      Cs = 3.2+0.66*(1.7-Phi)**1.5
    if Sigma1 < 1.44:
      Cs = 3.2+0.66*(1.7-Phi)**1.5+(1.44-Sigma1)*(0.8+0.2*(1.7-Phi)**1.5)/0.11
  if (Phi > 1.7) and (Phi <= 6.5):
    if (Sigma1 >= 1.44) and (Sigma1 <= 3.0):
      Cs = 0.44*(Phi+1)**2.0
    if (Sigma1 < 1.44):
      Cs = (0.44+(1.44-Sigma1))*(Phi-1.0)**2.0
  Dzetta0 = Cs*Re**(-0.27)
  if (Phi >= 1.7) and (Sigma1 > 3.0) and (Sigma1 <= 10):
    Dzetta0 = 1.83*Sigma1**(-1.46)
  Rez = Dzetta0*(z2+1.0)
  return Rez

@xlfunc
def f_b_004_f_19_DzettaCorridorBundle(d,s1,s2,z2,Re):
  '''The drag coefficient of Corridor tube bundle cube of air heater'''
  Sigma1 = s1/d
  Phi = (s1-d)/(s2-d)
  Dzetta0 = 0.0
  if (Phi >= 0.06) and (Phi <= 1.0):
    Dzetta0 = 2.0*((Sigma1-1)**(-0.5))*(Re**(-0.2))
  if (Phi > 1.0) and (Phi <= 8.0):
    Dzetta0 = 0.38*((Sigma1-1)**(-0.5))*((Phi-0.94)**(-0.59))*(Re**(-0.2/(Phi**2.0)))
  if (Phi > 8.0) and (Phi <= 15.0):
    Dzetta0 = 0.118*((Sigma1-1)**(-0.15))
  Rez = Dzetta0*z2
  return Rez

@xlfunc
def f_b_004_f_20_Reynolds(w,L,Nu):
  '''Reynolds'''
  Rez = w*L/Nu
  return Rez

@xlfunc
def f_b_004_f_21_DragInnerTubeWashingAH(d,DeltaTube,Dzetta,h,zh,Lambda,w,Density):
  '''The aerodynamic drag of the inner tube washing'''
  if (zh == 1.0):
    Rez = (Dzetta+Lambda*zh*h/(d-2.0*DeltaTube))*(w**2.0)*0.5*Density
  else:
    Rez = (Dzetta*(zh-1)+Lambda*zh*h/(d-2.0*DeltaTube))*(w**2.0)*0.5*Density
  return Rez

@xlfunc
def f_b_004_f_22_DragOuterTubeWashingAH(Dzetta1,Dzetta2,zh,w,Density):
  '''The aerodynamic drag of the outer tube washing'''
  Rez = (Dzetta1+Dzetta2)*zh*(w**2.0)*0.5*Density
  return Rez

@xlfunc
def f_b_004_f_23_KL(d,DeltaTube,Alfa1, Alfa2, LambdaM):
  '''!!! Внимание, отличие в наружном и внутреннем!!! Надо подумать!!!
  The linear coefficient of heat transfer through the cylindrical wall of the tube'''
  Rez = 1.0/(1.0/(numpy.pi*(d-2.0*DeltaTube)*Alfa1)+(numpy.log(d/(d-2.0*DeltaTube)))/(2.0*numpy.pi*LambdaM)+1.0/(numpy.pi*d*Alfa2))
  return Rez

@xlfunc
def f_b_004_f_24_KLUniversal(d1,d2,Alfa1, Alfa2, LambdaM):
  '''The linear coefficient of heat transfer through the cylindrical wall of the tube
  d1 - Outer Diameter;
  d2 - Inner Diameter;
  Alfa1 - Outer heat trans koeff;
  Alfa2 - Inner heat trans koeff;
  '''
  Rez = 1.0/(1.0/(numpy.pi*d1*Alfa1)+(numpy.log(d1/d2))/(2.0*numpy.pi*LambdaM)+1.0/(numpy.pi*d2*Alfa2))
  return Rez


@xlfunc
def f_b_004_f_25_NuProductCombation(rH2O,Tetta):
  '''Nu for Product Combation, м2/с  '''
  PromZn1 = numpy.interp(Tetta,
                         [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0],
                         [11.9,20.8,31.6,43.9,57.8,73.0,89.4,107.0,126.0,146.0,167.0,188.0,211.0,234.0,258.0,282.0,307.0,333.0,361.0,389.0,419.0,450.0,482.0])*1e-6
  L002 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [0.98, 0.965, 0.95, 0.9425, 0.94, 0.938,0.937,0.935, 0.935])
  L005 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.0, 0.99, 0.98, 0.975, 0.972, 0.97,0.97,0.97, 0.97])
  L010 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.0, 1.0,   1.0, 1.0,  1.0, 0.9985, 0.9975, 0.995, 0.9925])
  L015 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.0,  1.0,  1.005,1.01, 1.015, 1.015, 1.015, 1.015, 1.015])
  L020 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [0.98, 0.99, 1.01, 1.02, 1.025, 1.03,  1.03,  1.03,  1.03])
  L025 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [0.965, 0.99, 1.005, 1.017, 1.03, 1.038, 1.04, 1.0425,1.045])
  L029 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [0.955,0.975,1.005,1.025,1.04,  1.05,  1.05,  1.05,  1.05])
  PromZn2 = numpy.interp(rH2O,
                         [0.02,0.05,0.10,0.15,0.20,0.25,0.29],
                         [L002,L005,L010,L015,L020,L025,L029])
  Rez = PromZn1*PromZn2  
  return Rez

@xlfunc
def f_b_004_f_26_NuAir(t):
  '''Nu for Air, м2/с  '''
  Rez = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0],
                     [13.6,23.5,35.3,48.9,63.8,73.2,98.0,116.0,136.0,157.0,179.0,202.0,226.0,247.0,277.0,300.0,331.0,355.0,390.0,415.0,445.0,478.0,511.0])*1e-6
  return Rez

@xlfunc
def f_b_004_f_27_PrProductCombation(rH2O,Tetta):
  '''Pr for Product Combation  '''
  PromZn1 = numpy.interp(Tetta,
                         [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0],
                         [0.74,0.7,0.67,0.65,0.64,0.62,0.61,0.6,0.59,0.58,0.58,0.57,0.56,0.55,0.54,0.53,0.52,0.51,0.5,0.49,0.49,0.48,0.47])
  PromZn2 = numpy.interp(rH2O,
                         [0.0,0.05,0.10,0.15,0.20,0.25,0.27],
                         [0.94,0.965,0.995,1.025,1.055,1.09,1.11])
  Rez = PromZn1*PromZn2  
  return Rez

@xlfunc
def f_b_004_f_28_PrAir(t):
  '''Pr for Air  '''
  Rez = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0],
                     [0.7, 0.69,0.69,0.69,0.7,0.7,0.71,0.71,0.72,0.72,0.72,0.72,0.73,0.73,0.73,0.73,0.74,0.74,0.74,0.74,0.74,0.75,0.75])
  return Rez

@xlfunc
def f_b_004_f_29_LambdaProductCombation(rH2O,Tetta):
  '''Lambda (Termoconduction) for Product Combation, Вт/(м*К)  '''
  PromZn1 = numpy.interp(Tetta,
                         [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0],
                         [2.27,3.12,4.0,4.82,5.68,6.54,7.4,8.25,9.13,9.99,10.87,11.72,12.53,13.46,14.38,15.31,16.24,17.28,18.1,18.91,19.84,20.65,21.58])*1e-2
  L003 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [0.97,0.945,0.93,0.915,0.905,0.895,0.891,0.89,0.89])
  L005 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [0.99,0.965,0.95,0.945,0.94,0.935,0.93,0.93,0.93])
  L007 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.0,0.98,0.97,0.965,0.96,0.9525,0.9505,0.9505,0.9505])
  L009 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.0,1.0,0.995,0.995,0.99,0.982,0.975,0.975,0.975])
  L011 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
  L013 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.005,1.005,1.0075,1.01,1.012,1.015,1.015,1.015,1.015])
  L015 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.005,1.015,1.02,1.025,1.03,1.03,1.03,1.03,1.03])
  L017 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.005,1.015,1.02,1.025,1.03,1.04,1.045,1.05,1.05])
  L019 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.01,1.03,1.04,1.05,1.055,1.06,1.06,1.06,1.06])
  L021 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.01,1.035,1.05,1.06,1.07,1.0725,1.075,1.075,1.075])
  L023 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.01,1.04,1.06,1.07,1.075,1.08,1.085,1.09,1.09])
  L025 = numpy.interp(Tetta,
                      [0.0,200.0,400.0,600.0,800.0,1000.0,1200.0,1400.0,1600.0],
                      [1.02,1.045,1.065,1.08,1.085,1.09,1.095,1.1,1.1])
  PromZn2 = numpy.interp(rH2O,
                         [0.03,0.05,0.07,0.09,0.11,0.13,0.015,0.17,0.19,0.21,0.23,0.25],
                         [L003,L005,L007,L009,L011,L013,L015, L017,L019,L021,L023,L025])
  Rez = PromZn1*PromZn2  
  return Rez

@xlfunc
def f_b_004_f_30_LambdaAir(t):
  '''Lambda (Termoconduction) for Air, Вт/(м*К)  '''
  Rez = numpy.interp(t,
                     [0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0],
                     [2.42,3.18,3.89,4.47,5.03,5.6,6.14,6.65,7.12,7.59,8.03,8.44,8.85,9.24,9.63,10.0,10.36,10.72,11.08,11.43,11.83,12.06,12.41])*1e-2
  return Rez


@xlfunc
def f_b_004_f_31_dtlog(TypeFlow,tt1,tt2,t1,t2):
  '''DeltaT of heater.
  TypeFlow:
  0 - Countercurrent;
  1 - Cocurrent.'''
  Rez = 0.0
  if TypeFlow == 0.0:
      dt1 = float(tt1-t2)
      dt2 = float(tt2-t1)
  if TypeFlow == 1.0:
      dt1 = float(tt1-t1)
      dt2 = float(tt2-t2)
  if dt1 == dt2:
      Rez = 0.0
  if (dt1 != 0.0) and (dt2 !=0.0):
    if dt1 > dt2 and (numpy.log(dt1/dt2)!=0.0):
      Rez = (dt1-dt2)/numpy.log(dt1/dt2)
    if dt1 < dt2 and (numpy.log(dt2/dt1)!=0.0):
      Rez = (dt2-dt1)/numpy.log(dt2/dt1)
  return float(Rez)


@xlfunc
def f_b_004_f_32_psiAH(Nsch,tt1,tt2,t1, t2):
  '''Psi in AitHeater
  Nsch - Number Of scheme:
  '''
  Psi = 1.0
  TayMin = float(min((tt1-tt2),(t2-t1)))
  TayMax = float(max((tt1-tt2),(t2-t1)))
  P = 0.0  
  if (tt1-t1) != 0.0:
    P = TayMin/(tt1-t1)
  R = 0.0
  if TayMin != 0.0:
    R = TayMax/TayMin

  L10 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,
                     6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.7,11.4,12.1,12.8,
                     13.5,14.2,14.9,15.6,16.3,17.0,18.5,20.0,21.5,23.0,
                     24.5,26.0,27.5,29.0,30.5,32.0,35.1,38.2,41.3,44.4,
                     47.5,50.6,53.7,56.8,59.9,63.0,68.4,73.8,79.2,84.6,
                     90.0,95.4,100.8,106.2,111.6,117.0,128.3,139.6,150.9,
                     162.2,173.5,184.8,196.1,207.4,218.7,250.0,276.67,
                     303.33,330.0,330.0,330.0])
  L12 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,0.6,1.2,1.8,2.4,3,3.6,4.2,4.8,5.4,6,6.6,7.2,7.8,
                     8.4,9,9.6,10.2,10.8,11.4,12,13,14,15,16,17,18,19,
                     20,21,22,24.3,26.6,28.9,31.2,33.5,35.8,38.1,40.4,
                     42.7,45,49.5,54,58.5,63,67.5,72,76.5,81,85.5,90,101.5,
                     113,124.5,136,147.5,159,170.5,182,193.5,205,230,255,
                     280,305,330,330,330,330,330,330,330,330,330,330,
                     330])
  L14 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0.0,0.75,1.5,2.25,3.0,3.75,4.5,5.25,6.0,6.75,7.5,
                     8.25,9.0,9.75,10.5,11.25,12.0,12.75,13.5,14.25,15.0,
                     16.5,18.0,19.5,21.0,22.5,24.0,25.5,27.0,28.5,30.0,
                     33.5,37.0,40.5,44.0,47.5,51.0,54.5,58.0,61.5,65.0,
                     73.5,82.0,90.5,99.0,107.5,116.0,124.5,133.0,141.5,
                     150.0,172.5,195.0,217.5,240.0,262.5,285.0,307.5,330.0,
                     330.0,330.0,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330])
  L16 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,0.9,1.8,2.7,3.6,4.5,5.4,6.3,7.2,8.1,9,9.9,10.8,
                     11.7,12.6,13.5,14.4,15.3,16.2,17.1,18,19.8,21.6,23.4,
                     25.2,27,28.8,30.6,32.4,34.2,36,41.6,47.2,52.8,58.4,
                     64,69.6,75.2,80.8,86.4,92,111.8,131.6,151.4,171.2,
                     191,210.8,230.6,250.4,270.2,290,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330])
  L18 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
                     20,22,24,26,28,30,34,38,42,46,50,57,64,71,78,85,98,
                     111,124,137,150,170,192,220,270,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,
                     330])
  L20 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,11,12.1,13.2,
                     14.3,15.4,16.5,17.6,18.7,19.8,20.9,22,25,28,31,34,
                     37,42.6,48.2,53.8,59.4,65,77,89,101,113,125,150,175,
                     200,250,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330])
  L22 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17.4,19.8,22.2,
                     24.6,27,32.6,38.2,43.8,49.4,55,64,73,82,91,100,116.67,
                     133.33,150,200,250,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330])
  L24 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1.25,2.5,3.75,5,6.25,7.5,8.75,10,11.25,12.5,13.75,
                     15,16.25,17.5,18.75,20,23.75,27.5,31.25,35,40,45,50,
                     60,70,80,95,110,137.5,165,230,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330])
  L26 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1,2,3,4,5,6,7,8,9,10,12.4,14.8,17.2,19.6,22,26.6,
                     31.2,35.8,40.4,45,52.5,60,70,80,100,120,150,200,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330])
  L28 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1.2,2.4,3.6,4.8,6,7.2,8.4,9.6,10.8,12,14.6,17.2,
                     19.8,22.4,25,30,35,40,50,60,70,85,100,135,180,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330])
  L30 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1.5,3,4.5,6,7.5,9,10.5,12,13.5,15,18.4,21.8,25.2,
                     28.6,32,38.5,45,56.67,68.33,80,100,130,170,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330])
  L35 = numpy.interp(R,
                    [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,1.67,3.33,5,6.67,8.33,10,12,14,16,18,22,27,33,40,
                     55,95,130,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330])
  L40 = numpy.interp(R,
                     [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,
                     0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,
                     0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,
                     0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,
                     0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,
                     0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,
                     0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,
                     0.8,0.81,0.82,0.83,0.84,0.85],
                    [0,2,4,6,8,10,13,16,19,22,25,30,40,50,70,90,130,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330,330,330,330,330,330,330,330,
                     330,330,330,330,330,330])
  PromZn = numpy.interp(P,
                        [1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.5,4.0],
                        [L10,L12,L14,L16,L18,L20,L22,L24,L26,L28,L30,L35,L40])
                        
  N1 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.97,0.94,0.91,0.875,0.85,0.825,0.8,0.7783,0.7567,
                     0.735,0.715,0.6975,0.68,0.6625,0.645,0.63,0.615,0.6,0.6,
                     0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,
                     0.6])
  N2 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.987,0.974,0.961,0.948,0.935,0.92,0.905,0.89,0.875,
                     0.86,0.844,0.828,0.812,0.796,0.78,0.768,0.756,0.744,
                     0.732,0.72,0.708,0.696,0.684,0.672,0.66,0.648,0.636,
                     0.624,0.612,0.6,0.6,0.6,0.6])
  N3 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.994,0.988,0.982,0.976,0.97,0.963,0.956,0.949,
                     0.942,0.935,0.926,0.917,0.908,0.899,0.89,0.88,0.87,
                     0.86,0.85,0.84,0.828,0.816,0.804,0.792,0.78,0.768,
                     0.756,0.744,0.732,0.72,0.7067,0.693,0.68])
  N4 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.996,0.993,0.989,0.986,0.982,0.979,0.975,0.971,
                     0.968,0.964,0.961,0.957,0.954,0.95,0.945,0.941,0.936,
                     0.931,0.926,0.922,0.917,0.912,0.907,0.903,0.898,0.893,
                     0.888,0.884,0.879,0.874,0.869,0.865,0.86])
  N5 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.994,0.988,0.982,0.976,0.97,0.964,0.958,0.952,
                     0.946,0.94,0.934,0.928,0.922,0.916,0.91,0.904,0.898,
                     0.892,0.886,0.88,0.872,0.864,0.856,0.848,0.84,0.832,
                     0.824,0.816,0.808,0.8,0.7917,0.7833,0.775])
  N6 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.991,0.982,0.973,0.964,0.955,0.949,0.943,0.937,
                     0.931,0.925,0.919,0.913,0.907,0.901,0.895,0.889,0.883,
                     0.877,0.871,0.865,0.86,0.855,0.85,0.845,0.84,0.832,
                     0.824,0.816,0.808,0.8,0.7933,0.7867,0.78])
  N7 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.993,0.986,0.979,0.972,0.965,0.958,0.951,0.944,
                     0.937,0.93,0.924,0.918,0.912,0.906,0.9,0.895,0.89,
                     0.885,0.88,0.875,0.87,0.865,0.86,0.855,0.85,0.846,
                     0.842,0.838,0.834,0.83,0.8267,0.823,0.82])
  N8 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.995,0.99,0.985,0.98,0.975,0.971,0.967,0.963,
                     0.959,0.955,0.95,0.945,0.94,0.935,0.93,0.926,0.922,
                     0.918,0.914,0.91,0.905,0.9,0.895,0.89,0.885,0.88,
                     0.875,0.87,0.865,0.86,0.855,0.85,0.845])
  N9 = numpy.interp(PromZn,
                     [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,
                      160,170,180,190,200,210,220,230,240,250,260,270,280,
                      290,300,310,320,330],
                    [1.0,0.997,0.994,0.991,0.988,0.985,0.981,0.977,0.973,
                     0.969,0.965,0.962,0.959,0.956,0.953,0.95,0.948,0.946,
                     0.944,0.942,0.94,0.938,0.936,0.934,0.932,0.93,0.928,
                     0.926,0.924,0.922,0.92,0.9183,0.9167,0.915])

  Psi = numpy.interp(Nsch,
                     [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
                     [N1, N2, N3, N4, N5, N6, N7, N8, N9])
  return Psi


@xlfunc
def f_b_004_f_33_dtlogAH(TypeFlow,Nsch,tt1,tt2,t1, t2):
  '''DeltaT of AitHeater
  TypeFlow:
  0 - Countercurrent;
  1 - Cocurrent.
  Nsch - Number Of scheme:
  '''
  Psi = f_b_004_f_32_psiAH(Nsch,tt1,tt2,t1, t2)
  Rez = 0.0
  if TypeFlow == 0.0:
    Rez = Psi*f_b_004_f_31_dtlog(TypeFlow,tt1,tt2,t1,t2)
  if TypeFlow == 1.0:
    dtysl = 0.0  
    if (tt2-t1)>(tt1-t2):
      if ((tt1-t2) != 0.0) and (numpy.log((tt2-t1)/(tt1-t2))!=0.0):
        dtysl = ((tt2-t1)-(tt1-t2))/numpy.log((tt2-t1)/(tt1-t2))
    if (tt2-t1)<=(tt1-t2):
      if (tt2-t1) != 0.0 and (numpy.log((tt1-t2)/(tt2-t1)) !=0.0):
        dtysl = ((tt1-t2)-(tt2-t1))/numpy.log((tt1-t2)/(tt2-t1))
    Rez = Psi*dtysl
  return float(Rez)

































