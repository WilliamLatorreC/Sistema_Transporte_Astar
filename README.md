# 🚍 Sistema Inteligente de Rutas - TransMilenio (Bogotá)

## 📌 Descripción

Este proyecto implementa un sistema inteligente basado en **Inteligencia Artificial**, específicamente en técnicas de **búsqueda heurística (Algoritmo A*)** y **sistemas basados en reglas**, con el objetivo de encontrar la mejor ruta entre dos estaciones del sistema de transporte masivo TransMilenio en Bogotá.

El sistema modela las estaciones como nodos y las conexiones como un grafo con costos asociados (tiempo estimado de viaje).

---

## 🧠 Tecnologías utilizadas

* Python 3
* Algoritmo A* (A estrella)
* Programación Orientada a Objetos (POO)

---

## ⚙️ Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

* Python 3.x

Verifica con:

```bash
python --version
```

---

## ▶️ Instrucciones de ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/ia-transmilenio.git
```

2. Ingresar a la carpeta del proyecto:

```bash
cd ia-transmilenio
```

3. Ejecutar el programa:

```bash
python codigo.py
```

---

## 🗺️ Funcionamiento del sistema

El sistema representa una red simplificada de TransMilenio con estaciones como:

* Portal Norte
* Calle 100
* Calle 72
* Av. Jiménez
* Portal Sur

El algoritmo A* evalúa:

* El costo real del recorrido (tiempo)
* Una heurística (estimación al destino)

Y selecciona la ruta más eficiente.

---

## 🧪 Ejemplo de ejecución

Entrada:

```
Origen: Portal Norte  
Destino: Portal Sur  
```

Salida esperada:

```
Mejor ruta encontrada:
→ Portal Norte
→ Calle 100
→ Calle 72
→ Av. Jiménez
→ Portal Sur
```

---

## 📚 Conceptos aplicados

* Sistemas basados en reglas
* Representación del conocimiento
* Búsqueda heurística
* Algoritmo A*

---

## 🎥 Video del proyecto

Link al video explicativo (máx. 5 minutos):

👉 [PEGAR LINK DEL VIDEO AQUÍ]

---

## 📄 Documento de pruebas

El documento PDF con las pruebas realizadas se encuentra en el repositorio.

---

## 👥 Integrantes del equipo

* Nombre 1
* Nombre 2
* Nombre 3

---

## 📌 Notas adicionales

Este proyecto es una simulación académica del sistema TransMilenio y no representa rutas reales exactas.

---

## 🚀 Autor

Proyecto desarrollado para la asignatura **Inteligencia Artificial**.
