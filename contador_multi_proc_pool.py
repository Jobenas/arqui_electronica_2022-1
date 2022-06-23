import time
from multiprocessing import Pool, cpu_count, current_process

CUENTA = 100000000

num_proc = 16

def cuenta(n):
    print(f"El proceso {current_process().name} ha iniciado")
    while n > 0:
        n -= 1
    print(f"El proceso {current_process().name} ha terminado")

if __name__ == '__main__':
    inputs = [CUENTA / num_proc for _ in range(num_proc)]
    pool = Pool(processes=cpu_count())

    inicio = time.perf_counter()
    pool.map(cuenta, inputs)
    pool.close()
    pool.join()
    fin = time.perf_counter()
    print(f"Tiempo de ejecucion para {num_proc} procesos {fin - inicio} segundos")