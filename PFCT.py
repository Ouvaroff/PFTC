import pandas as pd
import math as mt
from prettytable import PrettyTable

x1 = PrettyTable()

x1.field_names = ["Programm for toxicological calculation (PFTC)"]
x1.add_row(["Start calculation"])
x1.add_row(["Working area air"])

x1.align["Programm for toxicological calculation (PFTC)"] = "e"
x1.border = True
x1.header = True
x1.padding_width = 1

print(x1)

filename = f'result_of_calculation.txt'

#VDK
#Working area air

    #Methods of correlation analysis

table_1 = pd.DataFrame()

# Создание таблицы с данными
x1 = PrettyTable()

x1.field_names = ["Класс или группа соединений","Номер класса соединений"]
x1.add_row(["Кетоны непредельные алифатические",0])
x1.add_row(["Хлоруглеводороды непредельные с одной или двумя двойными связями",1])
x1.add_row(["Бромуглеводроды",2])
x1.add_row(["Эфиры простые алифатические непредель-ные",3])
x1.add_row(["Углеводороды алифатические, циклические, ароматические с непредельной связью в от-крытой цепи",4])
x1.add_row(["Гетероциклические соединения, хлоруглево-дороды алифатические предельные, эфиры сложные хлорированные",5])
x1.add_row(["Нитросоединения алифатические с тремя или четырьмя группами NO2, а также некоторые динитроароматические соединения",6])
x1.add_row(["Фторированные органические кислоты",7])
x1.add_row(["Амины, углеводороды предельные алифатические, эфиры предельные простые алифатические, эфиры сложные (без фосфора)",8])
x1.add_row(["Нитросоединения",9])
x1.add_row(["Ацетаты и акрилаты, органические кислоты и их ангидриды, хлорангидриды органических кислот, хлорбензолы, хлорксилолы, хлорнафталины за исключением гексахлорбензола",10])
x1.add_row(["Кетоны предельные алифатические",11])
x1.add_row(["Спирты предельные алифатические, фенолы без непредельных боковых цепей",12])
x1.add_row(["Спирты непредельные алифатические с одной двойной связью",13])
x1.add_row(["Спирты непредельные алифатические с двумя двойными или одной тройной связью",14])
x1.add_row(["Альдегиды",15])
x1.add_row(["Нитриты, цианиды, изоцианаты, соединения, содержащие CN или CN",16])

x1.align["Класс или группа соединений"] = "e"
x1.align["Номер класса соединений"] = "e"
x1.border = True
x1.header = True
x1.padding_width = 1

print(x1)
#VDK Calculation_CL50

cl50 = int(input("Выберите класс соединений из таблицы:"))
cl50_v = float(input("Ваше значение CL50:"))
M = float(input("Введите молекулярную массу вещества с точностью до 3 знака после запятой:"))

if cl50 == 0:
    eq_1 = 0.015*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 1:
    eq_1 = 0.2*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 2:
    eq_1 = 0.25*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 3:
    eq_1 = 0.3*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 4:
    eq_1 = 0.4*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 5:
    eq_1 = 0.5*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 6:
    eq_1 = 0.63*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 7:
    eq_1 = 0.45*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 8:
    eq_1 = cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 9:
    eq_1 = 2.0*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 10:
    eq_1 = 2.5*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 11:
    eq_1 = 8.0*cl50_v
    print("Значение ВДК:",eq_1)
elif cl50 == 12:
    step_1 = 0.286 * mt.log10(cl50_v) - 0.75 + mt.log10(M)
    eq_1 = 10**(step_1)
    print("Значение ВДК:",eq_1)
elif cl50 == 13:
    step_1 = 0.286 * mt.log10(cl50_v) - 1.10 + mt.log10(M)
    eq_1 = 10**(step_1)
    print("Значение ВДК:",eq_1)
elif cl50 == 14:
    step_1 = 0.286 * mt.log10(cl50_v) - 1.35 + mt.log10(M)
    eq_1 = 10**(step_1)
    print("Значение ВДК:",eq_1)
elif cl50 == 15:
    step_1 = 0.53 * mt.log10(cl50_v) - 0.91 + mt.log10(M)
    eq_1 = 10**(step_1)
    print("Значение ВДК:",eq_1)
