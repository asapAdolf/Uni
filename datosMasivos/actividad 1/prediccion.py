import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

archivo = "datos.xlsx"
df = pd.read_excel(archivo)
print("Nombres de columnas detectados:", df.columns.tolist())

x = df[["Metros", "Habitaciones"]]
y = df["Precio"]
model = LinearRegression()

model.fit(x, y)


print("Intercep: ", model.intercept_)
print("Coeficiente: ", model.coef_[0])
print("Coeficiente habitaciones:", model.coef_[1])