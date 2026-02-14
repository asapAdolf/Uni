import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('Libro1.csv')

print(df.head())
X = df[['Peso', 'Altura']].values
y = df['Etiqueta'].values

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

nuevo_punto = np.array([[175, 13]]) 
prediccion = knn.predict(nuevo_punto)

print(f"La fruta es clasificada como: {'Manzana' if prediccion[0] == 0 else 'Pera'}")

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', label='Datos')
plt.scatter(nuevo_punto[:, 0], nuevo_punto[:, 1], c='black', label="Nuevo punto", marker='X', s=100)
plt.title("Clasificación KNN")
plt.xlabel("Peso (g)")
plt.ylabel("Altura (cm)")
plt.legend()
plt.show()