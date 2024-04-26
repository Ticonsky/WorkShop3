import time
import psutil
import functools

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

