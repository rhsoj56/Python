import socket

kali_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345

kali_server.bind(('', port)) #empty '' means the server will listen for ip

kali_server.listen(2) #listen for connection
print("Listening...")

conn, addr = kali_server.accept()
print(f"Connection from {addr}")

conn.send("Thanks for connecting".encode())

conn.close()

#