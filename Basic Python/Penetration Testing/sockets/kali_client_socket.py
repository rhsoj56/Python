import socket

target_machine = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1' #in the actual instance, this would be set to our server
port = 12345 #port 80 for testing purposes, could use something less obvious irl

target_machine.connect((ip, port))
print("Succesfully connected")

print(target_machine.recv(1024).decode())

target_machine.close()


