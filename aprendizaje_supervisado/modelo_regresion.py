import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# =========================
# 1. CREAR DATASET
# =========================

data = {
    "origen": ["Portal Norte", "Calle 100", "Calle 72", "Av. Jiménez", "Portal Norte"],
    "destino": ["Calle 100", "Calle 72", "Av. Jiménez", "Portal Sur", "Calle 72"],
    "distancia_km": [5, 4, 6, 10, 8],
    "trafico": ["medio", "alto", "medio", "alto", "bajo"],
    "hora": [8, 18, 12, 19, 6],
    "tiempo_min": [12, 15, 14, 25, 13]
}

df = pd.DataFrame(data)

# =========================
# 2. PREPROCESAMIENTO
# =========================

le = LabelEncoder()

df["origen"] = le.fit_transform(df["origen"])
df["destino"] = le.fit_transform(df["destino"])
df["trafico"] = le.fit_transform(df["trafico"])

X = df.drop("tiempo_min", axis=1)
y = df["tiempo_min"]

# =========================
# 3. ENTRENAMIENTO
# =========================

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# =========================
# 4. PREDICCIÓN
# =========================

predicciones = modelo.predict(X_test)

# =========================
# 5. EVALUACIÓN
# =========================

error = mean_absolute_error(y_test, predicciones)

print("Predicciones:", predicciones)
print("Valores reales:", list(y_test))
print("Error promedio:", error)