# lab 3
import pandas as pd

data = pd.read_csv('penguins.csv')

# Task 1
print('\nTask #1\n')
# 1. Вивести інформацію про набір даних, основні статистичні характеристики, типи ознак.
# Які ознаки є категоріальними, а які – кількісними?
print('Task #1, статистичні хар-тики')
print(data.describe())
print('Серед основних типів ознак можна виділити: ')
print(data.columns.values, '\n')
print('Серед наведених в DataFrame даних, кількісними є:\n'
      'culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g\n'
      'А категоріальними є:\n'
      'species, island, sex')

# Task 2
print('\nTask #2\n')
# 2. За допомогою зрізів зробити копію частини набору даних і зберегти до нового об’єкту DataFrame.
# Призначити йому власні індекси рядків та стовпців. Додати новий рядок.

# За допомогою зрізу робимо копію набору даних
newData = data.loc[100:200]

# Додаємо новий колонку
newData['index'] = newData['flipper_length_mm'] / (newData['culmen_length_mm'])

# Нову колонку робимо індексом рядків
newData.set_index(['index'], inplace=True)

# Міняємо індекси колонок
newData.rename({'species': 'new_species', 'island': 'new_island', 'culmen_length_mm': 'new_culmen_length_mm',
                'culmen_depth_mm': 'new_culmen_depth_mm', 'flipper_length_mm': 'new_flipper_length_mm',
                'body_mass_g': 'new_body_mass_g', 'sex': 'new_sex'}, axis=1, inplace=True)

# Додаємо новий рядок
print('Task #2, результат перетворень')
new_row = pd.DataFrame([{'new_species': 'Adelie', 'new_island': 'Coco', 'new_culmen_length_mm': 1,
                         'new_culmen_depth_mm': 1, 'new_flipper_length_mm': 1, 'new_body_mass_g': 1,
                         'new_sex': 'MALE'}])
newData = pd.concat([newData, new_row])
print(newData)

# Task 3
print('\nTask #3\n')
# 3. Використовуючи початковий DataFrame:
# а) Знайти кількість самців і самок на кожному з островів;
print('Task #3, а)\n')
print(data[data['sex'] == 'MALE'].groupby(['island', 'sex'])['sex'].count())
print(data[data['sex'] == 'FEMALE'].groupby(['island', 'sex'])['sex'].count())

# б) Вивести самців Аделі, що мають масу понад 3 кг.
print('\nTask #3, б)\n')
print(data[
          (data['body_mass_g'] > 3000) &
          (data['species'] == 'Adelie') &
          (data['sex'] == 'MALE')
          ]
      [['sex', 'species', 'body_mass_g']]
      )

# в) Додати новий стовпець, який показує, чи перевищує глибина дзьобу половину довжини дзьобу для даного
# пінгвіна.
print('\nTask #3, в)\n')
data['deep_greater_half_of_length'] = (data['culmen_depth_mm']) > ((data['culmen_length_mm']) / 2)
print(data[['deep_greater_half_of_length', 'culmen_depth_mm', 'culmen_length_mm']])

# г) Додати новий стовпець, який містить середню вагу пінгвінів даного виду.
print('\nTask #3, г)\n')
average_mass = data.groupby(['species'])['body_mass_g'].mean()
data = data.set_index(['species'])
data['average_mass'] = average_mass
data = data.reset_index()
print(data)
