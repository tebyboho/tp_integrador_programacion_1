'''
🛒 Descripción del problema
Una persona está haciendo las compras del mes y tiene una lista con varios productos. Al momento de revisar el ticket de compra (que tiene los productos listados en forma alfabética), quiere saber si ciertos productos específicos fueron comprados.
'''

import math


productos = [
    "Aceite", "Arroz", "Azúcar", "Café", "Cereales", "Detergente", "Fideos", 
    "Galletas", "Harina", "Jabón", "Leche", "Manteca", "Pan", "Papel higiénico", 
    "Queso", "Sal", "Salsa", "Shampoo", "Yerba"
]


producto_objetivo = "Pan"

# -----------------------------
# 1. Búsqueda Lineal
# -----------------------------
def busqueda_lineal(lista, objetivo):
    
    # 13 iteraciones
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


# -----------------------------
# 2. Búsqueda Binaria
# -----------------------------
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    # 4 iteraciones
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1



print("🔎 Búsqueda lineal:", busqueda_lineal(productos, producto_objetivo))
print("🔎 Búsqueda binaria:", busqueda_binaria(productos, producto_objetivo))

