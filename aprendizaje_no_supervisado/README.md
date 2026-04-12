# 🧠 Aprendizaje No Supervisado - TransMilenio

## 📌 Descripción

Este módulo implementa técnicas de **aprendizaje no supervisado** para analizar patrones en el sistema de transporte TransMilenio en Bogotá.

A diferencia del aprendizaje supervisado, en este enfoque **no se utiliza una variable objetivo**, sino que el modelo identifica automáticamente estructuras y relaciones en los datos.

---

## 🎯 Objetivo

Agrupar datos del sistema de transporte en diferentes categorías según sus características, con el fin de identificar patrones como:

* Rutas rápidas
* Rutas con tráfico medio
* Rutas largas o congestionadas

---

## 📊 Dataset

Se utiliza el archivo:

```bash id="htpbth"
dataset_transmilenio.csv
```

### Variables:

* `origen`: estación de inicio
* `destino`: estación final
* `distancia_km`: distancia del recorrido
* `trafico`: nivel de tráfico (bajo, medio, alto)
* `hora`: hora del día

⚠️ En este modelo no se usa la variable `tiempo_min`, ya que no hay aprendizaje supervisado.

---

## 🧠 Modelo utilizado

### 🔹 K-Means (Clustering)

El algoritmo K-Means permite agrupar los datos en diferentes **clusters** según la similitud entre sus características.

En este proyecto se definieron:

```bash id="3jv6ds"
n_clusters = 3
```

---

## ⚙️ Requisitos

Instalar las librerías necesarias:

```bash id="og61v8"
pip install pandas scikit-learn
```

---

## ▶️ Ejecución

Ejecutar el modelo con:

```bash id="dpt57a"
python modelo_kmeans.py
```

---

## 🧪 Proceso del modelo

1. Carga del dataset
2. Codificación de variables categóricas
3. Eliminación de variables no necesarias
4. Aplicación del algoritmo K-Means
5. Asignación de clusters

---

## 📈 Resultados

El modelo asigna un cluster a cada registro del dataset, permitiendo identificar grupos de comportamiento.

Ejemplo:

```bash id="nptn06"
   origen destino distancia_km trafico hora cluster
0       1       2             5       1    8       0
1       1       3             8       2   18       1
```

---

## 📌 Interpretación de clusters

* Cluster 0 → rutas rápidas
* Cluster 1 → tráfico medio
* Cluster 2 → rutas largas o congestionadas

---

## 📄 Conclusión

El aprendizaje no supervisado permite descubrir patrones ocultos en los datos sin necesidad de etiquetas.

El algoritmo K-Means es una herramienta útil para segmentar información y analizar comportamientos dentro del sistema de transporte.

---

## 👥 Integrantes

* William Latorre

