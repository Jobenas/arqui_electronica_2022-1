import random
import concurrent.futures
from threading import Lock

SENTINEL = object()

c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


def productor(pipeline):
    for _ in range(10):
        message = random.randint(1, 100)
        print(c[1] + f"Productor ha generado el mensaje {message}")
        pipeline.set_message(message, "Productor")
    
    pipeline.set_message(SENTINEL, "Productor")

    print(c[0] + "Fin del productor")


def consumidor(pipeline):
    message = 0

    while message is not SENTINEL:
        message = pipeline.get_message("Consumidor")
        if message is not SENTINEL:
            print(c[2] + f"Consumidor ha obtenido el mensaje {message}")
    
    print(c[0] + "Fin del consumidor")


class Pipeline:
    def __init__(self):
        self.message = 0
        self.productor_lock = Lock()
        self.consumidor_lock = Lock()
        self.consumidor_lock.acquire()

    def get_message(self, name):
        print(c[2] + f"{name} a punto de adquirir el candado get")
        self.consumidor_lock.acquire()
        print(c[2] + f"{name} ha adquirido el candado get")
        message = self.message
        print(c[2] + f"{name} a punto de liberar el candado set")
        self.productor_lock.release()
        print(c[2] + f"{name} ha liberado el candado set")

        return message
    
    def set_message(self, message, name):
        print(c[1] + f"{name} a punto de adquirir el candado set")
        self.productor_lock.acquire()
        print(c[1] + f"{name} ha adquirido el candado set")
        self.message = message
        print(c[1] + f"{name} ha punto de liberar el candado get")
        self.consumidor_lock.release()
        print(c[1] + f"{name} ha liberado el candado get")


if __name__ == "__main__":
    pipeline = Pipeline()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(productor, pipeline)
        executor.submit(consumidor, pipeline)