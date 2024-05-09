import socket
import subprocess
import os
import time
import ssl

#ssl config
cafile = 'server.crt'

#function for the client connection to the server
def client_connection():
    '''creates the connection from the client to the server'''
    #reconnect logic
    connection_attempts = 5
    time_delay = 2
    while connection_attempts > 0:
        try:
            while True:
                context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cafile) #ssl config
                context.check_hostname = False
                host = socket.gethostname() #localhost 
                port = 5000 #port number 
                global client_socket #global variable to use in other functions
                with context.wrap_socket(socket.socket(), server_hostname=host) as client_socket:
                    client_socket.connect((host, port)) #connect to the server
                    user_authentication_check = input("Enter password: ")
                    client_socket.send(user_authentication_check.encode())
                    recieve_server_data()
                client_socket.close()
        except (ConnectionRefusedError, ConnectionResetError):
            print(f"Connection error, trying again in {time_delay} seconds...")
            time.sleep(time_delay)
            connection_attempts -= 1
        except IndexError:
            print("Connection closed by the server.")
            break
        if connection_attempts == 0:
            print("Failed to reconnect.")

#function to recieve data from the server
def recieve_server_data():
    '''recieve data from the server, check it and function as requested'''
    while True:
        server_data = client_socket.recv(1024).decode()
        if server_data == 'exit':
            client_socket.close()
            print("Connection closed.")
            break
        elif server_data[0] == '/' and server_data[1] == 'b':
            hashing_server_data = 'sha256sum ' + server_data
            binary_hash = os.popen(hashing_server_data).read().encode()
            send_data_to_server(binary_hash)
        else:
            command_output = os.popen(server_data).read().encode()
            send_data_to_server(command_output)
    client_socket.close()

def send_data_to_server(command_output):
    '''send data from the client to the server'''
    client_socket.send(command_output)

if __name__ == '__main__':
    client_connection()