elif cl50 == 16:
    step_1 = 0.78 * mt.log10(cl50_v) - 0.67 + mt.log10(M)
    eq_1 = 10**(step_1)
    print("Значение ВДК:",eq_1)

with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКрз по методу CL50:{(eq_1)}\n")
table_2 = pd.DataFrame()

# Создание таблицы с данными
x2 = PrettyTable()

x2.field_names = ["Класс или группа соединений","Номер класса соединений"]
x2.add_row(["Углеводороды",0])
x2.add_row(["Галогенсодержащие углеводороды",1])
x2.add_row(["Спирты",2])
x2.add_row(["Амины",3])
x2.add_row(["Нитросоединения",4])
x2.add_row(["Гетероциклические соединения",5])
x2.add_row(["Сложные эфиры",6])

x2.align["Класс или группа соединений"] = "e"
x2.align["Номер класса соединений"] = "e"
x2.border = True
x2.header = True
x2.padding_width = 1

print(x2)
#VDK Calculation_DL50ж

dl50 = int(input("Выберите класс соединений из таблицы:"))
dl50_v = float(input("Ваше значение DL50ж:"))

if dl50 == 0:
    eq_2 = 0.016*dl50_v
    print("Значение ВДК:",eq_2)
elif dl50 == 1:
    eq_2 = 0.001*dl50_v
    print("Значение ВДК:",eq_2)
elif dl50 == 2:
    eq_2 = 0.0025*dl50_v
    print("Значение ВДК:",eq_2)
elif dl50 == 3:
    eq_2 = 0.005*dl50_v
    print("Значение ВДК:",eq_2)
elif dl50 == 4 or dl50 == 5 or dl50 == 6:
    eq_2 = 0.002*dl50_v
    print("Значение ВДК:",eq_2)

with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКрз по методу DL50ж:{(eq_2)}\n")
    #By the biological activity of chemical bonds

table_3 = pd.DataFrame()

# Создание таблицы с данными
x = PrettyTable()

x.field_names = ["Химическая связь","Класс соединений","Номер класса соединений"]
x.add_row(["-=C - H","Предельные, непредельные циклические, нецикли-ческие углеводороды",0])
x.add_row(["-=C - H","Предельные альдегиды (у карбонильной группы)",1])
x.add_row(["-=C - C=-","Предельные нециклические углеводороды",2])
x.add_row(["-=C - C=-","Предельные циклические углеводороды",3])
x.add_row(["=C=C= (обычная)","Непредельные нециклические углеводороды",4])
x.add_row(["=C=C= (сопрояжённая)","То же",5])
x.add_row(["=C=C=","Незамещенные ароматические углеводороды",6])
x.add_row(["=C=C=","Замещенные ароматические углеводороды с одной или двумя боковыми цепями",7])
x.add_row(["=C=C=","Замещенные ароматические углеводороды с непре-дельной боковой цепью",8])
x.add_row(["-C-=C-","Непредельные углеводороды с тройной связью",9])
x.add_row(["==N-O-","Оксиды азота",10])
x.add_row(["-=N=O","То же",11])
x.add_row(["-=C-N==","Нитросоединения алифатического ряда",12])
x.add_row(["-=C-N==","Нитросоединения алифатического ряда из тетра-нитрометана",13])
x.add_row(["-=C-N==","Циклические мононитросоединения",14])
x.add_row(["-=C-N==","Ароматические мононитросоединения",15])
x.add_row(["-=C-N==","Ароматические динитросоединения",16])
x.add_row(["-=C-N==","Ароматические тринитросоединения",17])
x.add_row(["-=C-N==","Первичные алифатические амины",18])
x.add_row(["-=C-N==","Вторичные алифатические амины",19])
x.add_row(["-=C-N==","Третичные алифатические амины",20])
x.add_row(["-=C-N==","Алифатические диамины",21])
x.add_row(["-=C-N==","Циклические амины",22])
x.add_row(["-=C-N==","Ароматические амины",23])
x.add_row(["-=C-N==","Амиды",24])
x.add_row(["-=C-N==","Гетероциклические соединения",25])
x.add_row(["=N-H","Аммиак",26])
x.add_row(["-C-=N","Цианиды",27])
x.add_row(["=N-N=","Неорганические амины",28])
x.add_row(["C=O","Оксид углерода",29])
x.add_row(["=C=O","Предельные кетоны",30])
x.add_row(["=C=O","Циклические предельные кетоны",31])
x.add_row(["=C=O","Предельные альдегиды (связь у карбонильной группы)",32])
x.add_row(["-=C-O-","Алифатические простые эфиры",33])
x.add_row(["-=C-O-","Нециклические оксиды",34])
x.add_row(["-=C-O-","Гетероциклические оксиды",35])
x.add_row(["-=C-O-","Сложные эфиры предельных спиртов",36])
x.add_row(["-=C-O-","Сложные эфиры непредельных спиртов",37])
x.add_row(["-O-H","Органические кислоты",38])
x.add_row(["-O-H","Одноатомные предельные спирты",39])
x.add_row(["-O-H","Непредельные спирты",40])
x.add_row(["-O-H","Ароматические спирты",41])
x.add_row(["=C=N-","Алифатические изоцианиды",42])
x.add_row(["=C=N-","Ароматические изоцианиды",43])
x.add_row(["=C=N-","Гетероциклические соединения",44])


