import socket
import subprocess
import ssl
import logging

#logging config
logger = logging.getLogger(__name__)
logging.basicConfig(filename='server_log.log', encoding='utf-8', level=logging.DEBUG, format=("%(asctime)s  - %(message)s"))

#ssl config
certfile = 'server.crt'
keyfile = 'server.key'

valid_authentication = 'frank' #password for authentication

print("### INCIDENT RESPONSE TOOL ###\n Waiting for a connection...") #banner

#server function that handles the connection
def server_connection():
    '''creates the socket for the client to connect to'''
    host = socket.gethostname()
    port = 5000
    with socket.socket() as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(2)
        #ssl config
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        server_socket = context.wrap_socket(server_socket, server_side=True)
        global conn
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        #authenticate user
        print("Waiting for client authentication...")
        authentication_data = conn.recv(1024).decode()
        if authentication_data == valid_authentication:
            command_line_interface()
        else:
            conn.close()
        conn.close()

def command_line_interface():
    '''CLI where users select a command via a number, the command is pulled from a dictionary and sent to the client'''
    while True:
        try:
            print("### COMMAND MENU ###\n[1] - exit\n[2] - pwd\n[3] - df -h\n[4] - check hash\n[5] - id\n[6] - cpu usage\n[7] - close server\n[8] - os information\n") #CLI menu
            commands_library = {1:'exit', 2:'pwd', 3:'df -h', 4:hash_checker, 5:'id', 6:'vmstat', 8:'uname -a ; cat /etc/os-release'} #dictionary with commands
            server_data = input("Enter a number: ")
            command_id = int(server_data)
            if server_data == '7':
                break
            if command_id not in commands_library:
                print("\nEnter a valid number!\n")
                continue
            cmd = commands_library.get(int(server_data))
            logging.info(f"Command selected: {cmd}")
            if callable(cmd):
                cmd()
            else:
                send_data_to_client(cmd)
                recieve_data_from_client()
        except ValueError:
            print("\nPlease enter a number.\n")

#functions called by the CLI
def send_data_to_client(server_data):
    '''send encoded data from the server to the client'''
    conn.send(server_data.encode())
    print(f"\n### SEND TO CLIENT ###\n{server_data}")

def recieve_data_from_client():
    '''recieve and decode data from client'''
    client_data = conn.recv(1024).decode()
    logging.info(f"Data recieved from client: {client_data}")
    print(f"\n### RESPONSE FROM CLIENT ###\n{client_data}\n")

def server_check_binary_hash(file):
    '''check the binary hash on the server'''
    server_data = 'sha256sum ' + file
    binary_hash = subprocess.run(server_data, shell=True, capture_output=True, text=True)
    hash_output = binary_hash.stdout
    print(f"### SECURE HASH ###\n{hash_output}")

def hash_checker():
    '''check hash of binary with user input to declare which binary to check'''
    binary_to_check = input("Enter binary filepath to check e.g. /bin/pwd: ")
    if binary_to_check == '' or '/' not in binary_to_check:
        print("\nEnter a valid filepath!\n")
    else:
        send_data_to_client(binary_to_check)
        client_hash = recieve_data_from_client()
        server_hash = server_check_binary_hash(binary_to_check)
        if client_hash == server_hash:
            print("Hashes are the same!\n")

if __name__ == '__main__':
    server_connection()