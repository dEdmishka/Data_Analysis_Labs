import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report

# Зчитуємо дані з файлу blood.csv
df = pd.read_csv('blood.csv')

# Розділяємо дані на ознаки (X) та цільову змінну (y)
X = df.drop(columns=['Class'])
y = df['Class']

# Розділяємо дані на тренувальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

# Логістична регресія
logistic_regression_model = LogisticRegression(class_weight='balanced', random_state=0)
logistic_regression_model.fit(X_train, y_train)

# Дерево рішень
decision_tree_model = DecisionTreeClassifier(random_state=0)
decision_tree_model.fit(X_train, y_train)

# Оцінка моделі логістичної регресії
y_pred_lr = logistic_regression_model.predict(X_test)
conf_matrix_lr = confusion_matrix(y_test, y_pred_lr)
classification_report_lr = classification_report(y_test, y_pred_lr)

print("Logistic Regression Model:")
print("Confusion Matrix:\n", conf_matrix_lr)
print("Classification Report:\n", classification_report_lr)

# Оцінка моделі дерева рішень
y_pred_dt = decision_tree_model.predict(X_test)
conf_matrix_dt = confusion_matrix(y_test, y_pred_dt)
classification_report_dt = classification_report(y_test, y_pred_dt)

print("\nDecision Tree Model:")
print("Confusion Matrix:\n", conf_matrix_dt)
print("Classification Report:\n", classification_report_dt)


from sklearn.model_selection import GridSearchCV

# Створюємо конвеєр для логістичної регресії
pipeline_lr = Pipeline([('scale', StandardScaler()), ('lr', LogisticRegression(random_state=0))])

# Визначаємо простір параметрів для логістичної регресії
param_grid_lr = {'lr__C': [0.001, 0.01, 0.1, 1, 10, 100]}

# Використовуємо GridSearchCV для пошуку оптимальних параметрів
grid_search_lr = GridSearchCV(pipeline_lr, param_grid_lr, cv=5, scoring='accuracy')
grid_search_lr.fit(X_train, y_train)

# Виводимо кращі параметри
print("Best Parameters for Logistic Regression:", grid_search_lr.best_params_)

# Оцінка оптимізованої моделі логістичної регресії
y_pred_optimized_lr = grid_search_lr.predict(X_test)
conf_matrix_optimized_lr = confusion_matrix(y_test, y_pred_optimized_lr)
classification_report_optimized_lr = classification_report(y_test, y_pred_optimized_lr)

print("\nOptimized Logistic Regression Model:")
print("Confusion Matrix:\n", conf_matrix_optimized_lr)
print("Classification Report:\n", classification_report_optimized_lr)
