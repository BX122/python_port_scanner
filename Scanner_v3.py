import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout=1):
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			if s.connect_ex((host,port)) != 0:
				return None
			banner = ""
			try:
				s.send(b"\r\n")
				banner = s.recv(1024).decode(errors="ignore").strip()
			except socket.error:
				pass
			return port, banner
	except socket.error:
		return None
def main():
	parser = argparse.ArgumentParser (description="simple multithreaded port scanner (educational use only)")
	parser.add_argument("host", help="Target host or IP")
	parser.add_argument("-s", "--start", type=int, default=1, help="start port")
	parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
	parser.add_argument("-t", "--threads", type=int, default=100, help="Number of Threads")
	args = parser.parse_args()

	print(f"Scanning {args.host} ports {args.start}-{args.end}...")
	with ThreadPoolExecutor(max_workers=args.threads) as ex:
		results = ex.map(lambda p: scan_port(args.host, p), range(args.start,args.end + 1))
		for r in results:
			if r:
				port, banner = r
				print(f"[+] {port}/tcp open {banner[:60]}")
if __name__ == "__main__":
	main()                            