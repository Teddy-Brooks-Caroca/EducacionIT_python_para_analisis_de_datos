# =====================================================
#   PYTHON PARA ANÁLISIS DE DATOS
#   MÓDULO 03 – DESAFÍOS
# =====================================================

# =====================================================
#   EJERCICIO 1: MANIPULACIÓN DE ARRAYS
# =====================================================
# A. Construir arrays a partir de una lista simple y una lista anidada usando
#    tipos de datos numéricos distintos para cada una.

import numpy as np

lista_1 = [1,2,4.5,12]

lista_2 = [[2,3,4,5],[4.2,5.2,6.3,7.9]]

arr_1 = np.array(lista_1)

arr_2 = np.array(lista_2)

print(arr_1)
print(arr_2)

# B. Construir un array lineal de 36 elementos. Cambiar el shape para que tenga:
#    ● 3 filas y 12 columnas
#    ● 4 columnas

array_3 = np.arange(36)

array_3_reshape = array_3.reshape(3,12)

array_3_reshape_4 = array_3.reshape(-1, 4)


# =====================================================
#   EJERCICIO 2: CÁLCULO DE ÍNDICE DE MASA CORPORAL (IMC)
# =====================================================
# Dado un vector de pesos(kg) y otro vector alturas(metros), calcular el índice
# de masa corporal general (un vector imc).
#
# pesos = np.array([50, 65.5, 89.2, 100])
# alturas = np.array([1.6, 1.7, 1.8, 1.75])

pesos = np.array([50, 65.5, 89.2, 100])

alturas = np.array([1.6, 1.7, 1.8, 1.75])

imc_vector = pesos / (alturas ** 2)

print(f"Los IMC correspondientes son: {imc_vector}")

# =====================================================
#   EJERCICIO 3: OPERACIONES CON VECTORES Y MATRICES
# =====================================================
# 1. Crear un vector con diez números, todos ceros.

vector_10_ceros = np.zeros(10)

print(vector_10_ceros)

# 2. Crear un vector con diez números al azar.

vector_10_numeros = np.random.random(10,)

print(vector_10_numeros)

# 3. Crear una matriz de 2x3 y multiplicarla por su traspuesta.
#    Lo pedido sería algo así: A * Aᵀ.
#
#    (Matriz transpuesta es, en álgebra, una matriz que se forma al cambiar
#    filas por columnas de la matriz original).

matriz = np.array([[2,3],[3,4]])

transpuesta = matriz * np.transpose(matriz)

print(transpuesta)

# =====================================================
#    FIN DESAFÍOS MÓDULO 03 - PYTHON PARA ANÁLISIS DE DATOS
# =====================================================