import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df = pd.read_csv('Estudiantes.csv')
print(df.head())
X = df[['Horas_Estudio', 'Asistencia']].values
y = df['Aprueba'].values

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

nuevo_punto1 = np.array([[1.0, 45.0]]) 
prediccion1 = knn.predict(nuevo_punto1)

nuevo_punto2 = np.array([[2.5, 60.0]]) 
prediccion2 = knn.predict(nuevo_punto2)

nuevo_punto3 = np.array([[6.0, 85.0]]) 
prediccion3 = knn.predict(nuevo_punto3)

nuevo_punto4 = np.array([[1.5, 90.0]])
prediccion4 = knn.predict(nuevo_punto4)

print(f"El alumno 1 es {'Aprobado' if prediccion1[0] == 1 else 'Reprobado' }")
print(f"El alumno 2 es {'Aprobado' if prediccion2[0] == 1 else 'Reprobado' }")
print(f"El alumno 3 es {'Aprobado' if prediccion3[0] == 1 else 'Reprobado' }")
print(f"El alumno 4 es {'Aprobado' if prediccion4[0] == 1 else 'Reprobado' }")
      
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', label='Datos')
plt.scatter(nuevo_punto1[:, 0], nuevo_punto1[:, 1], c='black', label="Alumno 1", marker='X', s=100)
plt.scatter(nuevo_punto2[:, 0], nuevo_punto2[:, 1], c='pink', label="Alumno 2", marker='X', s=100)
plt.scatter(nuevo_punto3[:, 0], nuevo_punto3[:, 1], c='orange', label="Alumno 3", marker='X', s=100)
plt.scatter(nuevo_punto4[:, 0], nuevo_punto4[:, 1], c='green', label="Alumno 4", marker='X', s=100)
plt.title("Clasificación KNN")
plt.xlabel("Horas_Estudio")
plt.ylabel("Asistencia")
plt.legend()
plt.show()