x.align["Химическая связь"] = "e"
x.align["Класс соединений"] = "e"
x.align["Номер класса соединений"] = "e"
x.border = True
x.header = True
x.padding_width = 1

print(x)

chem_b1 = int(input("Количество связей -=С-H :"))
if chem_b1 != 0:
    what_J_b1 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b1 == 0:
        Ji_b1 = 0.8
    elif what_J_b1 == 1:
        Ji_b1 = 21273.9
else:
    Ji_b1 = 0

chem_b2 = int(input("Количество связей -=C - C=- :"))
if chem_b2 != 0:
    what_J_b2 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b2 == 2:
        Ji_b2 = 51.4
    elif what_J_b2 == 3:
        Ji_b2 = 173.7
else:
    Ji_b2 = 0

chem_b3 = int(input("Количество связей =C=C= (обычная) :"))
Ji_b3 = 451.8

chem_b4 = int(input("Количество связей =C=C= (сопрояжённая) :"))
Ji_b4 = 242.4

chem_b5 = int(input("Количество связей =C=C= :"))
if chem_b5 != 0:
    what_J_b5 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b5 == 6:
        Ji_b5 = 1126.5
    elif what_J_b5 == 7:
        Ji_b5 = 507.9
    elif what_J_b5 == 8:
        Ji_b5 = 7057.9
else:
    Ji_b5 = 0

chem_b6 = int(input("Количество связей -C-=C- :"))
Ji_b6 = 2097.1

chem_b7 = int(input("Количество связей ==N-O- :"))
Ji_b7 = 2230.3

chem_b8 = int(input("Количество связей -=N=O :"))
Ji_b8 = 4460.6

chem_b9 = int(input("Количество связей -=C-N== :"))
if chem_b9 != 0:
    what_J_b9 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b9 == 12:
        Ji_b9 = -6242.7 
    elif what_J_b9 == 13:
        Ji_b9 = 154446.3
    elif what_J_b9 == 14:
        Ji_b9 = 119027.3
    elif what_J_b9 == 15:
        Ji_b9 = 27970.0
    elif what_J_b9 == 16:
        Ji_b9 = 77851.5
    elif what_J_b9 == 17:
        Ji_b9 = 66442.0
    elif what_J_b9 == 18:
        Ji_b9 = 6113.5
    elif what_J_b9 == 19:
        Ji_b9 = 1565.7
    elif what_J_b9 == 20:
        Ji_b9 = 3266.2
    elif what_J_b9 == 21:
        Ji_b9 = 35914.6
    elif what_J_b9 == 22:
        Ji_b9 = 97551.4
    elif what_J_b9 == 23:
        Ji_b9 = 33302.0
    elif what_J_b9 == 24:
        Ji_b9 = 16680.8
    elif what_J_b9 == 25:
        Ji_b9 = 4817.6 
else:
    Ji_b9 = 0

