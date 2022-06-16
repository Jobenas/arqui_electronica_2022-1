import socket
import time
import random

MSG_NUM = 10
SOCK_BUFFER = 4 

SLEEP_TIME = 2

var_global = random.randint(1, 20)

def imprime_inicio():
    global var_global

    print(f"El valor de la variable global es {var_global}")

if __name__ == '__main__':
    imprime_inicio()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.0.9", 5000)

    print(f"Conectando al servidor -> {server_address[0]}, en el puerto -> {server_address[1]}")

    sock.connect(server_address)
    print("Conexion establecida")

    try:
        for i in range(MSG_NUM):
            msg = f"Este es el mensaje de prueba {i + 1}"
            msg = msg.encode("utf-8")
            sock.sendall(msg)
            amnt_recvd = 0
            amnt_expected = len(msg)
            msg_rx = ""

            while amnt_recvd < amnt_expected:
                data = sock.recv(SOCK_BUFFER)
                amnt_recvd += len(data)
                msg_rx += data.decode("utf-8")
            print(f"Mensaje completo: {msg_rx}")
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("Usuario cancelo el programa")
        sock.close()
    except Exception as e:
        print(f"Excepcion: {e}")
        sock.close()
    finally:
        print("Cierro conexion")
        sock.close()
