#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 02:23:08 2023

@author: nazarodemchuk
"""


import pandas as pd

# Читаємо файл HTML і змінюємо назви стовпців
data = pd.read_html('Version 6.html')[0]  # Читаємо першу таблицю з HTML-файлу

# Змінюємо назви стовпців
data.columns = ["index", "date", "digit1", "digit2", "digit3", "digit4"]

# Перетворення стовпців 'digit' у числа
data['digit1'] = pd.to_numeric(data['digit1'], errors='coerce')
data['digit2'] = pd.to_numeric(data['digit2'], errors='coerce')
data['digit3'] = pd.to_numeric(data['digit3'], errors='coerce')
data['digit4'] = pd.to_numeric(data['digit4'], errors='coerce')

# Обробка повторюваних даних
data = data.drop_duplicates()

# Виправлення відсутніх або недійсних даних
data = data.dropna()  # Видалення рядків з пропущеними значеннями

# Робимо стовпець "index" індексом
data = data.set_index("index")

# Сортування та переупорядкування
data = data.sort_values(by="date")  # Сортування за стовпцем "date"

# Перетворення типів даних
data["date"] = pd.to_datetime(data["date"])  # Перетворення стовпця "date" до типу дати

# Видалення рядків з від'ємними значеннями
data = data.loc[(data['digit1'] >= 0) & (data['digit2'] >= 0) & (data['digit3'] >= 0) & (data['digit4'] >= 0)]

# Фільтрація до потрібної підмножини даних
# Наприклад, виберемо рядки, де 'digit1' більше за 10
filtered_data = data[data['digit1'] < 10]

# Виводимо оброблені дані на консоль
print(data)
print("Filtered data: ")
print(filtered_data)