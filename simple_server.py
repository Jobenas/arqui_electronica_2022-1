import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5000)
    sock.bind(server_address)

    sock.listen(5)
    
    while True:
        print("Esperando conexiones")
        
        conn, client_address = sock.accept()
        print(f"Recibi conexion de cliente {client_address}")

        try:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data}")
                conn.sendall(b'ACK')
        except Exception as e:
            print(f"Sucedio algo: {e}")
        finally:
            print("cliente cerro la sesion")
            conn.close()