chem_b10 = int(input("Количество связей =N-H :"))
Ji_b10 = 283.8

chem_b11 = int(input("Количество связей -C-=N :"))
Ji_b11 = 97856.8

chem_b12 = int(input("Количество связей =N-N= :"))
Ji_b12 = 318864.8

chem_b13 = int(input("Количество связей C=O :"))
Ji_b13 = 1400.0

chem_b14 = int(input("Количество связей =C=O :"))
if chem_b14 != 0:
    what_J_b14 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b14 == 30:
        Ji_b14 = 213.8 
    elif what_J_b14 == 31:
        Ji_b14 = 8753.8
    elif what_J_b14 == 32:
        Ji_b14 = -12517.8
else:
    Ji_b14 = 0

chem_b15 = int(input("Количество связей -=C-O- :"))
if chem_b15 != 0:
    what_J_b15 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b15 == 33:
        Ji_b15 = 68.1
    elif what_J_b15 == 34:
        Ji_b15 = 21987.7
    elif what_J_b15 == 35:
        Ji_b15 = 2465.7
    elif what_J_b15 == 36:
        Ji_b15 = 6535.3
    elif what_J_b15 == 37:
        Ji_b15 = 10306.9
else:
    Ji_b15 = 0

chem_b16 = int(input("Количество связей -O-H :"))
if chem_b16 != 0:
    what_J_b16 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b16 == 38:
        Ji_b16 = 8507.9
    elif what_J_b16 == 39:
        Ji_b16 = -21648.2
    elif what_J_b16 == 40:
        Ji_b16 = 100223.6
    elif what_J_b16 == 41:
        Ji_b16 = -5214.5
else:
    Ji_b16 = 0

chem_b17 = int(input("Количество связей =C=N- :"))
if chem_b17 != 0:
    what_J_b17 = int(input("Введите номер класса соединения в соотв. с хим. св.:"))
    if what_J_b17 == 42:
        Ji_b17 = 1664538.3
    elif what_J_b17 == 43:
        Ji_b17 = 139778.4
    elif what_J_b17 == 44:
        Ji_b17 = 9635.2
else:
    Ji_b17 = 0

SUM = chem_b1*Ji_b1 + chem_b2*Ji_b2 + chem_b3*Ji_b3 + chem_b4*Ji_b4 + chem_b5*Ji_b5 + chem_b6*Ji_b6 + chem_b7*Ji_b7 + chem_b8*Ji_b8 + chem_b9*Ji_b9 + chem_b10*Ji_b10 + chem_b11*Ji_b11 + chem_b12*Ji_b12 + chem_b13*Ji_b13 + chem_b14*Ji_b14 + chem_b15*Ji_b15 + chem_b16*Ji_b16 + chem_b17*Ji_b17

total_vdk_rz = (M*1000)/(SUM)
print("Итоговый ВДКрз по методу хим. связей:", total_vdk_rz)

with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКрз по методу хим. связей:{(total_vdk_rz)}\n")

x2 = PrettyTable()

x2.field_names = ["Programm for toxicological calculation (PFTC)"]
x2.add_row(["Atmospheric air of populated areas"])

x2.align["Programm for toxicological calculation (PFTC)"] = "e"
x2.border = True
x2.header = True
x2.padding_width = 1

print(x2)

#Atmospheric air of populated areas

vdk_av_step1_v1 = 0.62*mt.log10(total_vdk_rz) - 1.77
vdk_av_res_v1 = 10**(vdk_av_step1_v1)

vdk_av_step1_v2 = 0.62*mt.log10(cl50_v) - 1.6
vdk_av_res_v2 = 10**(vdk_av_step1_v2)

print("Итоговый ВДКав по методу ПДКрз:", vdk_av_res_v1)
print("Итоговый ВДКав по методу CL50:", vdk_av_res_v2)

with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКав по методу ПДКрз:{(vdk_av_res_v1)}\n")
with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКав по методу CL50:{(vdk_av_res_v2)}\n")

x3 = PrettyTable()

x3.field_names = ["Programm for toxicological calculation (PFTC)"]
x3.add_row(["Water bodies"])

