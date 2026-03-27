from __future__ import annotations

from typing import Any

import matplotlib.pyplot as plt
import random

Nodo = dict[str, Any]


def crear_nodo(etiqueta: str) -> Nodo:
    """
    Crea un nodo del árbol de llamadas.

    Cada nodo se representa con un diccionario que contiene:
    - 'etiqueta': texto descriptivo de la llamada actual.
    - 'hijos': lista con los nodos hijos generados por llamadas recursivas.

    Args:
        etiqueta: Texto que identifica la llamada actual.

    Returns:
        Un diccionario que representa un nodo del árbol.
    """
    return {
        "etiqueta": etiqueta,
        "hijos": []
    }


def imprimir_arbol(nodo: Nodo, prefijo: str = "", es_ultimo: bool = True) -> None:
    """
    Imprime un árbol con formato jerárquico.

    La función imprime primero el nodo actual y después recorre
    recursivamente cada uno de sus hijos.

    Args:
        nodo: Nodo actual que se desea imprimir.
        prefijo: Cadena auxiliar para conservar la forma visual del árbol.
        es_ultimo: Indica si el nodo actual es el último hijo de su nivel.

    Returns:
        None.
    """
    if es_ultimo:
        conector = "└── "
        nuevo_prefijo = prefijo + "    "
    else:
        conector = "├── "
        nuevo_prefijo = prefijo + "│   "

    print(prefijo + conector + nodo["etiqueta"])

    cantidad_hijos = len(nodo["hijos"])

    for indice, hijo in enumerate(nodo["hijos"]):
        hijo_es_ultimo = indice == cantidad_hijos - 1
        imprimir_arbol(hijo, nuevo_prefijo, hijo_es_ultimo)


def fibonacci_recursivo(n: int) -> tuple[int, Nodo, int]:
    """
    Calcula Fibonacci de forma recursiva y construye el árbol de llamadas.

    La función regresa tres valores:
    1. El resultado numérico de fib(n).
    2. El nodo raíz del subárbol correspondiente a la llamada actual.
    3. El total de llamadas realizadas dentro de este subproblema.

    Args:
        n: Valor de entrada para Fibonacci.

    Returns:
        Una tupla con:
        - resultado de Fibonacci
        - nodo raíz del árbol de llamadas
        - total de llamadas realizadas
    """
    nodo_actual = crear_nodo(f"fib({n})")

    if n <= 1:
        resultado = n
        total_llamadas = 1
        return resultado, nodo_actual, total_llamadas

    resultado_izquierdo, hijo_izquierdo, llamadas_izquierdas = fibonacci_recursivo(n - 1)
    resultado_derecho, hijo_derecho, llamadas_derechas = fibonacci_recursivo(n - 2)

    nodo_actual["hijos"].append(hijo_izquierdo)
    nodo_actual["hijos"].append(hijo_derecho)

    resultado = resultado_izquierdo + resultado_derecho
    total_llamadas = 1 + llamadas_izquierdas + llamadas_derechas

    return resultado, nodo_actual, total_llamadas


def fibonacci_recursivo_memoria(
    n: int,
    memo: dict[int, int] | None = None
) -> tuple[int, Nodo, int]:
    """
    Calcula Fibonacci con memoria dinámica y construye el árbol de llamadas.

    Si un valor ya fue calculado, no se vuelve a expandir su subárbol.
    En ese caso, el nodo se marca con la leyenda '[memo=valor]'.

    Args:
        n: Valor de entrada para Fibonacci.
        memo: Diccionario que almacena resultados ya calculados.

    Returns:
        Una tupla con:
        - resultado de Fibonacci
        - nodo raíz del árbol de llamadas
        - total de llamadas realizadas
    """
    if memo is None:
        memo = {}

    if n in memo:
        nodo_actual = crear_nodo(f"fib({n}) [memo={memo[n]}]")
        resultado = memo[n]
        total_llamadas = 1
        return resultado, nodo_actual, total_llamadas

    nodo_actual = crear_nodo(f"fib({n})")

    if n <= 1:
        memo[n] = n
        resultado = n
        total_llamadas = 1
        return resultado, nodo_actual, total_llamadas

    resultado_izquierdo, hijo_izquierdo, llamadas_izquierdas = fibonacci_recursivo_memoria(
        n - 1,
        memo
    )
    resultado_derecho, hijo_derecho, llamadas_derechas = fibonacci_recursivo_memoria(
        n - 2,
        memo
    )

    nodo_actual["hijos"].append(hijo_izquierdo)
    nodo_actual["hijos"].append(hijo_derecho)

    resultado = resultado_izquierdo + resultado_derecho
    memo[n] = resultado
    total_llamadas = 1 + llamadas_izquierdas + llamadas_derechas

    return resultado, nodo_actual, total_llamadas


