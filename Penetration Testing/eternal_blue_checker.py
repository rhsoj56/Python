import sys
import socket
import pyfiglet

#port scan

ip = input("Please enter the IP address of the TARGET machine: ")
open_ports = []
ports = (139, 445)

def probe_port(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print("Open ports are: ")
    print(sorted(open_ports))
else:
    print("No ports are open this time")

    
#if eternal blue ports are open then test against vuln

stage2 = input("Do you want to proceed? y/n: ")

if stage2 == 'y':
    try:


#if vuln then send payload and set up shell to listen

#else stop