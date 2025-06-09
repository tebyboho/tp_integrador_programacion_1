import time
import random

# -------------------- GENERACIÓN DE DATOS --------------------

# Generador de nombres aleatorios (combinación de letras)
def generar_nombres(cantidad):
    nombres = []
    for _ in range(cantidad):
        nombre = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(5, 10)))
        nombres.append(nombre)
    return nombres

# Lista grande de nombres desordenados
nombres_grandes = generar_nombres(500)

# -------------------- ALGORITMO: Bubble Sort (in-place) --------------------

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# -------------------- ALGORITMO: Merge Sort (devuelve nueva lista) --------------------

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# -------------------- PRUEBAS Y COMPARACIÓN --------------------

lista_bubble = nombres_grandes.copy()
lista_merge = nombres_grandes.copy()

inicio_bubble = time.perf_counter()
bubble_sort(lista_bubble)
fin_bubble = time.perf_counter()

inicio_merge = time.perf_counter()
lista_merge_ordenada = merge_sort(lista_merge)
fin_merge = time.perf_counter()

# -------------------- RESULTADOS --------------------

print("Cantidad de nombres:", len(nombres_grandes))
print("\nBubble Sort - Tiempo:", round((fin_bubble - inicio_bubble) * 1000, 3), "milisegundos")
print("Merge Sort  - Tiempo:", round((fin_merge - inicio_merge) * 1000, 3), "milisegundos")

# Mostrar primeros 10 resultados ordenados (para comprobar visualmente)
print("\nPrimeros 10 nombres ordenados con Bubble Sort:", lista_bubble[:10])
print("Primeros 10 nombres ordenados con Merge Sort: ", lista_merge_ordenada[:10])

# Comparación de eficiencia
if (fin_bubble - inicio_bubble) > (fin_merge - inicio_merge):
    print("\nConclusión: Merge Sort fue más rápido.")
else:
    print("\nConclusión: Bubble Sort fue más rápido (esto puede variar por el contenido aleatorio).")

