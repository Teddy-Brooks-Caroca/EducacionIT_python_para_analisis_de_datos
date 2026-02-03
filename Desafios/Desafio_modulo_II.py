# =====================================================
#   PYTHON PARA ANÁLISIS DE DATOS
#   MÓDULO 02 – DESAFÍOS
# =====================================================

# =====================================================
#   EJERCICIO 1: FRECUENCIA DE ELEMENTOS
# =====================================================
# Construir una función que dado un iterable, devuelva un diccionario con las
# frecuencias de sus elementos.

def frecuencias(iterable):
    contador = {}
    for item in iterable:
        if item in contador:
            contador[item] += 1
        else:
            contador[item] = 1
    return contador

print(frecuencias([1,5,4,2,1,5,4,7,8,9,8,1]))

# =====================================================
#   EJERCICIO 2: SUMA ACOTADOS
# =====================================================
# Construir una función que se llame suma_acotados. Esta función debe tomar un
# número arbitrario de argumentos posicionales y un keyword argument llamado
# cota que por defecto debe tener el valor None.
#
# - Si el argumento cota es None, debe sumar todos los números.
# - Si cota tiene un valor, debe sumar solo los números que se encuentren
#   entre -cota y cota.

def suma_acotados(*args, cota=None):
    if cota is None:
        suma = 0
        for num in args:
            suma += num
    else:
        suma = 0
        for num in args:
            if -cota <= num <= cota:
                suma += num
    return suma

print(suma_acotados(6,2,3,8,9,7,5,1,3,2,5,4,8))

print(suma_acotados(6,2,3,8,9,7,5,1,3,2,5,4,8, cota=5))

# =====================================================
#   EJERCICIO 3: ORDENAR PRODUCTOS POR PRECIO
# =====================================================
# Supongamos que tenemos una lista de tuplas en donde cada una contiene el
# nombre de un producto y el precio correspondiente. Por ejemplo:
# [("Campera", 3500), ("Mochila", 2400), ("Zapatillas", 5200), ("Jean", 1600)]
#
# Ordenar los productos según su precio de mayor a menor usando sorted, map
# y funciones lambda.

productos = [("Campera", 3500), ("Mochila", 2400), ("Zapatillas", 5200), ("Jean", 1600)]

print(list(map(lambda x: x[0], sorted(productos, key=lambda x: x[1], reverse=True))))

# =====================================================
#    FIN DESAFÍOS MÓDULO 02 - PYTHON PARA ANÁLISIS DE DATOS
# =====================================================