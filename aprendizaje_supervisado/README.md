# 🤖 Aprendizaje Supervisado - TransMilenio

## 📌 Descripción

Este módulo del proyecto implementa técnicas de **aprendizaje supervisado** para predecir el tiempo de viaje entre estaciones del sistema TransMilenio en Bogotá.

Se utilizan modelos de Machine Learning como:

* Regresión Lineal
* Random Forest

---

## 🎯 Objetivo

Predecir el tiempo estimado de un recorrido teniendo en cuenta variables como:

* Estación de origen
* Estación de destino
* Distancia (km)
* Nivel de tráfico
* Hora del día

---

## 📊 Dataset

Se utilizó un dataset sintético llamado:

```bash
dataset_transmilenio.csv
```

### Variables:

* `origen`: estación de inicio
* `destino`: estación final
* `distancia_km`: distancia entre estaciones
* `trafico`: nivel de tráfico (bajo, medio, alto)
* `hora`: hora del día
* `tiempo_min`: tiempo estimado (variable objetivo)

---

## ⚙️ Requisitos

Instalar las librerías necesarias:

```bash
pip install pandas scikit-learn
```

---

## ▶️ Ejecución

Ejecutar el modelo:

```bash
python modelo_random_forest.py
```

o

```bash
python modelo_regresion.py
```

---

## 🧠 Modelos implementados

### 🔹 Regresión Lineal

Modelo básico que establece una relación entre variables.

### 🌲 Random Forest

Modelo avanzado basado en múltiples árboles de decisión, que mejora la precisión.

---

## 📈 Resultados

El modelo genera:

* Predicciones del tiempo de viaje
* Comparación con valores reales
* Error promedio (MAE)

---

## 🧪 Ejemplo de salida

```bash
Predicciones: [14.5, 22.1]
Valores reales: [15, 20]
Error promedio: 1.3
```

---

## 📌 Conclusión

El aprendizaje supervisado permite modelar y predecir comportamientos del sistema de transporte, siendo útil para optimizar tiempos de viaje.

---

## 👥 Integrantes

* William Latorre
