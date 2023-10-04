
"""
Created on Sat Sep 30 15:46:48 2023

@author: nazarodemchuk
"""

#lab2
import numpy as np
from scipy import stats
import pandas as pd
data = pd.read_csv('Birthweight.csv')

#task1
print("Task 1")
children_height = np.array(data['Length'])
print("Середній зріст дітей:")
print(np.mean(children_height))
print("Медіана:")
print(np.median(children_height))

#task2
print("Task 2")
mom_cig = np.array(data['mnocig'])
dad_cig = np.array(data['fnocig'])
all_cig = mom_cig + dad_cig
print("Чи нормально розподілена кількість сигарет в день:")
print(stats.normaltest(all_cig))
# Виконаємо t-тест
t_statistic, p_value = stats.normaltest(all_cig)
# Визначимо рішення на основі p-значення
alpha = 0.05  # Рівень значущості
if p_value < alpha:
    print("Кількість сигарет в день не розподілена нормально")
else:
    print("(H0 правдива)Кількість сигарет в день розподілена нормально")

# Виведемо результат тесту
print("t-статистика:", t_statistic)
print("p-значення:", p_value)

#task3
print("Task 3")
#Альтернативна гіпотеза є односторонньою (параметр розподілу генеральної сукупності(Birthweight) більше певного значення)
# Розділимо дані на дві групи: матері старше 35 і матері молодше 35
older_mothers = data[data['mage35'] == 1]
younger_mothers = data[data['mage35'] == 0]

# Виконаємо t-тест
t_statistic, p_value = stats.ttest_ind(older_mothers['Birthweight'], younger_mothers['Birthweight'], alternative='less')

# Виведемо результат тесту
print("t-статистика:", t_statistic)
print("p-значення:", p_value)

# Визначимо рішення на основі p-значення
alpha = 0.05  # Рівень значущості
if p_value < alpha:
    print("Є статистично значуща різниця. Діти матерів старше 35 легші")
else:
    print("(H0 правдива)Немає статистично значущої різниці. Вага дітей не залежить від віку матері")
    
#task4
print("Task 4")
# Розділемо дані на два рядки - тривалість вагітності та вага дитини
gestation = data['Gestation']
birthweight = data['Birthweight']

# Використовуємо кореляцію Пірсона
correlation, p_value = stats.pearsonr(gestation, birthweight)

# Виведемо коефіцієнт кореляції та p-значення
print("Коефіцієнт кореляції Пірсона:", correlation)
print("p-значення:", p_value)
