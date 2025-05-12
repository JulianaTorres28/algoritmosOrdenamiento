# Práctica de Comparación de Algoritmos de Ordenamiento

## 📌 Información General

- **Título:** Comparación de Algoritmos de Ordenamiento en Python
- **Asignatura:** Estructura de Datos
- **Carrera:** Computación
- **Inetgrantes:** Andrea Hurtado y Juliana Torres
- **Fecha:** 11/5/2025
- **Profesor:** Ing. Pablo Torres

---

## 🛠️ Descripción

Este proyecto en Python tiene como objetivo comparar el rendimiento de cuatro algoritmos de ordenamiento clásicos:

- Bubble Sort
- Bubble Sort Mejorado
- Selección
- Shell Sort

Se realizan pruebas con listas de distintos tamaños, se mide el tiempo que tarda cada algoritmo en ordenar y se genera una gráfica comparativa utilizando `matplotlib`.

---

## 📂 Estructura del Proyecto

```

algoritmosOrdenamiento/
│
└── src\_python/
├── app.py
├── benchmarking.py
├── grafica.py
└── metodos\_ordenamiento.py

````

---


## 📈 Resultado Esperado

La ejecución mostrará una gráfica como esta (imagen de ejemplo):

![image](https://github.com/user-attachments/assets/766e2d18-9472-4316-be6c-772a2a697158)

## 📌 Conclusiones

* Bubble Sort, Bubble Sort Mejorado y Selección tienen una complejidad de $O(n^2)$, lo que los hace lentos con listas grandes.
* Shell Sort tiene una mejor eficiencia, con una complejidad promedio de $O(n \log n)$, por lo que es más rápido a medida que crece el tamaño de los datos.
* La gráfica permite visualizar claramente cómo se comporta cada algoritmo frente a diferentes volúmenes de datos.

```
```
