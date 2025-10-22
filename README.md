# prediccion-de-costos-medicos---Regresion-Lineal
Este proyecto aplica un modelo de **Regresión Lineal** para predecir el **costo médico de los asegurados** en función de variables como edad, sexo, índice de masa corporal (BMI), número de hijos, hábito de fumar y región geográfica.

El flujo del script incluye:
1. Carga y exploración de datos.
2. Limpieza y codificación de variables categóricas.
3. Escalado de características con `StandardScaler`.
4. División del dataset en entrenamiento y prueba.
5. Entrenamiento del modelo de **Regresión Lineal**.
6. Evaluación del modelo mediante:
   - **RMSE (Root Mean Squared Error)**
   - **R² (Coeficiente de Determinación)**

Finalmente, se genera un gráfico que muestra la relación entre **edad** y **coste médico**.

---

## ⚙️ Requisitos

Instala las librerías necesarias:

## Ejecución

Coloca el archivo insurance.csv dentro de la carpeta data/.

Ejecuta el script principal:

python sanidad.py

El programa imprimirá en consola:

Información general del dataset.

Valores faltantes.

Métricas del modelo (RMSE y R²).

Gráfico de dispersión “Edad vs Coste médico”.

## Resultados esperados 
Un R² alrededor de 0.75 - 0.85, dependiendo de los datos y ajustes.
Esto indica que el modelo explica aproximadamente el 75–85% de la variabilidad en los costos médicos.

## Autora

Verónica Balza

