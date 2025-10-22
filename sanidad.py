import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score




datos= 'insurance.csv'
df = pd.read_csv(datos)

print(df.info())
print(df.describe())
print(df.isnull().sum())

csv = df.to_csv('sanidad.csv', index=False)

#pasar columnas de string a int
df['smoker'] = df['smoker'].map({'yes':1, 'no':0})
df['sex'] = df['sex'].map({'female':1,'male':0}) 
df = pd.get_dummies(df, columns=['region'], drop_first=True)

#separamos variables x y e y
x = df.drop('charges', axis=1)
y=df['charges']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


#entranamos nuestro modelo 
model = LinearRegression()
model = model.fit(X_train_scaled, y_train)

#hacemos las predicciones
y_pred = model.predict(x_test_scaled)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f'RMSE: {rmse}')
print(f'R2: {r2}')

import matplotlib.pyplot as plt
plt.scatter(df['age'], df['charges'])
plt.xlabel('Edad')
plt.ylabel('Coste médico')
plt.title('Relación entre edad y coste')
plt.show()

