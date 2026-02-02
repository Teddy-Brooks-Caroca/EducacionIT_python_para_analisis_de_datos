# =====================================================
#   PYTHON PARA ANÁLISIS DE DATOS
#   MÓDULO 01 – DESAFÍOS
# =====================================================

# =====================================================
#   EJERCICIO 1: PROMEDIO DE UNA LISTA
# =====================================================
# Dada una lista de números encontrar el promedio de sus elementos:
#
# 1. Sin usar ninguna función.

numeros = [6,3,2,5,4,8,4,5,9,6,8,5,1,5]

suma = 0
n = 0
for num in numeros:
    suma += num
    n += 1

print(suma/n)

# 2. Usando funciones incorporadas de Python.

numeros = []

cantidad_numeros = int(input("Cuantos numeros desea introducir: "))

contador = 0

while cantidad_numeros > contador:
    nuevo_numero = int(input("Ingrese nuevo numero: "))
    numeros.append(nuevo_numero)
    contador = contador + 1

promedio = sum(numeros) /cantidad_numeros  

print(f"Su promedio es:{promedio}")

# =====================================================
#   EJERCICIO 2: MÚLTIPLOS DE 5
# =====================================================
# Crear una lista con los primeros 10 múltiplos de 5:
#
# 1. Usando bucles tradicionales.

multiplos_5 = []

for n in range(10):
    multiplos_5.append(5 * n)

print(multiplos_5)

# 2. Usando listas por comprensión.

multiplos = [5*i for i in range(10)]

print(multiplos)

# =====================================================
#   EJERCICIO 3: DIFERENCIA DE LISTAS
# =====================================================
# Dadas dos listas, crear otra que tenga los elementos que están en la primera
# y que no están en la segunda:
#
# 1. Usando bucles tradicionales.

lista1 = [0,1,2,3,2,3,1,5,4,5,4,6,3,5]
lista2 = [4,5,6,7,8,9]

resta = []

for item in lista1:
    if item not in lista2:
        resta.append(item)

print(resta)

# 2. Usando listas por comprensión.

resta_comp = [item for item in lista1 if item not in lista2]

print(resta_comp)

# Cada elemento debe aparecer tantas veces como en la lista original.

# =====================================================
#    FIN DESAFÍOS MÓDULO 01 - PYTHON PARA ANÁLISIS DE DATOS
# =====================================================