import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# =========================
# 1. CARGAR DATOS
# =========================

df = pd.read_csv("aprendizaje_no_supervisado/dataset.csv")

# =========================
# 2. PREPROCESAMIENTO
# =========================

le = LabelEncoder()

df["origen"] = le.fit_transform(df["origen"])
df["destino"] = le.fit_transform(df["destino"])
df["trafico"] = le.fit_transform(df["trafico"])

# Eliminamos la variable objetivo
X = df.drop("tiempo_min", axis=1)

# =========================
# 3. MODELO K-MEANS
# =========================

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# =========================
# 4. RESULTADOS
# =========================

df["cluster"] = kmeans.labels_

print(df)
print("Centroides:", kmeans.cluster_centers_)