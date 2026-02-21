import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# 1. Cargar el dataset con el nombre correcto
df = pd.read_csv('dataset_clientes.xlsx')

# 2. Definir las características (X) y la etiqueta (y)
X = df[['Numero_Hijos', 'Ingreso_Mensual']].values
y = df['Tipo_Vivienda'].values

# Crear un arreglo numérico para los colores del gráfico (Propia=1, Rentada=0)
y_color = np.where(y == 'Propia', 1, 0)

# 3. Configurar y entrenar el modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# 4. Definir los nuevos puntos a predecir
nuevo_punto1 = np.array([[3, 32000]]) 
prediccion1 = knn.predict(nuevo_punto1)

nuevo_punto2 = np.array([[0, 123220]]) 
prediccion2 = knn.predict(nuevo_punto2)

nuevo_punto3 = np.array([[1, 85000]]) 
prediccion3 = knn.predict(nuevo_punto3)

nuevo_punto4 = np.array([[2, 21345]])
prediccion4 = knn.predict(nuevo_punto4)

# 5. Imprimir los resultados (el modelo ya devuelve 'Propia' o 'Rentada')
print(f"El caso 1 es {prediccion1[0]}")
print(f"El caso 2 es {prediccion2[0]}")
print(f"El caso 3 es {prediccion3[0]}")
print(f"El caso 4 es {prediccion4[0]}")
      
# 6. Generar la gráfica
# Usamos y_color para el parámetro c (color) y le damos un poco de transparencia (alpha) a los puntos base
plt.scatter(X[:, 0], X[:, 1], c=y_color, cmap='coolwarm', label='Datos base', alpha=0.5)

plt.scatter(nuevo_punto1[:, 0], nuevo_punto1[:, 1], c='black', label="Caso 1", marker='X', s=100)
plt.scatter(nuevo_punto2[:, 0], nuevo_punto2[:, 1], c='pink', label="Caso 2", marker='X', s=100)
plt.scatter(nuevo_punto3[:, 0], nuevo_punto3[:, 1], c='orange', label="Caso 3", marker='X', s=100)
plt.scatter(nuevo_punto4[:, 0], nuevo_punto4[:, 1], c='green', label="Caso 4", marker='X', s=100)

plt.title("Clasificación KNN: Tipo de Vivienda")
plt.xlabel("Número de Hijos")
plt.ylabel("Ingreso Mensual ($)")
plt.legend()
plt.show()
#num hijos, edad, ingreso mensual