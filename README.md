# 🚍 Sistema Inteligente de Transporte - TransMilenio (IA)

## 📌 Descripción del proyecto

Este proyecto implementa diferentes técnicas de **Inteligencia Artificial** aplicadas al sistema de transporte TransMilenio en Bogotá.

Se desarrollan tres enfoques principales:

* 🔎 Búsqueda heurística (Algoritmo A*)
* 🤖 Aprendizaje supervisado (Regresión y Random Forest)
* 🧠 Aprendizaje no supervisado (K-Means)

El objetivo es modelar, analizar y optimizar rutas y tiempos de viaje dentro del sistema de transporte.

---

## 🧠 Tecnologías utilizadas

* Python 3
* Pandas
* Scikit-learn
* Algoritmos de búsqueda (A*)
* Machine Learning

---

## 📂 Estructura del proyecto

```
Sistema_Transporte_Astar/
│
├── busqueda_astar/
│   └── codigo_astar.py
│
├── aprendizaje_supervisado/
│   ├── modelo_regresion.py
│   ├── modelo_random_forest.py
│   └── dataset_transmilenio.csv
│
├── aprendizaje_no_supervisado/
│   ├── modelo_kmeans.py
│   └── dataset_transmilenio.csv
│
├── documentos/
│   ├── pruebas_astar.pdf
│   ├── pruebas_supervisado.pdf
│   └── pruebas_no_supervisado.pdf
│
└── README.md
```

---

## 🔎 Módulo 1: Búsqueda con A*

Se implementa el algoritmo A* para encontrar la mejor ruta entre estaciones.

📌 Características:

* Representación del sistema como grafo
* Uso de heurística
* Optimización de rutas

▶️ Ejecución:

```bash
python busqueda_astar/codigo_astar.py
```

---

## 🤖 Módulo 2: Aprendizaje Supervisado

Se desarrollan modelos para predecir el tiempo de viaje.

### Modelos utilizados:

* Regresión Lineal
* Random Forest

📊 Variables:

* Origen
* Destino
* Distancia
* Tráfico
* Hora

▶️ Ejecución:

```bash
python aprendizaje_supervisado/modelo_random_forest.py
```

---

## 🧠 Módulo 3: Aprendizaje No Supervisado

Se implementa K-Means para identificar patrones en los datos.

📌 Objetivo:
Agrupar rutas según características similares.

▶️ Ejecución:

```bash
python aprendizaje_no_supervisado/modelo_kmeans.py
```

---

## ⚙️ Instalación

Instalar dependencias:

```bash
pip install pandas scikit-learn
```

---

## 📊 Resultados

* Optimización de rutas mediante A*
* Predicción de tiempos con Machine Learning
* Agrupación de patrones con clustering

---

## 📄 Documentación

El proyecto incluye:

* PDF con pruebas A*
* PDF aprendizaje supervisado
* PDF aprendizaje no supervisado

---

## 👥 Integrantes

* William Latorre


---

## 📌 Conclusión

Este proyecto demuestra cómo diferentes técnicas de Inteligencia Artificial pueden integrarse para resolver problemas reales en sistemas de transporte, desde la búsqueda de rutas hasta la predicción y análisis de datos.

---

## 🚀 Autor

Proyecto desarrollado para la asignatura **Inteligencia Artificial**.
