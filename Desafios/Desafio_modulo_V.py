# =====================================================
#   PYTHON PARA ANÁLISIS DE DATOS
#   MÓDULO 05 – DESAFÍOS
# =====================================================

# =====================================================
#   EJERCICIO 1: ANÁLISIS ESTADÍSTICO DEL TITANIC
# =====================================================
# Importar nuevamente titanic.csv como dataframe, pero ahora hay que calcular:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tabla_titanic = pd.read_csv("titanic.csv")

# 1. El promedio de edad de los que sobrevivieron y los que no.

edad_sobreviviente = tabla_titanic.groupby("Survived")["Age"].mean()

print(edad_sobreviviente)

# 2. Edad máxima, edad mínima, de los que sobrevivieron y los que no.

edad_maxima = tabla_titanic.groupby("Survived")["Age"].max()

edad_minima = tabla_titanic.groupby("Survived")["Age"].min()

print(f"Edad máxima de ambos grupos: {edad_maxima}")

print(f"Edad mínima de ambos grupos: {edad_minima}")

# 3. Edad promedio por clase de los que sobrevivieron y los que no.

promedio_por_clase = tabla_titanic.groupby(["Survived","Pclass"])["Age"].mean()

print("Edad promedio por clase")
print(promedio_por_clase)

# (Hacer uso del groupby).

# =====================================================
#   EJERCICIO 2: VISUALIZACIÓN DE DATOS DEL TITANIC
# =====================================================
# 1. Del dataframe del titanic, calcular el promedio de edad de los que
#    sobrevivieron y los que no, hacer un gráfico de barras que sea representativo.

grafico_sobreviviente = tabla_titanic.groupby("Survived")["Age"].mean().plot.bar()

plt.show()

# 2. Hacer un gráfico del tipo histograma que represente la frecuencia de edades
#    únicamente de las mujeres que sobrevivieron.

mujeres_sobrevivientes = tabla_titanic[(tabla_titanic["Sex"]=="female")&(tabla_titanic["Survived"]==1)]["Age"].plot.hist()

plt.show()

# =====================================================
#   EJERCICIO 3: ANÁLISIS DE PRECIOS DEL ORO
# =====================================================
# Importar el archivo GoldPrice.csv (el mismo de la clase, del último apunte
# Pandas) como dataframe y realizar los siguientes cálculos:
#
# 1. Crear una nueva columna que solo contenga el año y llamarla "Year".

tabla_gold = pd.read_csv("goldprice.csv")

tabla_gold.info()

tabla_gold["Date"] = pd.to_datetime(tabla_gold["Date"])

tabla_gold["Year"] = tabla_gold["Date"].dt.year

print(tabla_gold)

# 2. Graficar el promedio del valor del oro por año con un gráfico de barras.

tabla_gold["Date"] = pd.to_datetime(tabla_gold["Date"])

tabla_gold["Year"] = tabla_gold["Date"].dt.year

valor_oro_por_annio = tabla_gold.groupby("Year")["Price"].mean()

print(valor_oro_por_annio)

grap_oro_por_annio = valor_oro_por_annio.plot.bar()

plt.show()

# 3. Determinar el promedio de precios del oro por año.

promedio_annio = tabla_gold.groupby("Year")["Price"].mean()

print(promedio_annio)

# 4. Calcular el año con mayor promedio y el año con menor promedio.

mayor_promedio =promedio_annio.idxmax()

menor_promedio = promedio_annio.idxmin()

print(f"El año con mejor promedio fue: {mayor_promedio}")

print(f"El año con menor promedio fue: {menor_promedio}")

# =====================================================
#    FIN DESAFÍOS MÓDULO 05 - PYTHON PARA ANÁLISIS DE DATOS
# =====================================================