x3.align["Programm for toxicological calculation (PFTC)"] = "e"
x3.border = True
x3.header = True
x3.padding_width = 1

print(x3)

#Water bodies

vdk_hp_step1_v1 = 0.61 * mt.log10(total_vdk_rz) - 1.0
vdk_hp_res_v1 = 10**(vdk_hp_step1_v1)

vdk_hp_step1_v2 = 1.7 * mt.log10(cl50_v) - 2.12
vdk_hp_res_v2 = 10**(vdk_hp_step1_v2)

vdk_hp_step1_v3 = 1.39 * mt.log10(dl50_v) - 4.76
vdk_hp_res_v3 = 10**(vdk_hp_step1_v3)

print("Итоговый ВДКхп по первой формуле:", vdk_hp_res_v1)
print("Итоговый ВДКхп по второй формуле:", vdk_hp_res_v3)
print("Итоговый ВДКхп по третьей формуле:", vdk_hp_res_v3)

with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКхп по первой формуле:{(vdk_hp_res_v1)}\n")
with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКхп по второй формуле:{(vdk_hp_res_v2)}\n")
with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКхп по третьей формуле:{(vdk_hp_res_v3)}\n")

x4 = PrettyTable()

x4.field_names = ["Programm for toxicological calculation (PFTC)"]
x4.add_row(["Food products"])

x4.align["Programm for toxicological calculation (PFTC)"] = "e"
x4.border = True
x4.header = True
x4.padding_width = 1

print(x4)

#Food products

vdk_pr_step1 = 0.13e-2 * mt.log10(dl50_v) + 0.76
vdk_pr_res = 10**(vdk_pr_step1)

vdk_pr_total_v1 = 1.23 + 0.48 * mt.log10(vdk_pr_res)

hlor = int(input("Есть ли в составе Вашего соединения хлор? 0 - нет 1 - да:"))
if hlor == 1:
    vdk_pr_hlor = 2.2 * vdk_hp_res_v1 + 0.33
    print("Итоговый ВДКпр по формуле для хлорорганических в-в:", vdk_pr_hlor)
    with open(filename, 'a') as file:
        file.write(f"Итоговый ВДКпр по формуле для хлорорганических в-в:{(vdk_pr_hlor)}\n")
    vdk_pr_total_v2 = 1.23 + 0.48 * mt.log10(vdk_pr_hlor)
    print("Итоговый ВДКпр почвы для хлорорганических в-в",vdk_pr_total_v2)
    with open(filename, 'a') as file:
        file.write(f"Итоговый ВДКпр почвы для хлорорганических в-в:{(vdk_pr_total_v2)}\n")
else:
    pass

phos = int(input("Есть ли в составе Вашего соединения фосфор? 0 - нет 1 - да:"))
if phos == 1:
    vdk_pr_phos = 1.45 * vdk_hp_res_v1 + 0.68
    print("Итоговый ВДКпр по формуле для форсфорорганических в-в:", vdk_pr_phos)
    with open(filename, 'a') as file:
        file.write(f"Итоговый ВДКпр по формуле для форсфорорганических в-в:{(vdk_pr_phos)}\n")
    vdk_pr_total_v2 = 1.23 + 0.48 * mt.log10(vdk_pr_hlor)
    print("Итоговый ВДКпр почвы для хлорорганических в-в",vdk_pr_total_v2)
    with open(filename, 'a') as file:
        file.write(f"Итоговый ВДКпр почвы для хлорорганических в-в:{(vdk_pr_total_v2)}\n")
else:
    pass

print("Итоговый ВДКпр по общей формуле:", vdk_pr_res)

with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКпр по общей формуле:{(vdk_pr_res)}\n")

print("Итоговый ВДКпр почвы по общей формуле:",vdk_pr_total_v1)
with open(filename, 'a') as file:
    file.write(f"Итоговый ВДКпр почвы по общей формуле:{(vdk_pr_total_v1)}\n")

x5 = PrettyTable()

x5.field_names = ["Programm for toxicological calculation (PFTC)"]
x5.add_row(["End of calculation"])

x5.align["Programm for toxicological calculation (PFTC)"] = "e"
x5.border = True
x5.header = True
x5.padding_width = 1

print(x5)