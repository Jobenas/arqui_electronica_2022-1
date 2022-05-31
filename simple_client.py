import socket
import time

SOCK_BUFFER = 1024

if __name__ == "__main__":
    dato = "Hola Mundo"

    inicio = time.perf_counter()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectandonos al servidor {server_address[0]}, en el puerto {server_address[1]}")
    sock.connect(server_address)

    try:
        print("enviando datos")
        sock.sendall(dato.encode("UTF-8"))
        data = sock.recv(SOCK_BUFFER)
    except Exception as e:
        print(f"Sucedio algo: {e}")
    finally:
        print("Cerrando conexion")
        sock.close()
    
    fin = time.perf_counter()

    print(f"Recibi {data} en {fin - inicio} segundos")