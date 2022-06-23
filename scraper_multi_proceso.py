import requests
import multiprocessing as mp
import time

session = None

def set_global_session():
    global session

    if not session:
        session = requests.Session()


def get_site(url: str):
    with session.get(url) as response:
        name = mp.current_process().name
        print(f"{name}: leyo {len(response.content)} bytes de {url}")


def get_all(sites: list[str]):
    with mp.Pool(initializer=set_global_session, processes=mp.cpu_count()) as pool:
        pool.map(get_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    inicio = time.perf_counter()
    get_all(sites)
    fin = time.perf_counter()

    print(f"Descarga completa multi procesos en {fin - inicio} segundos")