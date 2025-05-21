import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=1) as sock:
            try:
                banner = sock.recv(1024).decode().strip()
                return f"Port {port}: OPEN - {banner}"
            except:
                return f"Port {port}: OPEN"
    except:
        return f"Port {port}: CLOSED"

def run_scan(host, start_port, end_port):
    results = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            results.append(future.result())
    return results
