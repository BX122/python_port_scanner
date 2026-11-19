import socket

def scan_port(host, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port)) 
    s.close()
    return result == 0

host = "127.0.0.1"
for port in range(1, 1024):
    if scan_port(host, port):
        print(f"[+] port {port} is open")