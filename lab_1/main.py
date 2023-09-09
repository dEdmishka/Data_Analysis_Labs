# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np
import pandas as pd

# Task 1
print('Task 1')
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1)
arr2 = np.array([1, 2, 3, 4], dtype='int')
print(arr2)
arr3 = np.arange(1, 16, 2)
print(arr3)
arr4 = np.zeros((2, 4), dtype=float)
print(arr4)
arr5 = np.linspace(0, 1, 5)
print(arr5)
arr6 = np.random.random((4, 3))
print(arr6)
arr7 = np.random.randint(0, 100, (4, 4))
print(arr7)
arr8 = np.empty(5)
print(arr8)

# Task 2
print('Task 2')
print(arr2[1])
print(arr2[-1])
print(arr2[0:2])
print(arr1[0])

# Task 3
print('Task 3')
# додавання (+, np.add)
print(np.add(arr3, 2))
# віднімання (-, np.subtract)
print(np.subtract(arr3, 3))
# множення (*, np.multiply)
print(np.multiply(arr3, 2))
# ділення (/, np.divide)
print(np.divide(arr3, 2))
# піднесення до ступеню (**, np.power)
print(np.power(arr3, 2))
# ділення за модулем (%, np.mod)
print(np.mod(arr3, 2))
# зміна знаку на протилежний (-, np.negative).
print(np.negative(arr3))

a = np.arange(0, 6)
print(a)
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.multiply.outer(a, a))

# Task 4
print('Task 4')
data = pd.read_csv('iris.csv')
petal_width = np.array(data['petal_width'])
print(petal_width)
# Сума значень np.sum, мінімальне та максимальне значення np.min, np.max,
# середнє значення np.mean, середньоквадратичне відхилення np.std, дисперсія
# np.var, медіана np.median, персентилі np.percentile.
print(np.min(petal_width))
print(np.max(petal_width))
print(np.mean(petal_width))
print(np.var(petal_width))
print(np.std(petal_width))
print(np.median(petal_width))
print(np.percentile(petal_width, 25))
print(np.percentile(petal_width, 75))
