# =====================================================
#   PYTHON PARA ANÁLISIS DE DATOS
#   MÓDULO 04 – DESAFÍOS
# =====================================================

# =====================================================
#   EJERCICIO 1: CREACIÓN DE SERIES Y DATAFRAMES
# =====================================================
# 1. Crear series a partir de listas y a partir de arrays.

import numpy as np
import pandas as pd

mi_lista = [2,3,4,5]

serie_1 = pd.Series(mi_lista)

print(serie_1)

mi_array = np.array([2,3,4,5])

serie_2 = pd.Series(mi_array)

print(serie_2)

# 2. Crear dataframes a partir de listas anidadas, y de arrays anidados.

lista_anidada = ([1,2,3,4],[2.3,3.4,4.5,5.6])

df_1 = pd.DataFrame(lista_anidada)

print(df_1)

array_3 = np.array([2,3,4,5])

array_4 = np.array([5,6,7,8])

array_j = np.array([array_3, array_4])

df_2 = pd.DataFrame(array_j)

print(df_2)

# 3. Crear dataframes especificando etiquetas para las columnas.

array_3 = np.array([2,3,4,5])

array_4 = np.array([5,6,7,8])

array_j = np.array([array_3, array_4])

df_nombres = pd.DataFrame(array_j,columns=["Enero","Febrero","Marzo","Abril"])

print(df_nombres)

# 4. Cargar el dataframe del titanic (titanic.csv), y visualizar la información
#    del mismo.

tabla_titanic = pd.read_csv(r"C:\Users\brook\OneDrive\Escritorio\Portafolio\EducacionIT_ejercicios\EducacionIT_python_para_analisis_de_datos\Archivos\titanic.csv")

tabla_titanic.head()

# =====================================================
#   EJERCICIO 2: MANIPULACIÓN DEL DATAFRAME TITANIC
# =====================================================
# De titanic.csv, ya cargado como dataframe:
#
# 1. Seleccionar las columnas "Survived", "Pclass", "Age" y "Sex".

columnas_seleccionadas = tabla_titanic[["Survived", "Pclass", "Age","Sex"]]

print(columnas_seleccionadas)

# 2. Seleccionar las filas 200 a 400 de las columnas "Name" y "Age".

seleccion = tabla_titanic[["Name", "Age"]].iloc[200:400]

print(seleccion)

# 3. Cambiar el nombre de la columna "PassengerId" por "ID".

rename_columna = tabla_titanic.rename(columns={"PassengerId":"ID"})

print(rename_columna)

# 4. Seleccionar los datos de todas las mujeres de primera clase.

seleccion_mujeres = tabla_titanic[(tabla_titanic["Sex"]=="female") & (tabla_titanic["Pclass"]==1)]

print(seleccion_mujeres)

# 5. Seleccionar los datos de los varones menores de edad de segunda clase.

seleccion_varones = tabla_titanic[(tabla_titanic["Sex"]=="male")&(tabla_titanic["Age"]<18)]

print(seleccion_varones)

# =====================================================
#   EJERCICIO 3: ANÁLISIS ESTADÍSTICO DEL TITANIC
# =====================================================
# Del titanic.csv, ya cargado como dataframe:
#
# 1. Encontrar el promedio de edad de hombres y de las mujeres.

promedio_varones = tabla_titanic[tabla_titanic["Sex"]=="male"]["Age"].mean()

promedio_damas = tabla_titanic[tabla_titanic["Sex"]=="female"]["Age"].mean()

print(promedio_varones)

print(promedio_damas)

# 2. Encontrar la cantidad de sobrevivientes de hombres y las mujeres.

conteo_hombres = len(tabla_titanic[(tabla_titanic["Sex"]=="male") & (tabla_titanic["Survived"]==1)])

conteo_mujeres = len(tabla_titanic[(tabla_titanic["Sex"]=="female") & (tabla_titanic["Survived"]==1)])
        

print(conteo_hombres)

print(conteo_mujeres)

# Aclaración: Este dataframe (titanic.csv) no contiene realmente toda la
# información de los que viajaban en el barco, sino que es una porción de los
# pasajeros. Pero para cuestiones prácticas y académicas es uno de los más
# utilizados y empleados para aprender a usar estas herramientas.

# =====================================================
#    FIN DESAFÍOS MÓDULO 04 - PYTHON PARA ANÁLISIS DE DATOS
# =====================================================