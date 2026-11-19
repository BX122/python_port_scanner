import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host, port)) == 0:
                return port
    except socket.error:
        pass
    return None

def scan(host, start, end, threads=100):
    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda p: scan_port(host, p), range(start, end + 1))
        open_ports = [p for p in results if p]
    return open_ports

if __name__ == "__main__":
    host = "127.0.0.1"
    ports = scan(host, 1, 1024)
    for p in ports:
        print(f"[+] port {p} is open")        