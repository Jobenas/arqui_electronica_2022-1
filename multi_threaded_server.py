import socket
from threading import Thread

SOCK_BUFFER = 1024

contador_hilos = 0

def client_handler(conn, client_address):
    global contador_hilos

    contador_hilos += 1

    print(f"Tengo {contador_hilos} hilos corriendo en este momento")

    try:
        print(f"Conexion de {client_address}")

        while True:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data} de {client_address}")
                conn.sendall(data)
            else:
                break
    except Exception as e:
        print(f"Excepcion {e}")
    finally:
        print("El cliente ha cerrado la conexion")
        conn.close()

    contador_hilos -= 1

if __name__ == '__main__':
    sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en {server_address[0]}, en puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones")

        conn, client_address = sock.accept()

        t = Thread(target=client_handler, args=(conn, server_address))
        t.start()

    