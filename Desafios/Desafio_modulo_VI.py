# =====================================================
#   PYTHON PARA ANÁLISIS DE DATOS
#   MÓDULO 06 – DESAFÍOS
# =====================================================

# =====================================================
#   EJERCICIO 1: CURVAS CON LINSPACE
# =====================================================
# Construir 3 gráficos de línea a partir de un array creado con la función
# linspace de numpy.

# a. Uno que represente una curva lineal.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-5,5,20)
y = 2*x + 1

plt.plot(x,y)

plt.show()

# b. Otro que represente una curva cuadrática.

x = np.linspace(-5,5,20)
w = x**2 + x + 2

plt.plot(x,w)

plt.show()

# c. Un tercero que represente una curva logarítmica.

x = np.linspace(-5,5,20)

xpositivo = x[x>0]
len(xpositivo)

u = np.log(xpositivo)

plt.plot(xpositivo,u)

plt.show()

# =====================================================
#   EJERCICIO 2: FORMATO Y SUBPLOTS
# =====================================================
# Para los gráficos realizados en el ejercicio anterior, hay que cambiar el formato.
# Además, los 3 gráficos deben de quedar en una sola figura juntos, hay que activar
# la grilla y ponerle el título a la figura "Gráfico de pruebas" y cambiar el tamaño
# del mismo para poder apreciarlo mejor, según corresponda.
#
# Agregar leyendas.
#
# a. El que representa la curva lineal, debe ser de color rojo y punteada (···),
#    con marcador del tipo "square marker".
#
# b. La curva cuadrática, sólida de color negro y con un marcador del tipo
#    "circle marker".
#
# c. La curva logarítmica debe ser discontinua (- - -) de color amarillo y con
#    marcador del tipo "x marker".

x = np.linspace(-5,5,20)
y = 2*x + 1
w = x**2 + x + 2
xpositivo = x[x>0]
u = np.log(xpositivo)

plt.figure(figsize=(10,10))
plt.plot(x,y,"r:s",label="Lineal")
plt.plot(x,w,"k-o",label="Cuadrática")
plt.plot(xpositivo,u,"y--x",label="Logarítmica")
plt.grid()
plt.title("Grafico de pruebas")
plt.legend()

plt.show()

# =====================================================
#   EJERCICIO 3: SUBPLOT CON BARRAS Y TORTA
# =====================================================
# Se tiene una lista de listas de la evolución del dólar por año y un diccionario
# con la demanda según porcentaje de los que compran dólares o hacen uso de la
# divisa en Argentina:
#
# dolarValor = [[2020,70], [2021,95], [2022,110]]  (Año – Valor dólar oficial)
#
# dolarComp = {"privados": 40, "particulares": 20, "estatales": 30, "otros": 10}
#
# Hacer un subplot con un gráfico de barras de dolarValor y una torta de dolarComp
# con sus respectivos títulos.

dolarValor = [[2020,70],[2021,95],[2022,110]]

anio = [n[0] for n in dolarValor]

valor = [n[1] for n in dolarValor]

dolarComp = {"privados":40,"particulares":20,"estatales":30,"otros":10}

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(anio,valor)
plt.title("Valor del Dolar")
plt.subplot(1,2,2)
plt.pie(list(dolarComp.values()),labels=list(dolarComp.keys()))
plt.title("Compradores")

plt.show()

# =====================================================
#    FIN DESAFÍOS MÓDULO 06 - PYTHON PARA ANÁLISIS DE DATOS
# =====================================================