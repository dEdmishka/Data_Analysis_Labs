#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 02:23:08 2023

@author: nazarodemchuk
"""


import pandas as pd

# Читаємо файл HTML і змінюємо назви стовпців
df = pd.read_html('Version 6.html')[0]  # Читаємо першу таблицю з HTML-файлу

# Кількість рядків
print("Кількість рядків: ")
print(len(df))

# Змінюємо назви стовпців
df.columns = ["Index", "DATE", "TEMPmean", "WET", "WINDspeed", "PRSRmean"]

# Перетворемо всі значення у числа, тому що при обробці даних ми замітили що значення стовпця WET є у STRING
df['TEMPmean'] = pd.to_numeric(df['TEMPmean'], errors='coerce')
df['WET'] = pd.to_numeric(df['WET'], errors='coerce')
df['WINDspeed'] = pd.to_numeric(df['WINDspeed'], errors='coerce')
df['PRSRmean'] = pd.to_numeric(df['PRSRmean'], errors='coerce')

print(df)
df.info()

# Підрахунок кількості пропущених значень в усьому DataFrame
missing_values_count = df.isna().sum().sum()

# Виведення результату
print("\n\nКількість пропущених значень в усьому DataFrame:", missing_values_count)

# Аналіз унікальних значень у стовпці "TEMPmean"
tempmean_counts = df['TEMPmean'].value_counts()
print("Унікальні значення у стовпці 'TEMPmean':")
print(tempmean_counts)

# Аналіз унікальних значень у стовпці "WET"
wet_counts = df['WET'].value_counts()
print("\nУнікальні значення у стовпці 'WET':")
print(wet_counts)

# Аналіз унікальних значень у стовпці "WINDspeed"
windspeed_counts = df['WINDspeed'].value_counts()
print("\nУнікальні значення у стовпці 'WINDspeed':")
print(windspeed_counts)

# Аналіз унікальних значень у стовпці "PRSRmean"
prsrmean_counts = df['PRSRmean'].value_counts()
print("\nУнікальні значення в стовпці 'PRSRmean':")
print(prsrmean_counts)

# Виправлення відсутніх або недійсних даних 
# (ми подивилися на кількість пропущених даних і побачили що їх не ведика кіслькість)
df = df.dropna()  # Видалення рядків з пропущеними значеннями

# Перетворення типів даних
df["DATE"] = pd.to_datetime(df["DATE"])  # Перетворення стовпця "DATE" до типу дати

# Робимо стовпець "DATE" індексом
df = df.set_index("DATE")

# Видалення стовпця "Index"
df = df.drop("Index", axis=1)

# Виведення перших рядків DataFrame після видалення стовпця
print(df.head())

# Сортування за стовпцем "date"
df = df.sort_values(by="DATE")  

# Сортування та переупорядкування
df = df.sort_values(by="DATE")  # Сортування за стовпцем "DATE"

# Кількість дублікатів до чистки
print("Кількість дублікаті до чистки: ", df.duplicated().sum())

# Видалення дублікатів
df = df.drop_duplicates()

# Кількість дублікатів після чистки
print("Кількість дублікатів після чистки: ", df.duplicated().sum())

# Виведення DataFrame 
print("Filtered data: \n", df)
# Виведення інформації про DataFrame 
print(df.info())

