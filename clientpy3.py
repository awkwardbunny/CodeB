import socket
import sys

def run(user, password, * commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()

def get_status(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\n" + 'STATUS' + "\nCLOSE_CONNECTION\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        output = []
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            output += [rline.strip()]
            rline = sfile.readline()
    return output

def get_config(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\n" + 'CONFIGURATIONS' + "\nCLOSE_CONNECTION\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        output = []
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            output += [rline.strip()]
            rline = sfile.readline()
    return output
    
def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\nSUBSCRIBE\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