def busqueda_binaria_arbol(
    arreglo: list[int],
    objetivo: int,
    izquierda: int,
    derecha: int
) -> tuple[int, Nodo, int]:
    """
    Realiza búsqueda binaria recursiva y construye el árbol de llamadas.

    Cada llamada genera un nodo con el segmento actual del arreglo que
    está siendo analizado.

    Args:
        arreglo: Lista ordenada en la que se desea buscar.
        objetivo: Valor que se desea encontrar.
        izquierda: Índice izquierdo del rango de búsqueda actual.
        derecha: Índice derecho del rango de búsqueda actual.

    Returns:
        Una tupla con:
        - índice encontrado, o -1 si no existe
        - nodo raíz del árbol de llamadas
        - total de llamadas realizadas
    """
    segmento_actual = arreglo[izquierda:derecha + 1]
    etiqueta = "buscar(" + str(segmento_actual) + ")"
    nodo_actual = crear_nodo(etiqueta)

    total_llamadas = 1

    if izquierda > derecha:
        nodo_actual["etiqueta"] += " -> no encontrado"
        return -1, nodo_actual, total_llamadas

    medio = (izquierda + derecha) // 2

    if arreglo[medio] == objetivo:
        nodo_actual["etiqueta"] += " -> encontrado en indice " + str(medio)
        return medio, nodo_actual, total_llamadas

    if objetivo < arreglo[medio]:
        resultado, hijo, llamadas = busqueda_binaria_arbol(
            arreglo,
            objetivo,
            izquierda,
            medio - 1
        )
        nodo_actual["hijos"].append(hijo)
        total_llamadas = total_llamadas + llamadas
        return resultado, nodo_actual, total_llamadas

    resultado, hijo, llamadas = busqueda_binaria_arbol(
        arreglo,
        objetivo,
        medio + 1,
        derecha
    )
    nodo_actual["hijos"].append(hijo)
    total_llamadas = total_llamadas + llamadas

    return resultado, nodo_actual, total_llamadas


def ejecutar_fibonacci(n: int) -> None:
    """
    Ejecuta y muestra dos versiones de Fibonacci:
    - recursiva simple
    - recursiva con memoria dinámica

    Args:
        n: Valor que se utilizará en la demostración.

    Returns:
        None.
    """
    print("=" * 70)
    print("FIBONACCI SIN MEMORIA DINAMICA")
    print("=" * 70)

    resultado, raiz, total_llamadas = fibonacci_recursivo(n)

    print("\nArbol de llamadas:")
    imprimir_arbol(raiz)

    print("\nResumen:")
    print(f"Resultado: {resultado}")
    print(f"Total de llamadas: {total_llamadas}")

    print("\n" + "=" * 70)
    print("FIBONACCI CON MEMORIA DINAMICA")
    print("=" * 70)

    resultado_memo, raiz_memo, total_llamadas_memo = fibonacci_recursivo_memoria(n)

    print("\nArbol de llamadas:")
    imprimir_arbol(raiz_memo)

    print("\nResumen:")
    print(f"Resultado: {resultado_memo}")
    print(f"Total de llamadas: {total_llamadas_memo}")


def ejecutar_busqueda(arreglo: list[int], objetivo: int) -> None:
    """
    Ejecuta la búsqueda binaria recursiva y muestra su árbol de llamadas.

    Args:
        arreglo: Lista ordenada en la que se realizará la búsqueda.
        objetivo: Valor que se desea localizar.

    Returns:
        None.
    """
    print("=" * 70)
    print("BUSQUEDA BINARIA")
    print("=" * 70)

    resultado, raiz, total_llamadas = busqueda_binaria_arbol(
        arreglo,
        objetivo,
        0,
        len(arreglo) - 1
    )

    print("\nArbol de llamadas:")
    imprimir_arbol(raiz)

    print("\nResumen:")
    print(f"Indice encontrado: {resultado}")
    print(f"Total de llamadas: {total_llamadas}")

def generar_comparativa():
    #1.EXPONENCIAL: Fibonacci Tradicional
    #No podemos pasar de n=25 porque las llamadas crecen demasiado rápido
    n_exp = list(range(1, 23))
    llamadas_exp = []
    for n in n_exp:
        _, _, total = fibonacci_recursivo(n)
        llamadas_exp.append(total)

    #2.LINEAL: Fibonacci con Memoria
    #Aquí sí podemos usar valores más grandes
    n_lin = list(range(1, 101))
    llamadas_lin = []
    for n in n_lin:
        _, _, total = fibonacci_recursivo_memoria(n)
        llamadas_lin.append(total)

    #3.LOGARÍTMICO: Búsqueda Binaria
    #Usamos arreglos de tamaño creciente (hasta 10,000 elementos)
    n_log = [10, 50, 100, 500, 1000, 2500, 5000, 7500, 10000]
    llamadas_log = []
    for tam in n_log:
        # Creamos un arreglo aleatorio ordenado
        arreglo = sorted([random.randint(0, tam * 10) for _ in range(tam)])
        # Buscamos un número que NO esté para forzar el peor caso
        _, _, total = busqueda_binaria_arbol(arreglo, -1, 0, len(arreglo) - 1)
        llamadas_log.append(total)

    #--- RENDERIZADO DE GRÁFICAS ---
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    #Gráfica Exponencial
    ax1.plot(n_exp, llamadas_exp, color='red', marker='o')
    ax1.set_title("Exponencial: fibonacci_recursivo\n(Crecimiento explosivo)")
    ax1.set_xlabel("Valor de n")
    ax1.set_ylabel("Total de llamadas")

    #Gráfica Lineal
    ax2.plot(n_lin, llamadas_lin, color='green', marker='s')
    ax2.set_title("Lineal: fibonacci_memoria\n(Crecimiento constante)")
    ax2.set_xlabel("Valor de n")
    ax2.set_ylabel("Total de llamadas")

    #Gráfica Logarítmica
    ax3.plot(n_log, llamadas_log, color='blue', marker='^')
    ax3.set_title("Logarítmica: busqueda_binaria\n(Crecimiento muy lento)")
    ax3.set_xlabel("Tamaño del arreglo")
    ax3.set_ylabel("Total de llamadas")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generar_comparativa()