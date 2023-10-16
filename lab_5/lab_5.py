# lab 5
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Amazon.csv')

# Task 1
# 1.Побудувати графік зміни ціни на час закриття біржі:
print('\nTask #1\n')
#   a) загальний;
df_a = data[['Date', 'Close']].copy()
df_a['Date'] = pd.to_datetime(df_a['Date'])
df_a.set_index('Date', inplace=True)
df_a.plot(title='Завдання a) - Загальна зміна ціни на час закриття біржі')
plt.show()

#   b) за 2018 рік;
df_b = df_a.loc['2018']
df_b.plot(title='Завдання b) - Зміна ціни на час закриття біржі за 2018')
plt.show()

#   c) за січень 2020 року;
df_c = df_a.loc['2020-01']
df_c.plot(title='Завдання c) - Зміна ціни на час закриття біржі за січень 2020')
plt.show()

#   d) за грудень 2016 – лютий 2018;
df_d = df_a.loc['2016-12-01':'2018-02-28']
df_d.plot(title='Завдання d) - Зміна ціни на час закриття біржі за грудень 2016 - лютий 2018')
plt.show()

#   e) за 2016 та 2017 на одному графіку (паралельно).
df_e = data[['Date', 'Close']].copy()
df_e.set_index('Date', inplace=True)
df_e_1 = df_e.loc['2016-01-01':'2016-12-31']
df_e_2 = df_e.loc['2017-01-01':'2017-12-31']
fig, ax = plt.subplots()
df_e_1.rename(columns={'Close': 'Close 2016'}).plot(ax=ax,
                                                    title='Завдання e) - Зміна ціни на час закриття біржі за 2016 і '
                                                          '2017')
df_e_2.rename(columns={'Close': 'Close 2017'}).plot(ax=ax)
plt.show(figsize=(10, 5))

# Task 2
# 2.Знайти максимальні значення найбільшої ціни за день:
print('\nTask #2\n')
#   a) за 2016 рік;
second_df_a = data[['Date', 'High']].copy()
second_df_a['Date'] = pd.to_datetime(second_df_a['Date'])
second_df_a.set_index('Date', inplace=True)
print(second_df_a.loc['2016'].max())

#   b) за кожний рік;
print(second_df_a['High'].resample('Y').max())

#   c) за кожний тиждень весни 2019 року.
second_df_c = second_df_a.loc['2019-03':'2019-05']
print(second_df_c['High'].resample('W').max())

#   d) Розрахувати і зобразити зміни значення найбільшої ціни за день у
#      відсотках за кожен день впродовж весни 2018 року.
second_df_d = second_df_a.loc['2018-03':'2018-05']
second_df_d = second_df_d['High'].pct_change() * 100
# for index, value in enumerate(second_df_d):
#     print(index, value)
second_df_d.plot(title='Завдання d) - Зміна значення ціни впродовж весни 2018 у відсотках')
plt.show()

#   e) Знайти та зобразити графічно ковзне середнє найбільшої ціни за
#      день за 2017 рік з вікном в два місяці.
second_df_e = second_df_a.loc['2017']
second_df_e = second_df_e['High'].rolling(window=60).mean()
second_df_e.plot(title='Завдання e) - Ковзне середнє ціни за день, 2017, вікно в два місяці')
plt.show()
