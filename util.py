import time
from matplotlib import pyplot as plt

#принимает функцию, аргументы для нее и 
# количество итераций проверки функции, 
# возвращает минимальное время работы
def timed(f, *args, n_iter = 100):
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

#декоратор со словарем, хранящим вычисленные значения, 
# аналог: lru_cache
def memo(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

#сравнивает время работы функций через график
def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label = f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()