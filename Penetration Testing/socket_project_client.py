import socket

def client_program():
    host = socket.gethostbyname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port)) #connects to the server

    message = input("Enter a command to pass to the server: ") #take user input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) #send message
        data = client_socket.recv(1024).decode #recieve response

        print(f"Recieved from server: {data}")

        message = input(" -> ") #take input again

    client_socket.close()

if __name__ == '__main__':
    client_program()



