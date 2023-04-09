import socket

#establist socket

client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define ip and port
ADDR = socket.gethostbyname("www.google.com")
PORT = 80

#connect
client_connection.connect((ADDR, PORT))

#send
send_get = b'GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n'
client_connection.send(send_get)

#recieve
rx_message = client_connection.recv(4096)
print(rx_message)

#close
socket.close()