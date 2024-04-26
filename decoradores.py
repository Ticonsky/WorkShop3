import time
import psutil
import functools
from collections import deque
def calcular_tiempo(funcion):
        def wrapper(*args, **kwargs):
            inicio = time.time()  # Tiempo inicial
            resultado = funcion(*args, **kwargs)
            fin = time.time()  # Tiempo final
            with open("performance.txt","w") as file:
                file.write(f"Tiempo de ejecución de {funcion.__name__}: {fin - inicio} segundos")
            return resultado
        return wrapper


def calcular_memoria(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio_memoria = psutil.Process().memory_info().rss / 1024 / 1024  # Uso de memoria al inicio
        resultado = funcion(*args, **kwargs)  # Llamar a la función original con los argumentos
        fin_memoria = psutil.Process().memory_info().rss / 1024 / 1024  # Uso de memoria al final
        memoria_usada = fin_memoria - inicio_memoria
        with open("performance.txt","w") as file:
            file.write(f"Uso de memoria de {funcion.__name__}: {memoria_usada:.2f} MB")
        return resultado
    return wrapper



def log_funcion(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        with open("actions.txt", "a") as file:
            file.write(f"Llamada a la función {funcion.__name__}\n")
            file.write(f"Argumentos posicionales: {args}\n")
            file.write(f"Argumentos de palabras clave: {kwargs}\n\n")
        return funcion(*args, **kwargs)
    return wrapper


def lru_cache_size(maxsize):
    cache = {}
    queue = deque(maxlen=maxsize)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.items())
            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            if len(queue) == maxsize:
                del cache[queue.popleft()]
            cache[key] = result
            queue.append(key)
            return result
        return wrapper
    return decorator
