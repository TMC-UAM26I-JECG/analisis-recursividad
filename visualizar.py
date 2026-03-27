import time
import random
import matplotlib.pyplot as plt
import sys

# Aumentamos el límite de recursión por si acaso
sys.setrecursionlimit(2000)

# --- FUNCIONES DE PRUEBA (Versiones simplificadas para medición) ---

def fib_recursivo(n):
    if n <= 1: return n
    return fib_recursivo(n-1) + fib_recursivo(n-2)

def fib_memo(n, memo=None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def busqueda_binaria(arr, obj, izq, der):
    if izq > der: return -1
    medio = (izq + der) // 2
    if arr[medio] == obj: return medio
    if obj < arr[medio]:
        return busqueda_binaria(arr, obj, izq, medio - 1)
    return busqueda_binaria(arr, obj, medio + 1, der)

# --- RECOLECCIÓN DE DATOS ---

def medir_rendimiento():
    # 1. Exponencial: Fibonacci Simple (Rango pequeño porque es LENTO)
    n_exp = list(range(10, 32)) 
    tiempos_exp = []
    for n in n_exp:
        inicio = time.time()
        fib_recursivo(n)
        tiempos_exp.append(time.time() - inicio)

    # 2. Lineal: Fibonacci con Memoria (Rango grande)
    n_lin = list(range(10, 501, 20))
    tiempos_lin = []
    for n in n_lin:
        inicio = time.time()
        fib_memo(n)
        tiempos_lin.append(time.time() - inicio)

    # 3. Logarítmica: Búsqueda Binaria (Rango muy grande)
    # Creamos arreglos aleatorios ordenados de tamaños crecientes
    n_log = [100, 1000, 10000, 50000, 100000, 500000, 1000000, 2000000]
    tiempos_log = []
    for n in n_log:
        arreglo = sorted([random.randint(0, n*10) for _ in range(n)])
        objetivo = -1 # Forzamos el peor caso (que no esté)
        inicio = time.time()
        busqueda_binaria(arreglo, objetivo, 0, len(arreglo) - 1)
        tiempos_log.append(time.time() - inicio)

    # --- GENERACIÓN DE GRÁFICAS ---
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    # Gráfica Exponencial O(2^n)
    axs[0].plot(n_exp, tiempos_exp, 'r-o')
    axs[0].set_title("Exponencial: Fibonacci Recursivo\n$O(2^n)$")
    axs[0].set_xlabel("Valor de n")
    axs[0].set_ylabel("Tiempo (segundos)")

    # Gráfica Lineal O(n)
    axs[1].plot(n_lin, tiempos_lin, 'g-s')
    axs[1].set_title("Lineal: Fibonacci con Memoria\n$O(n)$")
    axs[1].set_xlabel("Valor de n")
    axs[1].set_ylabel("Tiempo (segundos)")

    # Gráfica Logarítmica O(log n)
    axs[2].plot(n_log, tiempos_log, 'b-^')
    axs[2].set_title("Logarítmica: Búsqueda Binaria\n$O(\log n)$")
    axs[2].set_xlabel("Tamaño del Arreglo")
    axs[2].set_ylabel("Tiempo (segundos)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    medir_rendimiento()