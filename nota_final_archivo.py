
import time

nombre_archivo = "notas.csv"

ta = 0
nl = 0

codigos = ["20220001", "20220002", "20220003", "20220004", "20220005", "20220006"]

tiempos_es = []
tiempos_cpu = []
promedios = []

contenido = None

def get_data(codigo: str):
    global contenido

    if contenido is None:
        f = open(nombre_archivo, "r")
        contenido = f.read()
        f.close()

    data = contenido.split("\n")

    for line in data:
        code = line.split(",")
        if code[0] == codigo:
            return code
    
    return []

if __name__ == "__main__":
    inicio = time.perf_counter() 
    for codigo in codigos:
        inicio_es = time.perf_counter()

        notas = get_data(codigo)

        fin_es = time.perf_counter()

        tiempos_es.append(fin_es - inicio_es)

        inicio_cpu = time.perf_counter()

        for i in range(1, len(notas) - 1):
            nl += int(notas[i])
        
        nl /= 10

        ta = int(notas[-1])

        nota_final = ((7 * nl) + (3 * ta)) / 10

        fin_cpu = time.perf_counter()
        tiempos_cpu.append(fin_cpu - inicio_cpu)
        promedios.append(nota_final)
    fin = time.perf_counter()

    print(f"Los promedios son {promedios}")
    print(f"El tiempo total de ejecucion del programa es: {fin - inicio} segundos")
    print(f"Los tiempos de operaciones de entrada/salida por iteracion son: {tiempos_es}")