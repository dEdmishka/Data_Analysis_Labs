#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 00:01:26 2023

@author: nazarodemchuk
"""

# lab 4
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('bike.csv')

# Task 1
# Побудувати стовпчикові діаграми, на яких відобразити 

# а) кількість покупців різних професій; 
# Підраховуємо кількість покупців для кожної професії
occupation_counts = data['Occupation'].value_counts()

# Побудова стовпчикової діаграми
plt.figure(figsize=(10, 6))
occupation_counts.plot(kind='bar')
plt.title("Кількість покупців різних професій")
plt.xlabel("Професія")
plt.ylabel("Кількість покупців")
plt.xticks(rotation=0) 
plt.tight_layout()
# Показати діаграму
plt.show()

# б) медіанний дохід покупців різних професій; 
# Групування даних за професією та розрахунок медіанного доходу
median_income_by_occupation = data.groupby('Occupation')['Income'].median().sort_values(ascending=False)
# Побудова стовпчикової діаграми
plt.figure(figsize=(10, 6))
median_income_by_occupation.plot(kind='bar')
plt.title("Медіанний дохід покупців різних професій")
plt.xlabel("Професія")
plt.ylabel("Медіанний дохід")
plt.xticks(rotation=0)  
plt.tight_layout()

# Показати діаграму
plt.show()

# в) середній вік покупців різних професій з розподілом на тих, хто купив велосипед і хто — ні. 
# Групування даних за професією та наявністю велосипеда та розрахунок середнього віку
average_age_by_occupation_and_bike = data.groupby(['Occupation', 'Purchased Bike'])['Age'].mean().unstack()

# Побудова стовпчикової діаграми
plt.figure(figsize=(10, 6))
average_age_by_occupation_and_bike.plot(kind='bar')
plt.title("Середній вік покупців різних професій\nз розподілом на наявність велосипеда")
plt.xlabel("Професія")
plt.ylabel("Середній вік")
plt.xticks(rotation=0)  
plt.legend(title="Купив велосипед", labels=["Ні", "Так"])
plt.tight_layout()
print(average_age_by_occupation_and_bike)
# Показати діаграму
plt.show()


# Task 2
# Побудувати гістограму кількості дітей, загальну і в залежності від покупки велосипеду.

# Поділ даних на тих, хто купив велосипед і тих, хто не купив
bought_bike = data[data['Purchased Bike'] == 'Yes']
did_not_buy_bike = data[data['Purchased Bike'] == 'No']

# Створення графіку та підготовка гістограм для кількості дітей
plt.figure(figsize=(10, 6))

# Гістограма для тих, хто не купив велосипед
plt.hist(did_not_buy_bike['Children'], bins=20, color='red', alpha=0.5, label='Не купили велосипед', edgecolor='black')

# Гістограма для тих, хто купив велосипед
plt.hist(bought_bike['Children'], bins=20, color='blue', alpha=0.5, label='Купили велосипед', edgecolor='black')

# Загальна гістограма (зеленого кольору) - з низькою прозорістю
plt.hist(data['Children'], bins=20, color='green', alpha=0.2, label='Загальна к-сть осіб із вказаною кількість дітей', edgecolor='black')

# Підписи осей та заголовок
plt.title("Гістограма кількості дітей з розподілом за покупкою велосипеду")
plt.xlabel("Кількість дітей")
plt.ylabel("Частота")

# Легенда
plt.legend()

# Показати графік
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()


# Task 3
# Побудувати діаграму розмаху доходу (загальну і в залежності від рівня освіти), визначити чи присутні викиди. 

# Побудова діаграми розмаху для загального доходу
plt.figure(figsize=(10, 6))
plt.boxplot(data['Income'], vert=False)
plt.title("Діаграма розмаху доходу (загальна)")
plt.xlabel("Дохід")
plt.yticks([])
plt.grid(axis='x', alpha=0.75)

# Показати діаграму розмаху загального доходу
plt.show()

# Розділити дані на різні рівні освіти
education_levels = data['Education'].unique()

# Побудова діаграми розмаху для доходу в залежності від рівня освіти
plt.figure(figsize=(10, 6))
boxplot_data = [data[data['Education'] == level]['Income'] 
                for level in education_levels]
print(boxplot_data)
plt.boxplot(boxplot_data, labels=education_levels)
plt.title("Діаграма розмаху доходу в залежності від рівня освіти")
plt.xlabel("Рівень освіти")
plt.ylabel("Дохід")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)

# Показати діаграму розмаху в залежності від рівня освіти
plt.show()
# З діаграм видно що викиди присутні


# 4 
# За допомогою діаграм розсіювання зробити висновки щодо залежності між 
# а) доходами і віком; 

# Діаграма розсіювання доходів і віку
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['Income'])
plt.title("Діаграма розсіювання між віком і доходами")
plt.xlabel("Вік")
plt.ylabel("Дохід")

# Висновок: основну к-сть грошей люди заробляють у віці 23-60, найбільші суми у віці 33-56
# Обчислення коефіцієнта кореляції Пірсона
correlation = data['Age'].corr(data['Income'])
print(f"Коефіцієнт кореляції Пірсона між віком і доходами: {correlation}")

# Показати діаграму розсіювання
plt.show()

# б) кількістю дітей і машин.
# Діаграма розсіювання кількості дітей і кількості машин
plt.figure(figsize=(10, 6))
plt.scatter(data['Children'], data['Cars'])
plt.title("Діаграма розсіювання між кількістю дітей і кількістю машин")
plt.xlabel("Кількість дітей")
plt.ylabel("Кількість машин")

# Обчислення коефіцієнта кореляції Пірсона
correlation = data['Children'].corr(data['Cars'])
print(f"Коефіцієнт кореляції Пірсона між кількістю дітей і кількістю машин: {correlation}")

# Показати діаграму розсіювання
plt.show()

# Висновок: дуже слабка  залежність між кількістю дітей і кількістю машин
