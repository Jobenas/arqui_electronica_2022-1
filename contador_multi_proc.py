import time
from multiprocessing import Process, cpu_count, current_process

CUENTA = 100000000

num_proc = cpu_count() * 2
procesos = []

def cuenta(n):
    print(f"El proceso {current_process().name} ha iniciado")
    while n > 0:
        n -= 1
    print(f"El proceso {current_process().name} ha terminado")

if __name__ == '__main__':
    for i in range(num_proc):
        p = Process(target=cuenta, args=(CUENTA / num_proc, ))
        procesos.append(p)
    inicio = time.perf_counter()
    for p in procesos:
        p.start()
    
    for p in procesos:
        p.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion para {num_proc} procesos {fin - inicio} segundos")