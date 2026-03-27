# Instalar matplot para la correcta ejecución del programa

pip install matplot

## Gráficas creadas

<img width="1791" height="497" alt="image" src="https://github.com/user-attachments/assets/502c449d-b001-4bc5-bdf7-c28de781d199" />

# Visualizador de Árboles de Recursión

Herramienta educativa en Python que genera y visualiza árboles de llamadas para algoritmos recursivos, permitiendo observar cómo se expande la recursión y comparar diferentes estrategias de optimización.

## Descripción

Este programa construye representaciones visuales de la estructura de llamadas recursivas. Cada nodo del árbol representa una invocación de la función, y las conexiones muestran las llamadas hijas generadas.

El objetivo es facilitar la comprensión de:
- Cómo crece el árbol de llamadas en diferentes algoritmos
- El impacto de técnicas como la memorización (memoization)
- La diferencia en complejidad entre estrategias recursivas

## Algoritmos Incluidos

### Fibonacci
Dos implementaciones para comparar:

| Versión | Complejidad Temporal | Complejidad Espacial |
|---------|---------------------|---------------------|
| Sin memoria | O(2ⁿ) | O(n) |
| Con memoria | O(n) | O(n) |

### Búsqueda Binaria
Implementación recursiva que muestra cómo el espacio de búsqueda se reduce a la mitad en cada llamada.

| Algoritmo | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| Búsqueda binaria | O(log n) | O(log n) |

## Uso

```bash
python recursion_trees.py
```

### Ejemplo de Salida

```
======================================================================
FIBONACCI SIN MEMORIA DINAMICA
======================================================================

Arbol de llamadas:
└── fib(6)
    ├── fib(5)
    │   ├── fib(4)
    │   │   ├── fib(3)
    │   │   │   ├── fib(2)
    │   │   │   │   ├── fib(1)
    │   │   │   │   └── fib(0)
    │   │   │   └── fib(1)
    │   │   └── fib(2)
    │   │       ├── fib(1)
    │   │       └── fib(0)
    │   └── fib(3)
    │       ├── fib(2)
    │       │   ├── fib(1)
    │       │   └── fib(0)
    │       └── fib(1)
    └── fib(4)
        ├── fib(3)
        │   ├── fib(2)
        │   │   ├── fib(1)
        │   │   └── fib(0)
        │   └── fib(1)
        └── fib(2)
            ├── fib(1)
            └── fib(0)

Resumen:
Resultado: 8
Total de llamadas: 25
```

Con memorización, el mismo cálculo requiere solo 11 llamadas, y los valores ya calculados se marcan con `[memo=valor]`.

## API

### Funciones Principales

```python
fibonacci_recursivo(n: int) -> tuple[int, Nodo, int]
```
Calcula Fibonacci sin optimización. Retorna el resultado, el árbol de llamadas y el total de invocaciones.

```python
fibonacci_recursivo_memoria(n: int, memo: dict | None = None) -> tuple[int, Nodo, int]
```
Calcula Fibonacci con memorización. Los nodos que usan valores en caché se etiquetan apropiadamente.

```python
busqueda_binaria_arbol(arreglo: list[int], objetivo: int, izquierda: int, derecha: int) -> tuple[int, Nodo, int]
```
Búsqueda binaria que construye el árbol mostrando cómo se reduce el espacio de búsqueda.

```python
imprimir_arbol(nodo: Nodo, prefijo: str = "", es_ultimo: bool = True) -> None
```
Imprime cualquier árbol de llamadas con formato visual jerárquico.

### Estructura de Nodo

```python
Nodo = {
    "etiqueta": str,  # Descripción de la llamada
    "hijos": list     # Nodos generados por llamadas recursivas
}
```

## Extensibilidad

Para agregar un nuevo algoritmo recursivo:

1. Crear la función que retorne `tuple[resultado, Nodo, llamadas]`
2. Usar `crear_nodo()` al inicio de cada llamada
3. Agregar nodos hijos con `nodo_actual["hijos"].append(hijo)`
4. Visualizar con `imprimir_arbol()`

Ejemplo mínimo:

```python
def factorial_arbol(n: int) -> tuple[int, Nodo, int]:
    nodo = crear_nodo(f"fact({n})")
    
    if n <= 1:
        return 1, nodo, 1
    
    resultado, hijo, llamadas = factorial_arbol(n - 1)
    nodo["hijos"].append(hijo)
    
    return n * resultado, nodo, 1 + llamadas
```

## Requisitos

- Python 3.10+

Sin dependencias externas.

## Contexto Académico


Permite visualizar conceptos como:
- Explosión exponencial en recursión sin memoria
- Eficiencia de programación dinámica top-down
- Comportamiento logarítmico de divide y vencerás

## Licencia

MIT
