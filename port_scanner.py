import socket
import sys

def scan_host(host='127.0.0.1', start=1, end=1024):
    open_ports = []
    for port in range(start, end+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
        except KeyboardInterrupt:
            break
        finally:
            sock.close()
    return open_ports

if __name__ == "__main__":
    host = input("Host (default 127.0.0.1): ") or "127.0.0.1"
    ports = scan_host(host, 1, 1024)
    print(f"Open ports on {host}: {ports}")
