import socket
import threading
import json
import csv
from queue import Queue

COMMON_PORTS = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    3306: 'MySQL',
    3389: 'RDP',
    5900: 'VNC',
    8080: 'HTTP-Alt'
}

scan_results = []
queue = Queue()

def banner_grab(sock):
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode('utf-8').strip()
        return banner
    except:
        return ""

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        banner = banner_grab(s)
        service = COMMON_PORTS.get(port, 'Unknown')
        scan_results.append({
            'port': port,
            'status': 'OPEN',
            'service': service,
            'banner': banner
        })
    except:
        scan_results.append({
            'port': port,
            'status': 'CLOSED',
            'service': '',
            'banner': ''
        })
    s.close()

def worker(host):
    while not queue.empty():
        port = queue.get()
        scan_port(host, port)
        queue.task_done()

def run_scan(host, start_port, end_port, thread_count=50):
    for port in range(start_port, end_port + 1):
        queue.put(port)

    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(host,))
        t.daemon = True
        t.start()
        threads.append(t)

    queue.join()
    return scan_results

def save_results_json(results, filename='scan_results.json'):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

def save_results_csv(results, filename='scan_results.csv'):
    keys = ['port', 'status', 'service', 'banner']
    with open(filename, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Advanced Network Port Scanner')
    parser.add_argument('host', help='Host to scan (IP or domain)')
    parser.add_argument('start_port', type=int, help='Start port number')
    parser.add_argument('end_port', type=int, help='End port number')
    parser.add_argument('--threads', type=int, default=50, help='Number of threads (default 50)')
    parser.add_argument('--json', action='store_true', help='Save results to JSON')
    parser.add_argument('--csv', action='store_true', help='Save results to CSV')

    args = parser.parse_args()

    print(f"Scanning {args.host} ports {args.start_port} to {args.end_port} with {args.threads} threads...")

    results = run_scan(args.host, args.start_port, args.end_port, args.threads)

    for r in sorted(results, key=lambda x: x['port']):
        print(f"Port {r['port']:5} [{r['status']:6}] Service: {r['service']:8} Banner: {r['banner']}")

    if args.json:
        save_results_json(results)
        print("Results saved to scan_results.json")

    if args.csv:
        save_results_csv(results)
        print("Results saved to scan_results.csv")
