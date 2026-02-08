import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

archivo = "resultados_medicos_Mexico.xlsx"
df = pd.read_excel(archivo)
df = df.dropna(subset=["presionMedia", "IMC", "Glucosa_mg_dl"])

x = df[["presionMedia", "IMC"]]
y = df["Glucosa_mg_dl"]

model = LinearRegression()
model.fit(x, y)

print("Intercep: ", model.intercept_)
print("Coeficiente: ", model.coef_[0])
print("Coeficiente 1:", model.coef_[1])