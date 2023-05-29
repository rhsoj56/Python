import socket

#define connection

def server_program():
    host = socket.gethostbyname
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept() #accept a new connection

    print(f"New connection from: {address}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"From connected user: {data}")
        data = input(" -> ") #send data to client
        conn.send(data.encode())
    
    conn.close()

if __name__ == '__main__':
    server_program()