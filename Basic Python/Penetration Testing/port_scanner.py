import socket
import threading
import pyfiglet
import colorama
import concurrent.futures
from colorama import Fore

colorama.init()
print_lock = threading.Lock()

#print fancy banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#function that defines the socket connection and connects
def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(100)
    try: #test for errors
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
    except: #to handle any errors
        pass

def main():
    ip = input("Enter the IP you want to scan: ")
    print("*** CHECKING PORT RANGE 1 - 65535 ***")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(0xFFFF):
            executor.submit(scan, ip, port + 1)

if __name__ == "__main__":
    main()

#Need to determine what services are on the ports next...