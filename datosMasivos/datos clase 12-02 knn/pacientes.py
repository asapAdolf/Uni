import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('pacientes.csv')
print(df.head())
X = df[['Presion', 'Glucosa']].values
y = df['Enfermo'].values

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

nuevo_punto1 = np.array([[150, 130]]) 
prediccion1 = knn.predict(nuevo_punto1)

nuevo_punto2 = np.array([[90, 125]]) 
prediccion2 = knn.predict(nuevo_punto2)

nuevo_punto3 = np.array([[112,90]]) 
prediccion3 = knn.predict(nuevo_punto3)

nuevo_punto4 = np.array([[150, 70]])
prediccion4 = knn.predict(nuevo_punto4)

print(f"El paciente 1 es {'Enfermo' if prediccion1[0] == 1 else 'Sano' }")
print(f"El paciente 2 es {'Enfermo' if prediccion2[0] == 1 else 'Sano' }")
print(f"El paciente 3 es {'Enfermo' if prediccion3[0] == 1 else 'Sano' }")
print(f"El paciente 4 es {'Enfermo' if prediccion4[0] == 1 else 'Sano' }")
      
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', label='Datos')
plt.scatter(nuevo_punto1[:, 0], nuevo_punto1[:, 1], c='black', label="paciente 1", marker='X', s=100)
plt.scatter(nuevo_punto2[:, 0], nuevo_punto2[:, 1], c='pink', label="paciente 2", marker='X', s=100)
plt.scatter(nuevo_punto3[:, 0], nuevo_punto3[:, 1], c='orange', label="paciente 3", marker='X', s=100)
plt.scatter(nuevo_punto4[:, 0], nuevo_punto4[:, 1], c='green', label="paciente 4", marker='X', s=100)
plt.title("Clasificación KNN")
plt.xlabel("Presion")
plt.ylabel("Glucosa")
plt.legend()
plt.show()