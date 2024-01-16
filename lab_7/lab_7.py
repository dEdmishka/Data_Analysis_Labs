# lab 7
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error, \
    median_absolute_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score

data = pd.read_csv('tips.csv')


# Task 1 - Використати будь-яку комбінацію незалежних ознак (не менше двох), щоб спрогнозувати розмір чайових.
print('\nTask 1\n')

# Кодування категоріальних змінних (sex, smoker, day, time) у числові
label_encoders = {}
categorical_columns = ['sex', 'smoker', 'day', 'time']

for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

print(data)

# Вибірка значень
X = data[['total_bill', 'sex', 'smoker', 'day', 'time']]
y = data['tip']

# Навчання моделі
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозування на тестових даних
predictions = model.predict(X_test)

# Оцінка точності моделі

print('\nКраще до 1')
print('R2, коефіцієнт детермінації, який кількісно визначає частку дисперсії залежної змінної: ',
      r2_score(y_test, predictions))
print('Оцінка поясненої дисперсії, яка говорить нам про відсоток дисперсії: ',
      explained_variance_score(y_test, predictions))

print('\nКраще до 0')
print('Середня абсолютна похибка (MAE): ', mean_absolute_error(y_test, predictions))

print('\nАбсолютні значення')
print('Середньоквадратична помилка (RMSE): ', np.sqrt(mean_squared_error(y_test, predictions)))
print('Середня абсолютна помилка, яка є медіаною залишків: ', median_absolute_error(y_test, predictions))

# Щоб оцінити модель лінійної регресії, потрібно візуалізувати залишки
# (розбіжності між фактичними значеннями та прогнозами моделі); вони повинні
# бути зосереджені навколо нуля і мати однакову дисперсію. Можна використати
# ядерну оцінку щільності, щоб оцінити, чи залишки зосереджені навколо нуля, і
# діаграму розсіювання, щоб побачити, чи мають вони однакову дисперсію.

# Побудова графіку для порівняння прогнозованих та реальних значень
plt.figure(figsize=(12, 10))
plt.scatter(y_test, predictions, color='blue', label='Predicted')
plt.plot(y_test, y_test, color='red', label='Actual')  # Лінія ідентичності для порівняння
plt.title('Порівняння прогнозованих та реальних значень')
plt.xlabel('Реальні значення')
plt.ylabel('Прогнозовані значення')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 10))
# Значення реальних даних
plt.plot(np.linspace(0, len(y_test), len(y_test)), y_test, color='blue', label='Actual')
# Значення 'прогнозованих' даних
plt.plot(np.linspace(0, len(predictions), len(predictions)), predictions, color='red',
         label='Predicted')
plt.title('Порівняння прогнозованих та реальних значень(як функцій)')
plt.xlabel('Кількість значень')
plt.ylabel('Розмір чайових')
plt.legend()
plt.show()

# Побудова графіків для аналізу залишків(різниць)
residuals = y_test - predictions

# Ядерна оцінка щільності залишків
# Вона показує розподіл залишків, а діаграма розсіювання дозволяє перевірити дисперсію залишків
# відносно прогнозованих значень. Червона лінія у діаграмі розсіювання показує нульове значення залишків.
plt.figure(figsize=(10, 10))
sns.kdeplot(residuals, fill=True)
plt.title('Ядерна оцінка щільності залишків')
plt.xlabel('Залишки')
plt.ylabel('Щільність')
plt.show()

# Діаграма розсіювання залишків
# Якщо залишки зосереджені навколо нуля та розкидані однаково навколо центральної лінії на діаграмі розсіювання
# це свідчить про адекватність моделі регресії. Якщо вони мають нетипові властивості, це може означати необхідність
# подальшого дослідження та покращення моделі.
plt.figure(figsize=(10, 10))
plt.scatter(predictions, residuals)
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Діаграма розсіювання залишків')
plt.xlabel('Прогнозовані значення')
plt.ylabel('Залишки')
plt.show()


# Task 2 - Виконати кластерний аналіз на даних, описати результати.
print('\nTask 2\n')

# Нормалізація числових ознак для кластеризації
kmeans_data = data[['total_bill', 'tip']]
scaled_features = StandardScaler().fit_transform(kmeans_data)

kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
kmeans.fit(scaled_features)

# Додавання міток кластерів до даних
data['cluster'] = kmeans.labels_
print(data)

# обчислюється шляхом віднімання середнього значення відстаней між кожними
# двома точками в кластері (a) із середнього відстаней між точками в даному
# кластері та найближчого іншого кластера (b) і діленням на максимальну з двох.
print('\nКраще до 1')
print('Коефіцієнт силуету: ', silhouette_score(scaled_features, kmeans.predict(scaled_features)))

# відношення відстаней всередині кластера (відстаней між точками в кластері)
# до відстаней між кластерами (відстаней між точками в різних кластерах
print('\nКраще до 0')
print('Оцінка Девіса-Болдіна: ', davies_bouldin_score(scaled_features, kmeans.predict(scaled_features)))

# критерій співвідношення дисперсії, який є відношенням
# дисперсії всередині кластера до дисперсії між кластерами.
print('\nКраще більші')
print('Оцінка Калінського та Харабаса: ', calinski_harabasz_score(scaled_features, kmeans.predict(scaled_features)))

# Побудова графіка для кластеризації
plt.figure(figsize=(7, 7))
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'navy', 'black', 'gray', 'olive', 'maroon']

for cluster, color in zip(range(len(kmeans.cluster_centers_)), colors):
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(cluster_data['total_bill'], cluster_data['tip'], c=color, label=f'Cluster {cluster}', edgecolor='k')

plt.title('Кластеризація "total_bill" та "tip"')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.legend()
plt.show()
